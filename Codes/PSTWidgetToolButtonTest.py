import sys
from PyQt5.QtCore import pyqtSlot
from functools import partial
from os import path

from PyQt5.QtWidgets import QHBoxLayout, QPushButton
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

        self.signal_edit = Display(ui_filename=self.getPath("SignalEditMenu.ui"))
        self.time_edit = Display(ui_filename=self.getPath("PyStripToolTimeManip.ui"))
        self.time_plot_edit = Display(ui_filename=self.getPath("TimePlotsEditMenu.ui"))

        self.ui.signal_edit_tool_button.clicked.connect(partial(showDisplay,
                                                                self.signal_edit))
        self.ui.time_edit_tool_button.clicked.connect(partial(showDisplay,
                                                              self.time_edit))

        """Create timeplot list."""
        self.timeplots = []
        self.make_timeplot()
        self.ui.timeplot_glayout.addLayout(self.timeplots[0], 0, 0)

        self.ui.timeplots_number_spinbox.valueChanged.connect(self.num_timeplots_changed)

    def make_timeplot(self):
        """Make time plots and their edit buttons."""
        h_layout = QHBoxLayout()
        p_lot = PyDMTimePLot()
        h_layout.addWidget(p_lot)
        edit_button = QPushButton('Edit')
        edit_button.clicked.connect(partial(self.time_plot_edit.update_plot, p_lot))
        h_layout.addWidget(edit_button)
        self.timeplots.append(h_layout)

    @staticmethod
    def get_dimensions(num_options):
        row_count = int(np.sqrt(num_options))
        col_count = int(np.ceil(np.sqrt(num_options)))
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

    def clear_plot_layout(self):
        while not self.ui.timeplot_glayout.isEmpty():
            item = self.ui.timeplot_glayout.itemAt(0)
            self.ui.timeplot_glayout.removeItem(item)
