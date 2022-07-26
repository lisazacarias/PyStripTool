import time
import json
import sys
import warnings
from qtpy import QtCore
from os import path
from typing import Optional
from pydm import Display
from qtpy.QtWidgets import (QAction, QApplication, QButtonGroup,
                            QCheckBox, QComboBox, QDateTimeEdit, QFrame,
                            QGridLayout, QGroupBox, QHBoxLayout,
                            QHeaderView, QLabel, QLineEdit, QPushButton,
                            QScrollArea, QSlider, QSpinBox, QTimeEdit,
                            QVBoxLayout, QWidget)
from pydm.widgets import PyDMEmbeddedDisplay
from pydm.widgets import PyDMTimePlot
from pydm.widgets import PyDMByteIndicator
from pydm.utilities import connection
from scipy.ndimage import maximum_position
# from lcls_tools.common.pydm_tools.pydmPlotUtil import (TimePlotParams,
                                                       # TimePlotUpdater)
# from lcls_tools.superconducting.scLinac import ALL_CRYOMODULES
# import plot_utils
# from plot_linac import Decarad, PLOT_CRYO_DICT, PlotCryomodule

warnings.filterwarnings("ignore", category=RuntimeWarning)


class PyStripTool(Display):

    def ui_filename(self):
        # Point to our UI file
        return 'PyStripToolALt.ui'

    def __init__(self, parent=None, args=None):
        super().__init__(parent=parent, args=args)

        self.pathHere = path.dirname(sys.modules[self.__module__].__file__)

        # self.current_line: Optional[PlotCryomodule] = None
        # self.ui.cryo_combobox.addItems(["None"] + ALL_CRYOMODULES)
        # self.ui.cryo_combobox.currentIndexChanged.connect(self.update_cryomodule)
        self.time_plot_updater: TimePlotUpdater = None
        self.setup_plots()

        self.ui.timespan_spinbox.editingFinished.connect(self.update_plot_timespan)
        self.current_line: Optional[y_axis] = None

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

    # def update_plot_lines(self):
        # try:
            # self.current_line = PLOT_LINE_DICT[self.ui.signal_line_edit.currentText()]

            # timeplot_update_map = {plot_utils.ONE: self.current_line.one,
            #                        plot_utils.TWO: self.current_line.two,
            #                        plot_utils.THREE: self.current_line.three,
            #                        plot_utils.FOUR: self.current_line.four,
            #                        plot_utils.FIVE: self.current_line.five,
            #                        plot_utils.SIX: self.current_line.six,
            #                        plot_utils.SEVEN: self.current_line.seven,
            #                        plot_utils.EIGHT: self.current_line.eight,
            #                        plot_utils.NINE: self.current_line.nine,
            #                        plot_utils.TEN: self.current_line.ten,
            #                        plot_utils.ELEVEN: self.current_line.eleven,
            #                        plot_utils.TWELVE: self.current_line.twelve}

            # self.time_plot_updater.updatePlots(timeplot_update_map)
        # except KeyError:
        #     self.time_plot_updater.clear_plots()

    def update_y_axis(self):
        try:
            self.current_line = TIMEPLOTS_YAXIS_DICT[self.ui.signal_y_axis_assignment_combo_box.currentText()]

            timeplot_update = {plot_utils.timeplot_number: self.current_line.y_axis}
            self.time_plot_updater.updatePlots(timeplot_update)
        except KeyError:
            self.time_plot_updater.clear_plots()

    # def setup_plots(self):
    #     time_plot_updater = {
    #         plot_utils.ONE: TimePlotParams(plot=self.ui.plot_steppertemps,
    #                                        formLayout=self.ui.stepper_form),
    #         plot_utils.TWO: TimePlotParams(plot=self.ui.plot_homus_temp,
    #                                        formLayout=self.ui.up_hom_form),
    #         plot_utils.THREE: TimePlotParams(plot=self.ui.plot_homds_temp,
    #                                          formLayout=self.ui.down_hom_form),
    #         plot_utils.FOUR: TimePlotParams(plot=self.ui.plot_couplertop_temp,
    #                                         formLayout=self.ui.coup_top_form),
    #         plot_utils.FIVE: TimePlotParams(plot=self.ui.plot_couplerbot_temp,
    #                                         formLayout=self.ui.coup_bot_hom),
    #         plot_utils.SIX: TimePlotParams(plot=self.ui.plot_cmvacuum,
    #                                        formLayout=self.ui.vacuum_form),
    #         plot_utils.SEVEN: TimePlotParams(plot=self.ui.plot_cryosignals,
    #                                          formLayout=self.ui.cryo_form),
    #         plot_utils.EIGHT: TimePlotParams(plot=self.ui.plot_decarad,
    #                                          formLayout=self.ui.decarad_form),
    #         plot_utils.NINE: TimePlotParams(plot=self.ui.plot_amps,
    #                                         formLayout=self.ui.amp_form),
    #         plot_utils.TEN: TimePlotParams(plot=self.ui.plot_cmvacuum,
    #                                        formLayout=self.ui.vacuum_form),
    #         plot_utils.ELEVEN: TimePlotParams(plot=self.ui.plot_cryosignals,
    #                                           formLayout=self.ui.cryo_form),
    #         plot_utils.TWELVE: TimePlotParams(plot=self.ui.plot_decarad,
    #                                           formLayout=self.ui.decarad_form),
    #     }
    #     self.time_plot_updater = TimePlotUpdater(time_plot_updater)

    def ui_filepath(self):
        # Return the full path to the UI file
        return path.join(path.dirname(path.realpath(__file__)), self.ui_filename())

    def get_path(self, file_name):
        return path.join(self.pathHere, file_name)

    def time_manipulation(self):
        self.ui.action_open_time_manipulation_box.clicked.connect(self.time_popup)
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

    def signal_manipulation(self):
        # Connect the add/load/save/delete buttons to the signal setup area.
        self.ui.action_add.clicked.connect(self.signal_setups())
        self.ui.action_load.clicked.connect(self.load_popup())
        self.ui.action_save.clicked.connect(self.signal_setups())
        self.ui.actiop_delete.clicked.connect(self.signal_setups())


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