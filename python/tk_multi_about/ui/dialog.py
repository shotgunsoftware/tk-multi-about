# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(836, 487)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.context_overview_tab_widget = QtGui.QTabWidget(Dialog)
        self.context_overview_tab_widget.setTabPosition(QtGui.QTabWidget.South)
        self.context_overview_tab_widget.setObjectName("context_overview_tab_widget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.context_browser = ContextBrowserWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.context_browser.sizePolicy().hasHeightForWidth()
        )
        self.context_browser.setSizePolicy(sizePolicy)
        self.context_browser.setMinimumSize(QtCore.QSize(380, 0))
        self.context_browser.setObjectName("context_browser")
        self.verticalLayout_4.addWidget(self.context_browser)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/res/icon_task.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.context_overview_tab_widget.addTab(self.tab, icon, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.app_browser = AppBrowserWidget(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_browser.sizePolicy().hasHeightForWidth())
        self.app_browser.setSizePolicy(sizePolicy)
        self.app_browser.setMinimumSize(QtCore.QSize(380, 0))
        self.app_browser.setObjectName("app_browser")
        self.verticalLayout_2.addWidget(self.app_browser)
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/res/logo_color_16.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.context_overview_tab_widget.addTab(self.tab_2, icon1, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.environment_browser = EnvironmentBrowserWidget(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.environment_browser.sizePolicy().hasHeightForWidth()
        )
        self.environment_browser.setSizePolicy(sizePolicy)
        self.environment_browser.setMinimumSize(QtCore.QSize(380, 0))
        self.environment_browser.setObjectName("environment_browser")
        self.verticalLayout_3.addWidget(self.environment_browser)
        self.label_3 = QtGui.QLabel(self.tab_3)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/res/cog_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.context_overview_tab_widget.addTab(self.tab_3, icon2, "")
        self.horizontalLayout.addWidget(self.context_overview_tab_widget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/res/tank_logo.png"))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.jump_to_fs = QtGui.QPushButton(Dialog)
        self.jump_to_fs.setObjectName("jump_to_fs")
        self.verticalLayout.addWidget(self.jump_to_fs)
        self.reload_apps = QtGui.QPushButton(Dialog)
        self.reload_apps.setObjectName("reload_apps")
        self.verticalLayout.addWidget(self.reload_apps)
        self.support = QtGui.QPushButton(Dialog)
        self.support.setObjectName("support")
        self.verticalLayout.addWidget(self.support)
        spacerItem = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem)
        self.close = QtGui.QPushButton(Dialog)
        self.close.setObjectName("close")
        self.verticalLayout.addWidget(self.close)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.context_overview_tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QtGui.QApplication.translate(
                "Dialog",
                "The Current Sgtk Environment",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.label_4.setText(
            QtGui.QApplication.translate(
                "Dialog",
                "The above breakdown shows all the different Shotgun objects that together make up the Current Work Area. Clicking any of the items in the list will take you to that object inside of Shotgun.",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.context_overview_tab_widget.setTabText(
            self.context_overview_tab_widget.indexOf(self.tab),
            QtGui.QApplication.translate(
                "Dialog", "Current Context", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.label_2.setText(
            QtGui.QApplication.translate(
                "Dialog",
                "The list above shows all the different apps that are currently active. You can double click on an app to jump to its documentation.",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.context_overview_tab_widget.setTabText(
            self.context_overview_tab_widget.indexOf(self.tab_2),
            QtGui.QApplication.translate(
                "Dialog", "Active Apps", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.label_3.setText(
            QtGui.QApplication.translate(
                "Dialog",
                "The environment file contains all the settings and configuration for the currently running Shotgun Apps. The Engine provides core services such as menu management and app startup.",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.context_overview_tab_widget.setTabText(
            self.context_overview_tab_widget.indexOf(self.tab_3),
            QtGui.QApplication.translate(
                "Dialog", "Environment", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.jump_to_fs.setText(
            QtGui.QApplication.translate(
                "Dialog",
                "Jump to the File System",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.reload_apps.setText(
            QtGui.QApplication.translate(
                "Dialog", "Reload Engine and Apps", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.support.setText(
            QtGui.QApplication.translate(
                "Dialog",
                "Documentation and Support",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.close.setText(
            QtGui.QApplication.translate(
                "Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8
            )
        )


from ..context_browser import ContextBrowserWidget
from ..environment_browser import EnvironmentBrowserWidget
from ..app_browser import AppBrowserWidget
from . import resources_rc
