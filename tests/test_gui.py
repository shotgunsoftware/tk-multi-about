# Copyright (c) 2019 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import pytest
import subprocess
import time
import os
import sys
import sgtk
from tank_vendor.six.moves import urllib
from tk_toolchain.cmd_line_tools import tk_run_app

try:
    from MA.UI import topwindows
except ImportError:
    pytestmark = pytest.mark.skip()


from sgtk.authentication import ShotgunAuthenticator
from tk_toolchain import authentication


@pytest.fixture(scope="session")
def context():
    # A task in Big Buck Bunny which we're going to use
    # for the current context.
    return {"type": "Task", "id": 3588}


# This fixture will launch tk-run-app on first usage
# and will remain valid until the test run ends.
@pytest.fixture(scope="session")
def host_application(context):
    """
    Launch the host application for the Toolkit application.

    TODO: This can probably be refactored, as it is not
    likely to change between apps, except for the context.
    One way to pass in a context would be to have the repo being
    tested to define a fixture named context and this fixture
    would consume it.
    """
    process = subprocess.Popen(
        [
            "python",
            "-m",
            "tk_toolchain.cmd_line_tools.tk_run_app",
            # Allows the test for this application to be invoked from
            # another repository, namely the tk-framework-widget repo,
            # by specifying that the repo detection should start
            # at the specified location.
            "--location",
            os.path.dirname(__file__),
            "--context-entity-type",
            context["type"],
            "--context-entity-id",
            str(context["id"]),
        ]
    )
    try:
        yield
    finally:
        # We're done. Grab all the output from the process
        # and print it so that is there was an error
        # we'll know about it.
        stdout, stderr = process.communicate()
        sys.stdout.write(stdout or "")
        sys.stderr.write(stderr or "")
        process.poll()
        # If returncode is not set, then the process
        # was hung and we need to kill it
        if process.returncode is None:
            process.kill()
        else:
            assert process.returncode == 0


@pytest.fixture(scope="session")
def about_box(host_application):
    """
    Retrieve the about box and return the AboutBoxAppWrapper.
    """
    before = time.time()
    while before + 30 > time.time():
        if sgtk.util.is_windows():
            about_box = AboutBoxAppWrapper(topwindows)
        else:
            about_box = AboutBoxAppWrapper(topwindows["python"])

        if about_box.exists() == True:
            yield about_box
            about_box.close()
            return
    else:
        raise RuntimeError("Timeout waiting for the about box to launch.")


class BrowserWidget(object):
    """
    Allows to automate GUI interactions with a browser widget.
    """

    # TODO: This should be refactored at some point inside the tk-framework-widget
    # framework, but since this is our first use of the wrapper, let's not over do this.
    # Besides, the breakdown app has some really custom behaviour, so let's not
    # commit to an interface too quickly.

    def __init__(self, parent, title, has_search_bar=False):
        """
        :param parent: Parent widget or QuerySet that can reach the specified title
        :param str title: Title of the browser widget. This is the
            label above the browser view.
        """
        self._title_widget = parent[title]
        self._has_search_bar = has_search_bar

    @property
    def search(self):
        """
        The MA.UI control for the search box.
        """
        assert self._has_search_bar
        return self._title_widget.parent.children[1]

    @property
    def items(self):
        r"""
        List of strings in the browser widget. There is one string per item in the browser.
        ``\n`` will delineate lines in an item.
        """
        if sgtk.util.is_windows():
            view = self._title_widget.parent.parent.children[1][0][0][0][0]
            return [c[0][1].name for c in view.children]
        else:
            # The search box comes before the list view in the children list.
            view = self._title_widget.parent.children[2 if self._has_search_bar else 1]
            assert view.exists()
            # Every other item is some text element.
            return [c.value for i, c in enumerate(view.children) if i % 2 == 1]


