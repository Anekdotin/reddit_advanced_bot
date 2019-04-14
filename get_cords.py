from Xlib import display
import time

while 1 == 1:
    data = display.Display().screen().root.query_pointer()._data
    thedata = data["root_x"], data["root_y"]
    time.sleep(2)
    print(thedata)