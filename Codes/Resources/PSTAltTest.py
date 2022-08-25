# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyStripToolAlt.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

# import LoadPopUpCode
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog


class Ui_MainWindow(object):

    def __init__(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.signal_manipulation_group_box = QtWidgets.QGroupBox(self.centralwidget)
        self.gridLayout_6 = QtWidgets.QGridLayout(self.signal_manipulation_group_box)
        self.signal_scroll_area_2 = QtWidgets.QScrollArea(self.signal_manipulation_group_box)
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.SignalLayout_3 = QtWidgets.QVBoxLayout()
        self.time_plots_layout = QtWidgets.QGroupBox(self.centralwidget)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.time_plots_layout)
        self.grid_layout_for_plots = QtWidgets.QGridLayout()
        self.current_time_date = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menu_signal_edit = QtWidgets.QMenu(self.menubar)
        self.menu_time_plots = QtWidgets.QMenu(self.menubar)
        self.menu_number_of_plots = QtWidgets.QMenu(self.menu_time_plots)
        self.menu_y_axis = QtWidgets.QMenu(self.menu_time_plots)
        self.menu_time_edit = QtWidgets.QMenu(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.action_add = QtWidgets.QAction(MainWindow)
        self.action_load = QtWidgets.QAction(MainWindow)
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_delete = QtWidgets.QAction(MainWindow)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action4 = QtWidgets.QAction(MainWindow)
        self.action5 = QtWidgets.QAction(MainWindow)
        self.action6 = QtWidgets.QAction(MainWindow)
        self.action7 = QtWidgets.QAction(MainWindow)
        self.action8 = QtWidgets.QAction(MainWindow)
        self.action9 = QtWidgets.QAction(MainWindow)
        self.action10 = QtWidgets.QAction(MainWindow)
        self.action11 = QtWidgets.QAction(MainWindow)
        self.action12 = QtWidgets.QAction(MainWindow)
        self.action_add_y_axis = QtWidgets.QAction(MainWindow)
        self.action_open_time_manipulation_box = QtWidgets.QAction(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1191, 408)

        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout.setObjectName("gridLayout")

        self.signal_manipulation_group_box.setObjectName("signal_manipulation_group_box")

        self.gridLayout_6.setObjectName("gridLayout_6")

        self.signal_scroll_area_2.setWidgetResizable(True)
        self.signal_scroll_area_2.setObjectName("signal_scroll_area_2")

        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1135, 105))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.SignalLayout_3.setObjectName("SignalLayout_3")
        self.verticalLayout_2.addLayout(self.SignalLayout_3)
        self.signal_scroll_area_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_6.addWidget(self.signal_scroll_area_2, 0, 0, 2, 1)
        self.gridLayout.addWidget(self.signal_manipulation_group_box, 2, 0, 1, 2)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_plots_layout.sizePolicy().hasHeightForWidth())
        self.time_plots_layout.setSizePolicy(sizePolicy)
        self.time_plots_layout.setObjectName("time_plots_layout")

        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.grid_layout_for_plots.setObjectName("grid_layout_for_plots")
        self.verticalLayout_6.addLayout(self.grid_layout_for_plots)
        self.gridLayout.addWidget(self.time_plots_layout, 1, 0, 1, 2)

        self.current_time_date.setReadOnly(True)
        self.current_time_date.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
        self.current_time_date.setCalendarPopup(True)
        self.current_time_date.setObjectName("current_time_date")
        self.gridLayout.addWidget(self.current_time_date, 0, 1, 1, 1)

        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 1191, 31))
        self.menubar.setObjectName("menubar")

        self.menu_signal_edit.setObjectName("menu_signal_edit")

        self.menu_time_plots.setObjectName("menu_time_plots")

        self.menu_number_of_plots.setObjectName("menu_number_of_plots")

        self.menu_y_axis.setObjectName("menu_y_axis")

        self.menu_time_edit.setObjectName("menu_time_edit")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.action_add.setObjectName("action_add")

        self.action_load.setObjectName("action_load")

        self.action_save.setObjectName("action_save")

        self.action_delete.setObjectName("action_delete")

        self.action1.setObjectName("action1")

        self.action2.setObjectName("action2")

        self.action3.setObjectName("action3")

        self.action4.setObjectName("action4")

        self.action5.setObjectName("action5")

        self.action6.setObjectName("action6")

        self.action7.setObjectName("action7")

        self.action8.setObjectName("action8")

        self.action9.setObjectName("action9")

        self.action10.setObjectName("action10")

        self.action11.setObjectName("action11")

        self.action12.setObjectName("action12")

        self.action_add_y_axis.setObjectName("action_add_y_axis")

        self.action_open_time_manipulation_box.setObjectName("action_open_time_manipulation_box")
        self.menu_signal_edit.addAction(self.action_add)

        self.menu_signal_edit.addAction(self.action_load)
        self.action_load.triggered.connect(self.show_load_popup)
        # self.action_load.triggered.connect(self.run_LoadPopUpCode)
        # self.action_load.triggered(LoadPopUpCode.Dialog.show())

        self.menu_signal_edit.addAction(self.action_save)
        self.menu_signal_edit.addAction(self.action_delete)
        self.menu_number_of_plots.addAction(self.action1)
        self.menu_number_of_plots.addAction(self.action2)
        self.menu_number_of_plots.addAction(self.action3)
        self.menu_number_of_plots.addAction(self.action4)
        self.menu_number_of_plots.addAction(self.action5)
        self.menu_number_of_plots.addAction(self.action6)
        self.menu_number_of_plots.addAction(self.action7)
        self.menu_number_of_plots.addAction(self.action8)
        self.menu_number_of_plots.addAction(self.action9)
        self.menu_number_of_plots.addAction(self.action10)
        self.menu_number_of_plots.addAction(self.action11)
        self.menu_number_of_plots.addAction(self.action12)
        self.menu_y_axis.addAction(self.action_add_y_axis)
        self.menu_time_plots.addAction(self.menu_number_of_plots.menuAction())
        self.menu_time_plots.addAction(self.menu_y_axis.menuAction())
        self.menu_time_edit.addAction(self.action_open_time_manipulation_box)
        self.menubar.addAction(self.menu_signal_edit.menuAction())
        self.menubar.addAction(self.menu_time_edit.menuAction())
        self.menubar.addAction(self.menu_time_plots.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.signal_manipulation_group_box.setTitle(_translate("MainWindow", "Signal"))
        self.time_plots_layout.setTitle(_translate("MainWindow", "Time Plots"))
        self.current_time_date.setToolTip(_translate("MainWindow", "Current time"))
        self.current_time_date.setDisplayFormat(_translate("MainWindow", "M/d/yyyy h:mm AP"))
        self.label.setText(_translate("MainWindow", "Signal Viewer"))
        self.menu_signal_edit.setTitle(_translate("MainWindow", "Signal Edit"))
        self.menu_time_plots.setTitle(_translate("MainWindow", "Time Plots"))
        self.menu_number_of_plots.setTitle(_translate("MainWindow", "Number of plots"))
        self.menu_y_axis.setTitle(_translate("MainWindow", "Y-Axis"))
        self.menu_time_edit.setTitle(_translate("MainWindow", "Time Edit"))
        self.action_add.setText(_translate("MainWindow", "Add"))
        self.action_add.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.action_load.setText(_translate("MainWindow", "Load"))
        self.action_load.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.action_save.setText(_translate("MainWindow", "Save"))
        self.action_save.setToolTip(_translate("MainWindow", "Save current setup"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_delete.setText(_translate("MainWindow", "Delete"))
        self.action_delete.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.action1.setText(_translate("MainWindow", "1"))
        self.action2.setText(_translate("MainWindow", "2"))
        self.action3.setText(_translate("MainWindow", "3"))
        self.action4.setText(_translate("MainWindow", "4"))
        self.action5.setText(_translate("MainWindow", "5"))
        self.action6.setText(_translate("MainWindow", "6"))
        self.action7.setText(_translate("MainWindow", "7"))
        self.action8.setText(_translate("MainWindow", "8"))
        self.action9.setText(_translate("MainWindow", "9"))
        self.action10.setText(_translate("MainWindow", "10"))
        self.action11.setText(_translate("MainWindow", "11"))
        self.action12.setText(_translate("MainWindow", "12"))
        self.action_add_y_axis.setText(_translate("MainWindow", "Add"))
        self.action_open_time_manipulation_box.setText(_translate("MainWindow", "Open Time Manipulation Box"))

    def show_load_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Load configurations.")
        msg.setText("Load menu placeholder.")
        msg.setStandardButtons(QMessageBox.Open | QMessageBox.Save | QMessageBox.Discard)
        # msg.connect(ui_filename="LoadPopUpCode.py")
        # msg.open(LoadPopUpCode)
        # LoadPopUpCode.show_load_popup()

        x = msg.exec_()


# class ActionTrig(object):
#     def __init__(self):
#         self.run_LoadPopUpCode = QtWidgets.QDialog()
#
    # def run_LoadPopUpCode(self):
    #     self.run_LoadPopUpCode.LoadPopUpCode.Dialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
