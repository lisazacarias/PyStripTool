from pydm import Display
from pydm.widgets import PyDMDrawingRectangle


class TimeManipulator(Display):
    def __init__(self):
        super().__init__()

    def ui_filename(self):
        return "PyStripToolLoadPopUp.ui"
    