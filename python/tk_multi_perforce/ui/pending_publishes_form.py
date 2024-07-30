# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pending_publishes_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from tank.platform.qt import QtCore
for name, cls in QtCore.__dict__.items():
    if isinstance(cls, type): globals()[name] = cls

from tank.platform.qt import QtGui
for name, cls in QtGui.__dict__.items():
    if isinstance(cls, type): globals()[name] = cls


from ..snapshot_list_view import SnapshotListView

from  . import resources_rc

class Ui_PendingPublishesForm(object):
    def setupUi(self, PendingPublishesForm):
        if not PendingPublishesForm.objectName():
            PendingPublishesForm.setObjectName(u"PendingPublishesForm")
        PendingPublishesForm.resize(783, 609)
        self.verticalLayout = QVBoxLayout(PendingPublishesForm)
        self.verticalLayout.setSpacing(-1)
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_frame = QFrame(PendingPublishesForm)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"#header_frame {\n"
"border-style: solid;\n"
"border-radius: 3;\n"
"border-width: 1;\n"
"border-color: rgb(32,32,32);\n"
"}")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.header_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 80))
        self.label_3.setMaximumSize(QSize(80, 80))
        self.label_3.setPixmap(QPixmap(u":/res/p4_icon.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label = QLabel(self.header_frame)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.verticalLayout.addWidget(self.header_frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.publishes_list = SnapshotListView(PendingPublishesForm)
        self.publishes_list.setObjectName(u"publishes_list")
        self.publishes_list.setStyleSheet(u"#snapshot_list {\n"
"background-color: rgb(255, 128, 0);\n"
"}")

        self.horizontalLayout.addWidget(self.publishes_list)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.publish_btn = QPushButton(PendingPublishesForm)
        self.publish_btn.setObjectName(u"publish_btn")

        self.horizontalLayout_2.addWidget(self.publish_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(PendingPublishesForm)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_2.addWidget(self.close_btn)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(PendingPublishesForm)
        self.close_btn.clicked.connect(PendingPublishesForm.close)

        QMetaObject.connectSlotsByName(PendingPublishesForm)
    # setupUi

    def retranslateUi(self, PendingPublishesForm):
        PendingPublishesForm.setWindowTitle(QCoreApplication.translate("PendingPublishesForm", u"Form", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("PendingPublishesForm", u"The list below shows you all pending publishes in Perforce, allowing you to commit or cancel them as needed.", None))
        self.publish_btn.setText(QCoreApplication.translate("PendingPublishesForm", u"Publish Current Scene...", None))
        self.close_btn.setText(QCoreApplication.translate("PendingPublishesForm", u"Close", None))
    # retranslateUi
