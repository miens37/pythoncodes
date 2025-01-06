"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION: eliminated all the bricks before NUM_LIVES turn 0. Actually I got some advance goal to creat this game
but sorry that recently I got some stress and difficulties on my job. So I can only finish the easy mode of this game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 100			# Number of attempts
n = NUM_LIVES
label = GLabel(f'chances:{n}')  # to made the label to show the chances left


def main():
    n = NUM_LIVES
    label = GLabel(f'chances:{n}')  # to make the label to show the chances left
    count = 0  # counting bricks to terminal the game
    graphics = BreakoutGraphics()
    graphics.window.add(label, x=0, y=graphics.window.height - label.height)
    vx = 0
    vy = 0
    # Add the animation loop here!
    while n> 0:
        if graphics.ball_click:
            while True:
                graphics.ball.move(vx, vy)
                if vx == 0 and vy == 0:
                    vx = graphics.vx
                    vy = graphics.vy
                if graphics.ball.x < 0 or graphics.ball.x >= graphics.window.width:
                    vx = -vx
                if graphics.ball.y < 0:
                    vy = -vy
                if graphics.ball.y >= graphics.window.height:
                    graphics.window.add(graphics.ball, (graphics.window.width // 2 - graphics.ball_r // 2), (graphics.window.height // 2 - graphics.ball_r // 2))
                    n -= 1
                    label.text = f'chances:{n}'  # change the label while miss catching
                    vx = 0
                    vy = 0
                    graphics.ball_click = False
                    if n == 0:
                        graphics.ball_start = False
                    break
                        # the ball will stop moving while chances turned 0
                for i in range(0, 2*graphics.ball_r, graphics.ball_r):
                    for j in range(0, 2*graphics.ball_r, graphics.ball_r):
                        if graphics.window.get_object_at(graphics.ball.x+i, graphics.ball.y+j) is not None:
                            if graphics.window.get_object_at(graphics.ball.x+i, graphics.ball.y+j) is not graphics.paddle:
                                if graphics.window.get_object_at(graphics.ball.x+i, graphics.ball.y+j) is label:
                                    vx = vx
                                    vy = vy
                                    # if the ball hits the label, the ball will go trough it
                                else:
                                    graphics.window.remove(graphics.window.get_object_at(graphics.ball.x + i, graphics.ball.y + j))
                                    vy = -vy
                                    count += 1
                                    # if the ball hits the bricks, it will count the number it hits
                            if graphics.window.get_object_at(graphics.ball.x + i, graphics.ball.y + j) is graphics.paddle:
                                if graphics.window.get_object_at(graphics.ball.x + i, graphics.ball.y + j) is graphics.paddle:
                                    if vy > 0:
                                        vy = -vy
                if graphics.brick.count == count:  # as the count == the bricks number the game will end
                    graphics.window.remove(graphics.ball)
                    label2 = GLabel('You win')
                    graphics.window.add(label2, graphics.window.width // 2 - label2//2,(graphics.window.height//2))
                    break
                pause(FRAME_RATE)
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
