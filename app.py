# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
General Perforce connection commands
"""

import os
import sgtk
from sgtk import TankError

class PerforceConnect(sgtk.platform.Application):

    def init_app(self):
        """
        Called as the application is being initialized
        """
        
        # register commands:
        self.engine.register_command("Perforce Connection...", self.show_connection_dlg)
        
        #self.engine.register_command("Perforce Check-Out", self.do_check_out)
        #self.engine.register_command("Perforce Revert", self.do_revert)
        
        # support connecting on startup:
        # Note, this runs every time the app is re-initialized (the engine is restarted).
        # however, the UI will only be shown when a connection can't be made with the
        # previous/cached settings so this should be infrequently!
        if self.engine.has_ui:
            connect_on_startup = self.get_setting("connect_on_startup")
            if connect_on_startup:
                self.connect_on_startup()
        
    def destroy_app(self):
        self.log_debug("Destroying tk-multi-perforce")
        
    def connect_on_startup(self):
        """
        """
        tk_multi_perforce = self.import_module("tk_multi_perforce")
        tk_multi_perforce.ConnectionHandler.connect(self)
        
    def show_connection_dlg(self):
        """
        
        """
        tk_multi_perforce = self.import_module("tk_multi_perforce")
        tk_multi_perforce.ConnectionHandler.open_connection(self)
    
    def do_check_out(self):
        """
        """
        pass
    
    def do_revert(self):
        """
        """
        pass
            