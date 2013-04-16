"""
Copyright (c) 2012 Shotgun Software, Inc
----------------------------------------------------

An app that shows information about the current work area.

"""

import sys
import os
import platform

from tank.platform import Application

class AboutTank(Application):
    
    def init_app(self):
        """
        Called as the application is being initialized
        """
        tk_multi_about = self.import_module("tk_multi_about")
        cb = lambda : tk_multi_about.show_dialog(self)
        self.engine.register_command("work_area_info", cb, {"type": "context_menu", title: "Work Area Info..."})

