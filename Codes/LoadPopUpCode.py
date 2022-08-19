from pydm import Display


class LoadPopUp(Display):
    def __init__(self):
        super().__init__()

    def ui_filename(self):
        return "PyStripToolLoadPopUp.ui"
