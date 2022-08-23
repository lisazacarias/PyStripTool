from pydm import Display
from pydm.widgets import PyDMDrawingRectangle


class TimeManipulator(Display):
    def __init__(self):
        super().__init__()
        self.ui.pause_play_button.clicked.connect(self.update_indicator)
        self.ui.days_selector.indexChanged()
        self.indicator: PyDMDrawingRectangle = self.ui.pause_play_indicator

    def update_indicator(self):
        if self.ui.pause_play_button.isChecked():
            self.indicator.brush.setColor(Red)

    def ui_filename(self):
        return "PyStripToolTimeManip.ui"
