"""
File: draw_line
Name:Sung mien huang
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


SIZE = 10
window = GWindow()
click = 0
x1 = 0
y1 = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(event):
    """
    if the click was odd then add oval
    if the click was even then erase oval add line
    click was a global count so it wont be restart after click by mouse
    x1, y1 was global so it wont be erase by new click by mouse
    """
    global click, x1, y1
    click += 1
    if click % 2 == 1:
        oval = GOval(SIZE,SIZE)
        oval.color = "black"
        window.add(oval,event.x-SIZE/2,event.y-SIZE/2)
        x1 = event.x - SIZE/2
        y1 = event.y -SIZE/2
    else:
        """
        get object at x1,y1 so we can erase oval made by previous click 
        """
        previous = window.get_object_at(x1+SIZE/2,y1+SIZE/2)
        window.remove(previous)
        line = GLine(x1, y1, event.x, event.y)
        window.add(line)


if __name__ == "__main__":
    main()
