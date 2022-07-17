import time
import json
from qtpy import QtCore
from os import path
from pydm import Display
from qtpy.QtWidgets import (QVBoxLayout, QHBoxLayout, QGroupBox,
                            QLabel, QLineEdit, QPushButton, QScrollArea, QFrame,
                            QApplication, QWidget, QSlider, QCheckBox, QSpinBox, QTimeEdit)
from pydm.widgets import PyDMEmbeddedDisplay
from pydm.widgets import PyDMTimePlot
from pydm.widgets import PyDMByteIndicator
from pydm.utilities import connection
from scipy.ndimage.measurements import maximum_position


class PyStripTool(Display):

    def __init__(self, parent=None, args=None):
        super(PyStripTool, self).__init__(parent=parent, args=args)

    def y_axis_set_up(self):
        y_axis_line_edit = QLineEdit
        y_axis_line_edit.returnPressed.connect(self.data)
        y_axis_line_edit.returnPressed.connect(self.y_axis)
        delete_y_axis_unit_button = QPushButton
        delete_y_axis_unit_button.clicked.connect(self.y_axis)

    def y_axis_manipulator(self):
        add_y_axis = QPushButton()
        add_y_axis.clicked.connect(self.y_axis_set_up())
        y_axis_scroll_area = QScrollArea
        add_y_axis.clicked.connect(y_axis_scroll_area)

    def time_manipulation(self):
        (years_selector, months_selector, days_selector, hours_selector, minutes_selector) = QSpinBox
        QSpinBox.clicked.connect(self.x_axis)
        start_time_select = QTimeEdit
        start_time_select.clicked.connect(self.x_axis)
        pause_play_button = QPushButton
        pause_play_indicator = PyDMByteIndicator
        pause_play_button.clicked.connect(self.update_plot)
        pause_play_button.clicked.connect(pause_play_indicator)

    # Signal Color Opacity Set Up = SCOSU
    def scosu(self):
        signal_line_edit = QLineEdit()
        signal_line_edit.returnPressed.connect(self.data)
        (signal_checkbox, opacity_checkbox) = QCheckBox
        signal_checkbox.checked.connect(signal_line_edit)
        signal_checkbox.checked.connect(self.update_plot)
        color_slider = QSlider
        color_slider.SliderMove.connect(signal_line_edit)
        color_slider.SliderMove.connect(self.update_plot)
        opacity_checkbox.checked.connect(signal_line_edit)
        opacity_checkbox.checked.connect(self.update_plot)

    def signal_manipulation(self):
        (add_scosu, load_configuration, save_configuration, delete_scosu) = QPushButton
        add_scosu.clicked.connect(self.scosu())


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

    def ui_filename(self):
        # Point to our UI file
        return 'PyStripTool.ui'

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
        
    # Signal Color Opacity Set Up = SCOSU
    def scosu_layout(self):
        h_layout = QHBoxLayout()
        h_layout.addWidget(QCheckBox)
        
    def add_signal(self):
        self.ui.signal_layout.addwidget(self.make_signal())
        signal.QCheckBox.checked.connect(self.update_plot)
"""