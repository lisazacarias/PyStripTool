from pydm import Display
from pydm.widgets import PyDMDrawingRectangle


class TimeManipulator(Display):
    def __init__(self):
        super().__init__()
        self.ui.pause_play_button_2.clicked.connect(self.update_indicator)
        self.ui.days_selector_2.indexChanged()
        self.indicator: PyDMDrawingRectangle = self.ui.pause_play_indicator_2

    def update_indicator(self):
        if self.ui.pause_play_button_2.isChecked():
            self.indicator.brush.setColor(Red)

    def ui_filename(self):
        return "PyStripToolTimeManip.ui"
