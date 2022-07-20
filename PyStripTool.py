import time
import json
from qtpy import QtCore
from os import path
from pydm import Display
from qtpy.QtWidgets import (QVBoxLayout, QHBoxLayout, QGroupBox,
                            QLabel, QLineEdit, QPushButton, QScrollArea, QFrame,
                            QApplication, QWidget, QSlider, QCheckBox, QSpinBox, QTimeEdit, QComboBox)
from pydm.widgets import PyDMEmbeddedDisplay
from pydm.widgets import PyDMTimePlot
from pydm.widgets import PyDMByteIndicator
from pydm.utilities import connection
from scipy.ndimage.measurements import maximum_position


class PyStripTool(Display):

    def __init__(self, parent=None, args=None):
        super(PyStripTool, self).__init__(parent=parent, args=args)

        self.pathHere = path.dirname(sys.modules[self.__module__].__file__)

        self.current_cm: Optional[PlotCryomodule] = None
        self.ui.cryo_combobox.addItems(["None"] + ALL_CRYOMODULES)
        self.ui.cryo_combobox.currentIndexChanged.connect(self.update_cryomodule)
        self.time_plot_updater: TimePlotUpdater = None
        self.setup_plots()

        self.ui.timespan_spinbox.editingFinished.connect(self.update_plot_timespan)

        self.time_combo_boxes = [self.ui.years_selector, self.ui.months_selector,
                                 self.ui.days_selector, self.ui.hours_selector,
                                 self.ui.minutes_selector]
        self.signal_setups_check_boxes = [self.ui.signal_checkbox, self.ui.opacity_checkbox]

    def ui_filename(self):
        # Point to our UI file
        return 'PyStripTool.ui'

    def y_axis_set_up(self):
        self.ui.y_axis_line_edit.returnPressed.connect(self.data)
        self.ui.y_axis_line_edit.returnPressed.connect(self.y_axis)
        self.ui.delete_y_axis_unit_button.clicked.connect(self.y_axis)

    def y_axis_manipulator(self):
        self.ui.add_y_axis.clicked.connect(self.y_axis_set_up())
        self.ui.add_y_axis.clicked.connect(self.ui.y_axis_scroll_area)

    def time_manipulation(self):
        for combo_box in self.time_combo_boxes:
            combo_box.clicked.connect(self.time_span)
            self.start_time_select.clicked.connect(self.time_span)
            self.ui.pause_play_button.clicked.connect(self.update_plot)
            self.ui.pause_play_button.clicked.connect(self.ui.pause_play_indicator)

    def update_plot_timespan(self):
        self.time_plot_updater.updateTimespans(self.ui.timespan_spinbox.value())

    def signal_setups(self):
        # Y-Axis Assignment combo box
        self.ui.signal_y_axis_assignment_combo_box = {"1": y_axis(1), "2": y_axis(2)}

        self.ui.signal_y_axis_assignment_combo_box = None

        # Line edit
        self.ui.signal_line_edit.returnPressed.connect(self.data)
        # Signal checkbox
        self.ui.signal_checkbox.checked.connect(self.ui.signal_line_edit)
        self.ui.signal_checkbox.checked.connect(self.update_plot)
        # Color slider
        self.ui.color_slider.SliderMove.connect(self.ui.signal_line_edit)
        self.ui.color_slider.SliderMove.connect(self.update_plot)
        # Opacity checkbox
        self.ui.opacity_checkbox.checked.connect(self.ui.signal_line_edit)
        self.ui.opacity_checkbox.checked.connect(self.update_plot)

    def signal_manipulation(self):
        self.ui.add_signal_setups.clicked.connect(self.signal_setups())
        self.ui.load_configuration.clicked.connect(self.signal_setups())
        self.ui.save_configuration.clicked.connect(self.signal_setups())
        self.ui.delete_signal_setups.clicked.connect(self.signal_setups())


"""
---Example pool---
import time
import json
from qtpy import QtCore
from os import path
from pydm import Display
from qtpy.QtWidgets import (QVBoxLayout, QHBoxLayout, QGroupBox,
                            QLabel, QLineEdit, QPushButton, QScrollArea, QFrame,
                            QApplication, QWidget, QSlider)
from pydm.widgets import PyDMEmbeddedDisplay
from pydm.utilities import connection
from scipy.ndimage.measurements import maximum_position


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


    def ui_filepath(self):
        # Return the full path to the UI file
        return path.join(path.dirname(path.realpath(__file__)), self.ui_filename())


    def setup_ui(self):
        # Create the main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Create a Label to be the title
        lbl_title = QLabel("Signal Viewer")

        # Add the title label to the main layout
        main_layout.addWidget(lbl_title)

        # Create the Signals Layout
        signals_layout = QVBoxLayout()

        # Create a GroupBox with "Signals" as Title
        gb_signals = QGroupBox(parent=self)
        gb_signals.setTitle("Signals")
        gb_signals.setLayout(signals_layout)

        # Create a signal scroll area, and add, load, save and delete buttons.
        btn_add = QPushButton()
        btn_add.clicked.connect(self.signals)
        btn_opacity = QPushButton()
        btn_opacity.clicked.checks or smt ***
        btn_opacity.returnPressed.connect(self.color_wheel)

        # Create a Frame to host the results of search
        self.frm_signals = QFrame(parent=self)
        self.frm_signals.setLayout(self.signals_layout)

        # Create a ScrollArea so we can properly handle many entries
        scroll_area = QScrollArea(parent=self)
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)

        # Add the Frame to the scroll area
        scroll_area.setWidget(self.frm_signals)

        # Add the scroll area to the main layout
        main_layout.addWidget(scroll_area)

        # Create the Time Manipulation Panel layout
        time_manipulation_layout = QHBoxLayout()

        # Create a GroupBox with "Time Manipulation" as Title
        gb_time_manipulation = QGroupBox(parent=self)
        gb_time_manipulation.setTitle("Time Manipulation")
        gb_time_manipulation.setLayout(time_manipulation_layout)

        # Add the created widgets to the layout
        search_layout.addWidget(lbl_search)
        search_layout.addWidget(self.txt_filter)
        search_layout.addWidget(btn_search)

        # Add the Groupbox to the main layout
        main_layout.addWidget(gb_search)

    def signals(self):
        # Create a signal check button, line edit, color slider and opacity check button.
        btn_signal_check = QPushButton()
        btn_signal_check.clicked.checks or smt***
        btn_signal_check.returnPressed.connect(self.time_plot)
        self.txt_signal = QLineEdit()
        self.txt_signal.returnPressed.connect(self.load_signal)
        slider_color = QSlider()
        slider_color.activated or smt***
        slider_color.activated.connect(self.color_wheel)
        btn_opacity = QPushButton()
        btn_opacity.clicked. checks or smt***
        btn_opacity.returnPressed.connect(self.color_wheel)
        
    def signal_setups_layout(self):
        h_layout = QHBoxLayout()
        h_layout.addWidget(QCheckBox)
        
    def add_signal(self):
        self.ui.signal_layout.addwidget(self.make_signal())
        signal.QCheckBox.checked.connect(self.update_plot)
"""