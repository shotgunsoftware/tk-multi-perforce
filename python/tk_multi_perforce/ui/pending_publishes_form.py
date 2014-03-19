# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pending_publishes_form.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_PendingPublishesForm(object):
    def setupUi(self, PendingPublishesForm):
        PendingPublishesForm.setObjectName("PendingPublishesForm")
        PendingPublishesForm.resize(726, 431)
        self.verticalLayout = QtGui.QVBoxLayout(PendingPublishesForm)
        self.verticalLayout.setSpacing(-1)
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_frame = QtGui.QFrame(PendingPublishesForm)
        self.header_frame.setStyleSheet("#header_frame {\n"
"border-style: solid;\n"
"border-radius: 3;\n"
"border-width: 1;\n"
"border-color: rgb(32,32,32);\n"
"}")
        self.header_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(self.header_frame)
        self.label_3.setMinimumSize(QtCore.QSize(80, 80))
        self.label_3.setMaximumSize(QtCore.QSize(80, 80))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/res/p4_icon.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label = QtGui.QLabel(self.header_frame)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout.addWidget(self.header_frame)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.publishes_list = SnapshotListView(PendingPublishesForm)
        self.publishes_list.setStyleSheet("#snapshot_list {\n"
"background-color: rgb(255, 128, 0);\n"
"}")
        self.publishes_list.setObjectName("publishes_list")
        self.horizontalLayout.addWidget(self.publishes_list)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.publish_btn = QtGui.QPushButton(PendingPublishesForm)
        self.publish_btn.setObjectName("publish_btn")
        self.horizontalLayout_2.addWidget(self.publish_btn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.close_btn = QtGui.QPushButton(PendingPublishesForm)
        self.close_btn.setMinimumSize(QtCore.QSize(90, 0))
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_2.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(PendingPublishesForm)
        QtCore.QObject.connect(self.close_btn, QtCore.SIGNAL("clicked()"), PendingPublishesForm.close)
        QtCore.QMetaObject.connectSlotsByName(PendingPublishesForm)

    def retranslateUi(self, PendingPublishesForm):
        PendingPublishesForm.setWindowTitle(QtGui.QApplication.translate("PendingPublishesForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PendingPublishesForm", "The list below shows you all pending publishes in Perforce, allowing you to commit or cancel them as needed.", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_btn.setText(QtGui.QApplication.translate("PendingPublishesForm", "Publish Current Scene...", None, QtGui.QApplication.UnicodeUTF8))
        self.close_btn.setText(QtGui.QApplication.translate("PendingPublishesForm", "Close", None, QtGui.QApplication.UnicodeUTF8))

from ..snapshot_list_view import SnapshotListView
from . import resources_rc
