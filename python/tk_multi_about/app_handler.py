"""
Copyright (c) 2012 Shotgun Software, Inc
----------------------------------------------------
"""
import tempfile
import os
import platform
import sys
import uuid
import shutil
import tank

class AppHandler(object):
    """
    Handles the startup of the UIs, wrapped so that
    it works nicely in batch mode.
    """
    
    def __init__(self, app):
        self._app = app
        self._dialogs = []

    def show_dialog(self):
        # do the import just before so that this app can run nicely in nuke
        # command line mode,
        from .dialog import AppDialog
        
        dialog = tank.platform.qt.create_dialog(AppDialog)
        dialog.post_init(self._app)
        # Keep the dialog object from being GC-ed by storing in a member var
        self._dialogs.append(dialog)
        # run modal dialogue
        dialog.show()
        