class TabWidget(object):
    """
    Abstracts out the differences between platforms when interacting with a tab widget.
    """

    def __init__(self, parent):
        """
        :param parent: Parent widget or QuerySet that can reach the tabs.
        """
        self._parent = parent

    def switch_tab(self, name):
        """
        Switch to the given tab name.

        :param str name: Name of the tab to switch to.
        """
        if sgtk.util.is_windows():
            self._parent.tabs[name].get().mouseClick()
        else:
            self._parent.radioButtons[name].get().mouseClick()


class AboutBoxAppWrapper(object):
    """
    Wrapper around the About Box.
    """

    def __init__(self, parent):
        """
        :param root:
        """
        self._root = parent["Shotgun: Your Current Work Area"].get()

    def exists(self):
        """
        ``True`` if the widget was found, ``False`` otherwise.
        """
        return self._root.exists()

    def close(self):
        self._root.buttons["Close"].get().mouseClick()

    def select_context_tab(self):
        """
        Selects the Current Context tab
        """
        TabWidget(self._root).switch_tab("Current Context")

    def select_active_apps_tab(self):
        """
        Selects the Active Apps tab
        """
        TabWidget(self._root).switch_tab("Active Apps")

    def select_environment_tab(self):
        """
        Selects the Environment tab
        """
        TabWidget(self._root).switch_tab("Environment")

    @property
    def context_browser(self):
        """
        Access the BrowserWidget from the Current Context tab.
        """
        return BrowserWidget(self._root, "Your Current Work Context")

    @property
    def active_apps_browser(self):
        """
        Access the BrowserWidget from the Active Apps tab.
        """
        return BrowserWidget(self._root, "Currently Running Apps", has_search_bar=True)

    @property
    def environment_browser(self):
        """
        Access the BrowserWidget from the Environment tab.
        """
        return BrowserWidget(self._root, "The Current Environment")


def test_context_tab(about_box):
    """
    Ensure the content of the context browser is complete.
    """
    about_box.select_context_tab()
    user = authentication.get_toolkit_user()
    server = urllib.parse.urlparse(user.host).netloc
    # The first line contains the server name, which we do not want to display during
    # automation on the cloud.
    assert about_box.context_browser.items[1:] == [
        "Asset Acorn\nAs to size, Alice hastily but Im not looking for eggs, as it spoke. As wet as ever, said Alice to herself, and fanned herself one",
        "Pipeline Step Art\nNo Description",
        "Task Art\nStatus: fin\nAssigned to: Artist 3",
    ]


def test_active_apps_tab(about_box):
    """
    Ensure the content of the active apps browser is complete.
    """
    about_box.select_active_apps_tab()
    assert about_box.active_apps_browser.items == [
        "About Shotgun Pipeline Toolkit\nVersion: Undefined\nDescription: Shows a breakdown of your current environment and configuration."
    ]


def test_search_box_that_empties_list(about_box):
    """
    Ensure searching for missing keyword returns nothing.
    """
    about_box.select_active_apps_tab()
    about_box.active_apps_browser.search.pasteIn("Workfiles")
    assert about_box.active_apps_browser.items == []


def test_search_box_that_keeps_item(about_box):
    """
    Ensure searching for valid keyword returns something, but
    if you add invalid text then it stops matching.
    """
    about_box.select_active_apps_tab()
    about_box.active_apps_browser.search.pasteIn("about")
    assert about_box.active_apps_browser.items == [
        "About Shotgun Pipeline Toolkit\nVersion: Undefined\nDescription: Shows a breakdown of your current environment and configuration."
    ]
    about_box.active_apps_browser.search.typeIn("zxcxc")
    assert about_box.active_apps_browser.items == []


def test_environment_tab(about_box):
    """
    Ensure the environment box is fully populated.
    """
    about_box.select_environment_tab()
    assert about_box.environment_browser.items == [
        "Engine: tk_testengine\nVersion: Undefined\nDescription: No description available.",
        "Environment: test\nPath: %s\nDescription: No description found."
        % os.path.join(tk_run_app.get_config_location(), "env", "test.yml"),
    ]
