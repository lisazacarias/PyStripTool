# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyStripTool.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def __init__(self):
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.label = QtWidgets.QLabel(Form)
        self.time_plots_layout = QtWidgets.QGroupBox(Form)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.time_plots_layout)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.signal_manipulation_group_box = QtWidgets.QGroupBox(Form)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.signal_manipulation_group_box)
        self.signal_scroll_area = QtWidgets.QScrollArea(self.signal_manipulation_group_box)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.SignalLayout_2 = QtWidgets.QVBoxLayout()
        self.current_time_date = QtWidgets.QDateTimeEdit(Form)
        # self.signal_edit_tool_button = QtWidgets.QToolButton(Form)
        # self.signal_edit_add = QtWidgets.QMenu()
        # self.signal_edit_load = QtWidgets.QMenu()
        # self.signal_edit_save = QtWidgets.QMenu()
        # self.signal_edit_delete = QtWidgets.QMenu()
        # self.time_edit_tool_button = QtWidgets.QToolButton(Form)
        # self.time_edit_open_time_box = QtWidgets.QMenu()
        # self.time_plots_tool_button = QtWidgets.QToolButton(Form)
        # self.time_plots_number_plots = QtWidgets.QMenu()
        # self.time_plots_y_axis = QtWidgets.QMenu()
        self.menu_button = QtWidgets.QToolButton()
        self.menu = QtWidgets.QMenu()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1156, 376)

        self.gridLayout.setObjectName("gridLayout")

        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_plots_layout.sizePolicy().hasHeightForWidth())
        self.time_plots_layout.setSizePolicy(sizePolicy)
        self.time_plots_layout.setObjectName("time_plots_layout")

        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_5.addLayout(self.gridLayout_4)
        self.gridLayout.addWidget(self.time_plots_layout, 2, 0, 1, 4)

        self.signal_manipulation_group_box.setObjectName("signal_manipulation_group_box")

        self.gridLayout_2.setObjectName("gridLayout_2")

        self.signal_scroll_area.setWidgetResizable(True)
        self.signal_scroll_area.setObjectName("signal_scroll_area")

        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1100, 105))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout.setObjectName("verticalLayout")

        self.SignalLayout_2.setObjectName("SignalLayout_2")
        self.verticalLayout.addLayout(self.SignalLayout_2)
        self.signal_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.signal_scroll_area, 0, 0, 2, 1)
        self.gridLayout.addWidget(self.signal_manipulation_group_box, 3, 0, 3, 4)

        self.current_time_date.setReadOnly(True)
        self.current_time_date.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
        self.current_time_date.setCalendarPopup(True)
        self.current_time_date.setObjectName("current_time_date")
        self.gridLayout.addWidget(self.current_time_date, 1, 3, 1, 1)

        # self.signal_edit_tool_button.setObjectName("signal_edit_tool_button")
        # self.gridLayout.addWidget(self.signal_edit_tool_button, 0, 0, 1, 1)
        #
        # self.time_edit_tool_button.setObjectName("time_edit_tool_button")
        # self.gridLayout.addWidget(self.time_edit_tool_button, 0, 1, 1, 1)
        #
        # self.time_plots_tool_button.setObjectName("time_plots_tool_button")
        # self.gridLayout.addWidget(self.time_plots_tool_button, 0, 2, 1, 1)

        self.menu_button.setObjectName("menu_bar")
        self.gridLayout.addWidget(self.menu_button, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # def signal_edit_submenu(self, k, v):
    #     return lambda: self.signal_edit_tool_button.setText('{0}_{1}'.format(k, v))
    #
    # def time_edit_submenu(self, k, v):
    #     return lambda: self.time_edit_tool_button.setText('{0}_{1}'.format(k, v))
    #
    # def time_plots_submenu(self, k, v):
    #     return lambda: self.time_plots_tool_button.setText('{0}_{1}'.format(k, v))

    def menu_callback(self, k, v):
        return lambda: self.menu_button.setText('{0}_{1}.format(k,v)')

    def set_menu(self):
        menu_dic = {'Signal Edit': ["Add", "Load", "Save", "Delete"],
                    'Time Edit': ["Open Time Box"],
                    'Time Plots': ["Time Plot Number", "Y Axis"]}
        for k, vals in menu_dic.items():
            sub_menu = self.menu.addMenu(k)
            for v in vals:
                action = sub_menu.addAction(str(v))
                action.triggered.connect(self.menu_callback(k, v))
        self.menu_button.setMenu(self.menu)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Signal Viewer"))
        self.time_plots_layout.setTitle(_translate("Form", "Time Plots"))
        self.signal_manipulation_group_box.setTitle(_translate("Form", "Signal"))
        self.current_time_date.setToolTip(_translate("Form", "Current time"))
        self.current_time_date.setDisplayFormat(_translate("Form", "M/d/yyyy h:mm AP"))
        # self.signal_edit_tool_button.setText(_translate("Form", "Signal Edit"))
        # self.time_edit_tool_button.setText(_translate("Form", "Time Edit"))
        # self.time_plots_tool_button.setText(_translate("Form", "Time Plots"))
        self.menu_button.setText(_translate("Form", "Menu Bar"))


# # class MenuBar(object):
# #     def __init__(self):
# #         self.menu_button = QtWidgets.QToolButton()
# #         self.menu = QtWidgets.QMenu()
# #
# #     def menu_callback(self, k, v):
# #         return lambda: self.menu_button.setText('{0}_{1}.format(k,v)')
# #
# #     def set_menu(self):
# #         menu_dic = {'Signal Edit': ["Add", "Load", "Save", "Delete"],
# #                     'Time Edit': ["Open Time Box"],
# #                     'Time Plots': ["Time Plot Number", "Y Axis"]}
# #         for k, vals in menu_dic.items():
# #             sub_menu = self.menu.addMenu(k)
# #             for v in vals:
# #                 action = sub_menu.addAction(str(v))
# #                 action.triggered.connect(self.menu_callback(k, v))
# #         self.menu_button.setMenu(self.menu)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
