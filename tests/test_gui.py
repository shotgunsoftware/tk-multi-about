import pytest
import subprocess
import time
import sgtk

try:
    from MA.UI import topwindows, mouseClick
except ImportError:
    pytestmark = pytest.mark.skip()


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
            about_box = topwindows["Shotgun: Your Current Work Area"]
        else:
            about_box = topwindows["python"]["Shotgun: Your Current Work Area"]

        if about_box.exists() == True:
            return AboutBoxAppWrapper(about_box.get())
    raise RuntimeError("Timeout waiting for about box to launch.")


class AboutBoxAppWrapper(object):
    def __init__(self, about_box):
        self._about_box = about_box
        assert self._about_box.exists()

    def select_context_tab(self):
        mouseClick(self._get_radio_button("Current Context"))

    def select_active_apps_tab(self):
        mouseClick(self._get_radio_button("Active Apps"))

    def select_environment_tab(self):
        mouseClick(self._get_radio_button("Environment"))

    @property
    def context_view(self):
        return self._get_context_view_content("Your Current Work Context")

    @property
    def active_apps_view(self):
        return self._get_context_view_content("Currently Running Apps")

    @property
    def current_environment_view(self):
        return self._get_context_view_content("The Current Environment")

    def _get_radio_button(self, name):
        if sgtk.util.is_windows():
            button = self._about_box.tabs[name]
        else:
            button = self._about_box.radioButtons[name]
        assert button.exists()
        return button

    def _get_context_view_content(self, name):
        if sgtk.util.is_windows():
            browser = self._about_box["context_browser"].get()
            return [c[0][1].name for c in browser.children[1][0][0][0][0].children]
        else:
            context_view = self._about_box[name].parent.children[1]
            assert context_view.exists()
            return [c.value for i, c in enumerate(context_view.children) if i % 2 == 1]


def test_context_tab(about_box):
    about_box.select_context_tab()
    assert about_box.context_view == [
        "Project Big Buck Bunny (jf-dev.shotgunstudio.com)\nBig Buck Bunny is a short computer animated film by the Blender Institute, part of the Blender Foundation.",
        "Asset Acorn\nAs to size, Alice hastily but Im not looking for eggs, as it spoke. As wet as ever, said Alice to herself, and fanned herself one",
        "Pipeline Step Art\nNo Description",
        "Task Art\nStatus: fin\nAssigned to: Artist 3",
    ]


def test_active_apps_tab(about_box):
    about_box.select_active_apps_tab()
    assert about_box.active_apps_view == []


def test_environment_tab(about_box):
    about_box.select_environment_tab()
    assert about_box.current_environment_view == [
        "Engine: tk_testengine\nVersion: Undefined\nDescription: No description available.",
        "Environment: test\nPath: /Users/boismej/gitlocal/tk-toolchain/tk_toolchain/cmd_line_tools/tk_run_app/config/env/test.yml\nDescription: No description found.",
    ]
