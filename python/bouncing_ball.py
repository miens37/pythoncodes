"""
File: bouncing ball
Name: Sung mien huang
-------------------------
TODO:
"""
from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
window = GWindow(800, 500, title='bouncing_ball.py')
check = False

# oval = GOval(SIZE, SIZE)
# oval.filled = True
# oval.fill_color = 'black'
# window.add(oval, START_X, START_Y)
# can = True
# count = 0



def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(start)
    oval = GOval(SIZE, SIZE)
    oval.filled = True
    oval.fill_color = 'black'
    window.add(oval, START_X, START_Y)
    global check
    count = 3
    while True:
        if check and count > 0:
            check = False
            vy = 0
            while oval.x < window.width:
                oval.move(VX, vy)
                if vy > 0 and oval.y +SIZE > window.height:
                    vy = -vy + REDUCE
                vy += GRAVITY
                pause(DELAY)
            count -=1
            oval.x, oval.y = START_X, START_Y
        pause(DELAY)



def start(a):
    global check
    check = True
    """
    need oval as global for the window shows an oval at first
    can was a switch, at first was true to get in the while loop to move. But after the ball start moving,
    the switch turns off in case the mouse click would interrupted the ball falling
    the switch will turn on while the while loop ended (3 bounce out of x range around 1.2 window width in length)
    """

    # global can, oval, count
    # vy = 0
    # if can:
    #     can = False
    #     while True:
    #         vy += GRAVITY
    #         oval.move(VX, vy)
    #         if oval.x + SIZE >= 1.2*window.width:
    #             count += 1
    #             break
    #         if oval.y + SIZE >= window.height:
    #             # make sure the VY facing will turn around while adding -
    #             if vy >= 0:
    #                 vy = -vy * REDUCE
    #         pause(DELAY)
    #     # add a new ball onto the window for the next turn of bouncing ball play
    #     oval = GOval(SIZE, SIZE)
    #     oval.filled = True
    #     oval.fill_color = 'black'
    #     window.add(oval, START_X, START_Y)
    #     # if the ball out of x range for 3 times, it's game over. The switch will be off.
    #     if count == 3:
    #         can = False
    #     else:
    #         can = True


if __name__ == "__main__":
    main()
