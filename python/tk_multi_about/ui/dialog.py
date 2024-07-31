# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
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


from ..context_browser import ContextBrowserWidget
from ..app_browser import AppBrowserWidget
from ..environment_browser import EnvironmentBrowserWidget

from  . import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(836, 487)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.context_overview_tab_widget = QTabWidget(Dialog)
        self.context_overview_tab_widget.setObjectName(u"context_overview_tab_widget")
        self.context_overview_tab_widget.setTabPosition(QTabWidget.South)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.context_browser = ContextBrowserWidget(self.tab)
        self.context_browser.setObjectName(u"context_browser")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.context_browser.sizePolicy().hasHeightForWidth())
        self.context_browser.setSizePolicy(sizePolicy)
        self.context_browser.setMinimumSize(QSize(380, 0))

        self.verticalLayout_4.addWidget(self.context_browser)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_4)

        icon = QIcon()
        icon.addFile(u":/res/icon_task.png", QSize(), QIcon.Normal, QIcon.Off)
        self.context_overview_tab_widget.addTab(self.tab, icon, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.app_browser = AppBrowserWidget(self.tab_2)
        self.app_browser.setObjectName(u"app_browser")
        sizePolicy.setHeightForWidth(self.app_browser.sizePolicy().hasHeightForWidth())
        self.app_browser.setSizePolicy(sizePolicy)
        self.app_browser.setMinimumSize(QSize(380, 0))

        self.verticalLayout_2.addWidget(self.app_browser)

        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_2)

        icon1 = QIcon()
        icon1.addFile(u":/res/logo_color_16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.context_overview_tab_widget.addTab(self.tab_2, icon1, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_3 = QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.environment_browser = EnvironmentBrowserWidget(self.tab_3)
        self.environment_browser.setObjectName(u"environment_browser")
        sizePolicy.setHeightForWidth(self.environment_browser.sizePolicy().hasHeightForWidth())
        self.environment_browser.setSizePolicy(sizePolicy)
        self.environment_browser.setMinimumSize(QSize(380, 0))

        self.verticalLayout_3.addWidget(self.environment_browser)

        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_3)

        icon2 = QIcon()
        icon2.addFile(u":/res/cog_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.context_overview_tab_widget.addTab(self.tab_3, icon2, "")

        self.horizontalLayout.addWidget(self.context_overview_tab_widget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/res/tank_logo.png"))

        self.verticalLayout.addWidget(self.label)

        self.jump_to_fs = QPushButton(Dialog)
        self.jump_to_fs.setObjectName(u"jump_to_fs")

        self.verticalLayout.addWidget(self.jump_to_fs)

        self.reload_apps = QPushButton(Dialog)
        self.reload_apps.setObjectName(u"reload_apps")

        self.verticalLayout.addWidget(self.reload_apps)

        self.support = QPushButton(Dialog)
        self.support.setObjectName(u"support")

        self.verticalLayout.addWidget(self.support)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.close = QPushButton(Dialog)
        self.close.setObjectName(u"close")

        self.verticalLayout.addWidget(self.close)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)

        self.context_overview_tab_widget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"The Current Sgtk Environment", None))
#if QT_CONFIG(accessibility)
        self.context_browser.setAccessibleName(QCoreApplication.translate("Dialog", u"context_browser", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.context_browser.setAccessibleDescription(QCoreApplication.translate("Dialog", u"context_browser", None))
#endif // QT_CONFIG(accessibility)
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Current Context lists all Flow Production Tracking objects that together make up the Current Work Area. Double-click an item to access the object in Flow Production Tracking.", None))
        self.context_overview_tab_widget.setTabText(self.context_overview_tab_widget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Current Context", None))
#if QT_CONFIG(accessibility)
        self.app_browser.setAccessibleName(QCoreApplication.translate("Dialog", u"app_browser", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.app_browser.setAccessibleDescription(QCoreApplication.translate("Dialog", u"app_browser", None))
#endif // QT_CONFIG(accessibility)
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Active Apps lists all currently active apps. Double-click an app to jump to its documentation.", None))
        self.context_overview_tab_widget.setTabText(self.context_overview_tab_widget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Active Apps", None))
#if QT_CONFIG(accessibility)
        self.environment_browser.setAccessibleName(QCoreApplication.translate("Dialog", u"environment_browser", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.environment_browser.setAccessibleDescription(QCoreApplication.translate("Dialog", u"environment_browser", None))
#endif // QT_CONFIG(accessibility)
        self.label_3.setText(QCoreApplication.translate("Dialog", u"The Environment file contains all settings and configurations for currently running Flow Production Tracking apps. The Engine provides core services, such as menu management and app startup.", None))
        self.context_overview_tab_widget.setTabText(self.context_overview_tab_widget.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"Environment", None))
        self.label.setText("")
        self.jump_to_fs.setText(QCoreApplication.translate("Dialog", u"Jump to the File System", None))
        self.reload_apps.setText(QCoreApplication.translate("Dialog", u"Reload Engine and Apps", None))
        self.support.setText(QCoreApplication.translate("Dialog", u"Documentation and Support", None))
        self.close.setText(QCoreApplication.translate("Dialog", u"Close", None))
    # retranslateUi
