from Xlib import display
import time


def cords():
    data = display.Display().screen().root.query_pointer()._data
    thedata = data["root_x"], data["root_y"]
    time.sleep(2)
    return str(thedata)
