import sys
from functools import partial
from os import path

from lcls_tools.common.pydm_tools.displayUtils import showDisplay
from pydm import Display


class Ui_Form(Display):
    """Build the Display."""

    def ui_filename(self):
        # Point to our UI file
        return 'PyStripTool.ui'

    def getPath(self, fileName):
        # Find files in the path.
        return path.join(self.pathHere, fileName)

    def __init__(self, parent=None, args=None):
        # Inherit properties and still run init.
        super().__init__(parent=parent, args=args)

        self.pathHere = path.dirname(sys.modules[self.__module__].__file__)

        self.signal_edit = Display(ui_filename=self.getPath("SignalEditMenu.ui"))
        self.time_edit = Display(ui_filename=self.getPath("PyStripToolTimeManip.ui"))
        self.plot_edit = Display(ui_filename=self.getPath("TimePlotsEditMenu.ui"))

        self.ui.signal_edit_tool_button.clicked.connect(partial(showDisplay, self.signal_edit))
        self.ui.time_edit_tool_button.clicked.connect(partial(showDisplay, self.time_edit))
