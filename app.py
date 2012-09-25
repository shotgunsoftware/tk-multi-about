"""
Copyright (c) 2012 Shotgun Software, Inc
----------------------------------------------------

An app that launches revolver from nuke

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
        import tk_multi_about
        self.app_handler = tk_multi_about.AppHandler(self)        
        # add stuff to main menu
        self.engine.register_command("Info about current Work Area...", 
                                     self.app_handler.show_dialog, 
                                     {"type": "context_menu"})

