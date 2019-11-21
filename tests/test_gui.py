import pytest
import subprocess
import time
import sgtk

try:
    from MA.UI import topwindows, mouseClick
except ImportError:
    pytestmark = pytest.mark.skip()


# tk-run-app should run during the entire test run and not start and
# stop on each test.
@pytest.fixture(scope="session")
def host_application():
    """
    Launches the host application for the Toolkit application.
    """
    process = subprocess.Popen(["tk-run-app", "-e", "Task", "-i", "448"])
    try:
        yield
    finally:
        process.kill()


@pytest.fixture
def about_box(host_application):
    before = time.time()
    while before + 30 > time.time():
        if sgtk.util.is_windows():
            about_box = AboutBoxAppWrapper(topwindows)
        else:
            about_box = AboutBoxAppWrapper(topwindows["python"])

        if about_box.exists() == True:
            return about_box
    raise RuntimeError("Timeout waiting for the about box to launch.")


class BrowserWidget(object):
    """
    Allows to automate GUI interactions with a browser widget.
    """

    # TODO: This should be refactored at some point inside the tk-framework-widget
    # framework, but since this is our first use of the wrapper, let's not over do this.
    # Besides, the breakdown app has some really custom behaviour, so let's not
    # commit to an interace too quickly.

    def __init__(self, title, parent):
        """
        :param parent: Parent widget or QuerySet that can reach the specified title
        :param str title: Title of the browser widget. This is the
            label above the browser view.
        """
        self._title_widget = parent[title].get()

    @property
    def items(self):
        r"""
        List of strings in the browser widget. There is one string per item in the browser.
        ``\n`` will delineate lines in an item.
        """
        if sgtk.util.is_windows():
            return [
                c[0][1].name
                for c in self._title_widget.parent.parent.children[1][0][0][0][
                    0
                ].children
            ]
        else:
            context_view = self._title_widget.parent.children[1]
            assert context_view.exists()
            # Every other item is some text element.
            return [c.value for i, c in enumerate(context_view.children) if i % 2 == 1]


class TabWidget(object):
    """
    Abstracts out the differences between platforms when interacting with a tab widget.
    """

    def __init__(self, parent):
        """
        :param parent: Parent widget or QuerySet that can reach the tabs.
        """
        self._parent = parent

    def switchTab(self, name):
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
        return self._root.exists()

    def select_context_tab(self):
        TabWidget(self._root).switchTab("Current Context")

    def select_active_apps_tab(self):
        TabWidget(self._root).switchTab("Active Apps")

    def select_environment_tab(self):
        TabWidget(self._root).switchTab("Environment")

    @property
    def context_browser(self):
        return BrowserWidget("Your Current Work Context", self._root)

    @property
    def active_apps_browser(self):
        return BrowserWidget("Currently Running Apps", self._root)

    @property
    def current_environment_browser(self):
        return BrowserWidget("The Current Environment", self._root)


def test_context_tab(about_box):
    about_box.select_context_tab()
    assert about_box.context_browser.items == [
        "Project Big Buck Bunny (jf-dev.shotgunstudio.com)\nBig Buck Bunny is a short computer animated film by the Blender Institute, part of the Blender Foundation.",
        "Asset Acorn\nAs to size, Alice hastily but Im not looking for eggs, as it spoke. As wet as ever, said Alice to herself, and fanned herself one",
        "Pipeline Step Art\nNo Description",
        "Task Art\nStatus: fin\nAssigned to: Artist 3",
    ]


def test_active_apps_tab(about_box):
    about_box.select_active_apps_tab()
    assert about_box.active_apps_browser.items == []


def test_environment_tab(about_box):
    about_box.select_environment_tab()
    assert about_box.current_environment_browser.items == [
        "Engine: tk_testengine\nVersion: Undefined\nDescription: No description available.",
        "Environment: test\nPath: /Users/boismej/gitlocal/tk-toolchain/tk_toolchain/cmd_line_tools/tk_run_app/config/env/test.yml\nDescription: No description found.",
    ]
