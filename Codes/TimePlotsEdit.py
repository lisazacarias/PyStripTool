from pydm import Display
from lcls_tools.common.pydm_tools.pydmPlotUtil import (TimePlotParams,
                                                       TimePlotUpdater)


class TimePotEdit(Display):
    def __init__(self):
        super().__init__()
        self.time_plot_updater: TimePlotUpdater = None

        self.ui.timeplot_name_edit.editingFinished.connect(PyDMTimePlot())

        self.ui.delete_signal_button.clicked.connect(signals_scroll_layout)
        self.ui.add_yaxis_button.clicked.connect(signals_scroll_layout)
        self.ui.delete_yaxis_button.clicked.connect(signals_scroll_layout)

        """Create signals list."""
        self.signals = []
        self.make_signal()
        self.ui.signals_scroll_layout.addLayout(self.signals[0], 0, 0)
        self.ui.add_signal_button.clicked.connect()

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
        autoscale_checkbox = QCheckBox()
        signal_setups.addWidget(autoscale_checkbox('AutoScale'))

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

    @staticmethod
    def get_dimensions(num_options):
        row_count = int(np.sqrt(num_options))
        col_count = int(np.ceil(np.sqrt(num_options)))
        if row_count * col_count != num_options:
            col_count += 1
        return col_count

    @pyqtSlot(int)
    def num_timeplots_changed(self, value):
        self.clear_signal_layout()
        col_count = self.get_dimensions(value)
        if value <= len(self.signals):
            for idx, timeplot in enumerate(range(value)):
                self.ui.signals_scroll_layout.addLayout(self.signals[idx],
                                                   int(idx / col_count),
                                                   idx % col_count)

    def clear_plot_layout(self):
        while not self.ui.signals_scroll_layout.isEmpty():
            item = self.ui.signals_scroll_layout.itemAt(0)
            self.ui.signals_scroll_layout.removeItem(item)

    def ui_filename(self):
        return "TimePlotsEditMenu.ui"

