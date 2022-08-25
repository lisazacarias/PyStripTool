import sys
from qtpy import QtCore
import numpy as np
from PyQt5.QtCore import pyqtSlot
from functools import partial
from os import path
from pydm.widgets import PyDMTimePlot, PyDMRelatedDisplayButton
from PyQt5.QtWidgets import QCheckBox, QHBoxLayout, QLineEdit, QComboBox, QPushButton, QSpinBox, QSlider
from lcls_tools.common.pydm_tools.displayUtils import showDisplay
from pydm import Display


class Ui_Form(Display):
    """Build the Display."""

    def ui_filename(self):
        """Point to our UI file"""
        return 'PyStripTool.ui'

    def getPath(self, fileName):
        """Find files in the path."""
        return path.join(self.pathHere, fileName)

    def __init__(self, parent=None, args=None):
        """Inherit properties and still run init."""
        super().__init__(parent=parent, args=args)

        self.pathHere = path.dirname(sys.modules[self.__module__].__file__)

        """Call related Uis."""

        self.signal_edit = Display(ui_filename=self.getPath("PyStripToolLoadPopUp.ui"))
        self.time_edit = Display(ui_filename=self.getPath("PyStripToolTimeManip.ui"))
        self.time_plot_edit = Display(ui_filename=self.getPath("TimePlotsEditMenu.ui"))

        self.ui.signal_edit_tool_button.clicked.connect(partial(showDisplay,
                                                                self.signal_edit))
        """Create timeplot list."""
        self.timeplots = []
        self.make_timeplot()
        self.ui.timeplot_glayout.addLayout(self.timeplots[0], 0, 0)

        self.ui.timeplots_number_spinbox.valueChanged.connect(self.num_timeplots_changed)

        """Create signals list."""
        self.signals = []
        self.make_signal()
        for idx, item in enumerate(self.signals[0]):
            self.time_plot_edit.ui.signals_scroll_layout.addWidget(item, 1, idx)
        self.time_plot_edit.ui.add_signal_button.clicked.connect(self.make_signal)

    def make_signal(self):
        """Make the signal setups."""
        signal_setups = []

        # "Visible" Checkbox
        self.signal_check_box = QCheckBox()
        signal_setups.append(self.signal_check_box)

        # "Signal" Line Edit
        self.signal_line_edit = QLineEdit()
        signal_setups.append(self.signal_line_edit)

        # "Y-Axis Unit" Spinbox
        self.signal_y_axis_assignment_combo_box = QComboBox()
        signal_setups.append(self.signal_y_axis_assignment_combo_box)

        # AutoScale Checkbox
        self.autoscale_checkbox = QCheckBox('AutoScale')
        signal_setups.append(self.autoscale_checkbox)

        # "Y-Min" Spinbox
        self.y_min_spinbox = QSpinBox()
        signal_setups.append(self.y_min_spinbox)

        # "Y-Max" Spinbox
        self.y_max_spinbox = QSpinBox()
        signal_setups.append(self.y_max_spinbox)

        # "Color" Slider
        self.color_slider = QSlider()
        self.color_slider.setOrientation(QtCore.Qt.Horizontal)
        signal_setups.append(self.color_slider)

        # "Opacity" Checkbox
        self.opacity_check_box = QCheckBox()
        signal_setups.append(self.opacity_check_box)

        self.signals.append(signal_setups)

    def update_plot(self, time_plot: PyDMTimePlot):
        time_plot.setVisible(self.signal_check_box.isChecked())
        self.signal_line_edit.editingFinished.connect(partial(time_plot.addYChannel, self.signal_line_edit.text()))
        time_plot.setY(self.signal_y_axis_assignment_combo_box.editingFinished())
        time_plot.setAutoRangeY(self.autoscale_checkbox.isChecked())
        time_plot.setMinYRange(self.y_min_spinbox.valueChanged())
        time_plot.setMaxYRange(self.y_max_spinbox.valueChanged())
        time_plot.setColor(self.color_slider.SliderMove())
        time_plot.setOpacity(self.opacity_check_box.isChecked())

    def make_timeplot(self):
        """Make time plots and their edit buttons."""
        h_layout = QHBoxLayout()
        p_lot = PyDMTimePlot()
        h_layout.addWidget(p_lot)
        edit_button: QPushButton = QPushButton('Edit')
        edit_button.clicked.connect(partial(showDisplay, self.time_plot_edit))
        edit_button.clicked.connect(partial(self.update_plot, p_lot))
        h_layout.addWidget(edit_button)
        self.timeplots.append(h_layout)

    @staticmethod
    def get_dimensions(num_options):
        row_count = int(np.sqrt(num_options))
        col_count = int(np.floor(np.sqrt(num_options)))
        if row_count * col_count != num_options:
            col_count += 1
        return col_count

    @pyqtSlot(int)
    def num_timeplots_changed(self, value):
        self.clear_plot_layout()
        col_count = self.get_dimensions(value)
        if value <= len(self.timeplots):
            for idx, timeplot in enumerate(range(value)):
                self.ui.timeplot_glayout.addLayout(self.timeplots[idx],
                                                   int(idx / col_count),
                                                   idx % col_count)
        elif value > len(self.timeplots):
            for i in range(value-len(self.timeplots)):
                self.make_timeplot()
            for idx, timeplot in enumerate(range(value)):
                self.ui.timeplot_glayout.addLayout(self.timeplots[idx],
                                                   int(idx / col_count),
                                                   idx % col_count)

    def clear_plot_layout(self):
        while not self.ui.timeplot_glayout.isEmpty():
            item = self.ui.timeplot_glayout.itemAt(0)
            self.ui.timeplot_glayout.removeItem(item)
