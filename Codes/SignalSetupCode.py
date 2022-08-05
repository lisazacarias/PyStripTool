# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyStripToolSignalSetUp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1087, 105)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.signal_setups_box)
        self.signal_check_box = QtWidgets.QCheckBox(self.signal_setups_box)
        self.horizontalLayout.addWidget(self.signal_check_box)
        self.signal_line_edit = QtWidgets.QLineEdit(self.signal_setups_box)
        self.horizontalLayout.addWidget(self.signal_line_edit)
        self.signal_y_axis_assignment_combo_box = QtWidgets.QComboBox(self.signal_setups_box)
        self.horizontalLayout.addWidget(self.signal_y_axis_assignment_combo_box)
        self.time_plot_assignment = QtWidgets.QComboBox(self.signal_setups_box)
        self.time_plot_assignment.addItems([str(i) for i in range(1,13)])
        self.horizontalLayout.addWidget(self.time_plot_assignment)
        self.color_slider = QtWidgets.QSlider(self.signal_setups_box)
        self.color_slider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalLayout.addWidget(self.color_slider)
        self.opacity_check_box = QtWidgets.QCheckBox(self.signal_setups_box)
        self.horizontalLayout.addWidget(self.opacity_check_box)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.signal_setups_box.setTitle(_translate("Form", "Signal Set Ups"))
        self.signal_y_axis_assignment_combo_box.setToolTip(_translate("Form", "Y-Axis"))
        self.signal_y_axis_assignment_combo_box.setItemText(0, _translate("Form", "Y-Axis Unit"))
        self.time_plot_assignment.setToolTip(_translate("Form", "Time Plot"))
        self.time_plot_assignment.setItemText(0, _translate("Form", "1"))
        self.time_plot_assignment.setItemText(1, _translate("Form", "2"))
        self.time_plot_assignment.setItemText(2, _translate("Form", "3"))
        self.time_plot_assignment.setItemText(3, _translate("Form", "4"))
        self.time_plot_assignment.setItemText(4, _translate("Form", "5"))
        self.time_plot_assignment.setItemText(5, _translate("Form", "6"))
        self.time_plot_assignment.setItemText(6, _translate("Form", "7"))
        self.time_plot_assignment.setItemText(7, _translate("Form", "8"))
        self.time_plot_assignment.setItemText(8, _translate("Form", "9"))
        self.time_plot_assignment.setItemText(9, _translate("Form", "10"))
        self.time_plot_assignment.setItemText(10, _translate("Form", "11"))
        self.time_plot_assignment.setItemText(11, _translate("Form", "12"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

