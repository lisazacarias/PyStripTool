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
        self.ui.time_edit_button.clicked.connect(partial(showDisplay,
                                                              self.time_edit))

        """Create timeplot list."""
        self.timeplots = []
        self.make_timeplot()
        self.ui.timeplot_glayout.addLayout(self.timeplots[0], 0, 0)

        self.ui.timeplots_number_spinbox.valueChanged.connect(self.num_timeplots_changed)

    def make_signal(self):
        """Make the signal setups."""
        signal_setups = QHBoxLayout()

        # "Visible" Checkbox
        signal_check_box = QCheckBox()
        signal_setups.addWidget(signal_check_box)

        # "Signal" Line Edit
        signal_line_edit = QLineEdit()
        signal_setups.addWidget(signal_line_edit)

        # "Y-Axis Unit" Spinbox
        signal_y_axis_assignment_combo_box = QComboBox()
        signal_setups.addWidget(signal_y_axis_assignment_combo_box)

        # AutoScale Checkbox
        autoscale_checkbox = QCheckBox('AutoScale')
        signal_setups.addWidget(autoscale_checkbox)

        # "Y-Min" Spinbox
        y_min_spinbox = QSpinBox()
        signal_setups.addWidget(y_min_spinbox)

        # "Y-Max" Spinbox
        y_max_spinbox = QSpinBox()
        signal_setups.addWidget(y_max_spinbox)

        # "Color" Slider
        color_slider = QSlider()
        color_slider.setOrientation(QtCore.Qt.Horizontal)
        signal_setups.addWidget(color_slider)

        # "Opacity" Checkbox
        opacity_check_box = QCheckBox()
        signal_setups.addWidget(opacity_check_box)

        self.signals.append(signal_setups)

    def update_plot(self, time_plot):
        time_plot.setVisible(self.ui.signal_check_box.isChecked())
        time_plot.setCurves(self.ui.signal_line_edit.editingFinished())
        time_plot.setY(self.ui.signal_y_axis_assignment_combo_box.editingFinished())
        time_plot.setAutoRangeY(self.ui.autoscale_checkbox.isChecked())
        time_plot.setMinYRange(self.ui.y_min_spinbox.valueChanged())
        time_plot.setMaxYRange(self.ui.y_max_spinbox.valueChanged())
        time_plot.setColor(self.ui.color_slider.SliderMove())
        time_plot.setOpacity(self.ui.opacity_check_box.isChecked())

    def make_timeplot(self):
        """Make time plots and their edit buttons."""
        h_layout = QHBoxLayout()
        p_lot = PyDMTimePlot()
        h_layout.addWidget(p_lot)
        edit_button = PyDMRelatedDisplayButton('Edit')
        edit_button.clicked.connect(partial(showDisplay,
                                                         self.time_plot_edit))
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
