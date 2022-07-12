import time
from os import path
from pydm import Display
from scipy.ndimage.measurements import maximum_position


class PyStripTool(Display):

    def __init__(self, parent=None, args=None):
        super(PyStripTool, self).__init__(parent=parent, args=args)


    def ui_filename(self):
        # Point to our UI file
        return 'Signal Viewer Draft 2_Electric Boogaloo.ui'

    def ui_filepath(self):
        # Return the full path to the UI file
        return path.join(path.dirname(path.realpath(__file__)), self.ui_filename())
