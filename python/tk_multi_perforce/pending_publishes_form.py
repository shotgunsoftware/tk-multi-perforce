# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import os
import sgtk
from sgtk.platform.qt import QtCore, QtGui

class PendingPublishesForm(QtGui.QWidget):
    """
    Display a list of Pending publishes from Perforce for the current 
    user & workspace. This list allows the user to commit or revert 
    pending commits
    """
    #restore = QtCore.Signal(QtGui.QWidget, basestring, basestring)
    #snapshot = QtCore.Signal(QtGui.QWidget)
    #closed = QtCore.Signal(QtGui.QWidget)
    
    def __init__(self, app, parent = None):
        """
        Construction
        """
        QtGui.QWidget.__init__(self, parent)
    
        self._app = app
        #self._handler = handler
    
        # set up the UI
        from .ui.pending_publishes_form import Ui_PendingPublishesForm
        self._ui = Ui_PendingPublishesForm()
        self._ui.setupUi(self)
        
        #self._ui.snapshot_list.set_app(self._app)
        #self._ui.snapshot_list.selection_changed.connect(self._on_list_selection_changed)
        #self._ui.snapshot_list.action_requested.connect(self._on_restore)
