# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyStripToolLoadPopUp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1081, 313)
        self.load_configurations_setup = QtWidgets.QGroupBox(Dialog)
        self.load_configurations_setup.setGeometry(QtCore.QRect(10, 10, 1061, 287))
        self.load_configurations_setup.setObjectName("load_configurations_setup")
        self.gridLayout = QtWidgets.QGridLayout(self.load_configurations_setup)
        self.gridLayout.setObjectName("gridLayout")
        self.delete_configuration_button = QtWidgets.QPushButton(self.load_configurations_setup)
        self.delete_configuration_button.setObjectName("delete_configuration_button")
        self.gridLayout.addWidget(self.delete_configuration_button, 1, 2, 1, 1)
        self.create_configuration_button = QtWidgets.QPushButton(self.load_configurations_setup)
        self.create_configuration_button.setObjectName("create_configuration_button")
        self.gridLayout.addWidget(self.create_configuration_button, 1, 1, 1, 1)
        self.load_configuration_button = QtWidgets.QPushButton(self.load_configurations_setup)
        self.load_configuration_button.setObjectName("load_configuration_button")
        self.gridLayout.addWidget(self.load_configuration_button, 1, 0, 1, 1)
        self.load_configuration_scroll_area = QtWidgets.QScrollArea(self.load_configurations_setup)
        self.load_configuration_scroll_area.setWidgetResizable(True)
        self.load_configuration_scroll_area.setObjectName("load_configuration_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1031, 195))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.load_configuration_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.load_configuration_scroll_area, 0, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.load_configurations_setup.setTitle(_translate("Dialog", "Load Configurations Set Up"))
        self.delete_configuration_button.setText(_translate("Dialog", "Delete"))
        self.create_configuration_button.setText(_translate("Dialog", "New"))
        self.load_configuration_button.setText(_translate("Dialog", "Load"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

