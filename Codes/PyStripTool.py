import sys
import warnings
from functools import partial
from os import path
from typing import Optional

# from lcls_tools.common.pydm_tools.displayUtils import showDisplay
# from lcls_tools.common.pydm_tools.pydmPlotUtil import (TimePlotUpdater)
from PyQt5.QtCore import pyqtSlot
from pydm import Display
from qtpy import QtCore
from qtpy.QtWidgets import (QCheckBox, QComboBox, QHBoxLayout,
                            QLineEdit, QSlider)

warnings.filterwarnings("ignore", category=RuntimeWarning)


class PyStripTool(Display):
    
    def ui_filename(self):
        # Point to our UI file
        return 'PyStripTool.ui'
    
    def __init__(self, parent=None, args=None):
        super().__init__(parent=parent, args=args)
        
        self.pathHere = path.dirname(sys.modules[self.__module__].__file__)
        
        self.setup_plots()
        
        self.ui.timespan_spinbox.editingFinished.connect(self.update_plot_timespan)
        self.current_line: Optional[str] = None
        
        self.time_combo_boxes = [self.ui.years_selector,
                                 self.ui.months_selector,
                                 self.ui.days_selector,
                                 self.ui.hours_selector,
                                 self.ui.minutes_selector]
        self.signal_setups_check_boxes = [self.ui.signal_checkbox, self.ui.opacity_checkbox]
        
        self.load_popup = Display(ui_filename="PyStripToolLoadPopUp.ui")
        self.time_popup = Display(ui_filename="PyStripToolTimeManip.ui")
    
    def update_plot_timespan(self):
        # Update the time span.
        self.time_plot_updater.updateTimespans(self.ui.timespan_spinbox.value())
    
    def ui_filepath(self):
        # Return the full path to the UI file
        return path.join(path.dirname(path.realpath(__file__)), self.ui_filename())
    
    def get_path(self, file_name):
        return path.join(self.pathHere, file_name)
    
    def time_manipulation(self):
        self.ui.action_open_time_manipulation_box.clicked.connect(partial(showDisplay, self.time_popup))
        # Connect year/month/day/hour/minute combo boxes to the time span of the plots.
        for combo_box in self.time_combo_boxes:
            combo_box.clicked.connect(self.update_plot_timespan)
            # self.ui.timespan_spinbox.editingFinished.connect(self.update_plot_timespan)
            # Connect the start time spin box to the time span of the plots.
            self.start_time_select.clicked.connect(self.update_plot_timespan)
            # Connect the live view button and indicator to the plots.
            self.ui.pause_play_button.clicked.connect(self.time_plot_updater)
            self.ui.pause_play_button.clicked.connect(self.ui.pause_play_indicator)
    
    def signal_setups(self):
        """Build signal setups."""
        signal_setups = QHBoxLayout()
        
        signal_check_box = QCheckBox()
        signal_setups.addWidget(signal_check_box)
        
        signal_line_edit = QLineEdit()
        signal_setups.addWidget(signal_line_edit)
        
        signal_y_axis_assignment_combo_box = QComboBox()
        signal_setups.addWidget(signal_y_axis_assignment_combo_box)
        
        color_slider = QSlider()
        color_slider.setOrientation(QtCore.Qt.Horizontal)
        signal_setups.addWidget(color_slider)
        
        opacity_check_box = QCheckBox()
        signal_setups.addWidget(opacity_check_box)
        
        self.ui.SignalLayout_2.addLayout(signal_setups)
        
        # Line edit
        self.ui.signal_line_edit.returnPressed.connect(self.data)
        # Signal checkbox
        self.ui.signal_checkbox.checked.connect(self.ui.signal_line_edit)
        self.ui.signal_checkbox.checked.connect(self.time_plot_updater)
        # Color slider
        self.ui.color_slider.SliderMove.connect(self.ui.signal_line_edit)
        self.ui.color_slider.SliderMove.connect(self.time_plot_updater)
        # Opacity checkbox
        self.ui.opacity_checkbox.checked.connect(self.ui.signal_line_edit)
        self.ui.opacity_checkbox.checked.connect(self.time_plot_updater)
    
    @pyqtSlot
    def signal_manipulation(self):
        # Connect the add/load/save/delete buttons to the signal setup area.
        self.ui.action_add.clicked.connect(self.signal_setups)
        self.ui.action_load.clicked.connect(partial(showDisplay, self.load_popup))
        self.ui.action_save.clicked.connect(self.signal_setups)
        self.ui.actiop_delete.clicked.connect(self.signal_setups)


# class MenuBar(object):
#     def __init__(self):
#         self.menu_button = QtWidgets.QToolButton()
#         self.menu = QtWidgets.QMenu()
#
#     def menu_callback(self, k, v):
#         return lambda: self.menu_button.setText('{0}_{1}.format(k,v)')
#
#     def set_menu(self):
#         menu_dic = {'Signal Edit': ["Add", "Load", "Save", "Delete"],
#                     'Time Edit': ["Open Time Box"],
#                     'Time Plots': ["Time Plot Number", "Y Axis"]}
#         for k, vals in menu_dic.items():
#             sub_menu = self.menu.addMenu(k)
#             for v in vals:
#                 action = sub_menu.addAction(str(v))
#                 action.triggered.connect(self.menu_callback(k, v))
#         self.menu_button.setMenu(self.menu)


"""
---Example pool---

class PyStripTool(Display):

    def __init__(self, parent=None, args=None):
        super(PyStripTool, self).__init__(parent=parent, args=args)
        # Placeholder for data to filter
        self.data = []
        # Reference to the PyDMApplication
        self.app = QApplication.instance()
        # Load data from file
        self.load_data()
        # Assemble the Widgets
        self.setup_ui()

    def minimum_size_hint(self):
        # This is the default recommended size for this screen
        return QtCore.QSize(750, 120)
        
    def get_dimensions(options):
    num_options = len(options.keys())
    row_count = int(np.sqrt(num_options))
    col_count = int(np.ceil(np.sqrt(num_options)))
    if row_count * col_count != num_options:
        col_count += 1
    return col_count
"""
