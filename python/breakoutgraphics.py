"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 8    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.ball_r = 2*ball_radius
        self.paddle_off = paddle_offset
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (window_width-paddle_width)//2,window_height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS*2, BALL_RADIUS*2)
        self.ball.filled = True
        self.ball.color = 'navy'
        self.ball.fill_color = 'navy'
        self.window.add(self.ball, (window_width//2-ball_radius), (window_height//2-ball_radius))
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.ball_start = True
        self.ball_click = False
        # Initialize our mouse listeners
        onmousemoved(self.move)
        onmouseclicked(self.start)
        # Draw bricks
        self.brick_offset = brick_offset
        self.brick_cols = brick_cols
        self.brick_rows = brick_rows
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_spacing = brick_spacing
        self.draw_bricks()

    def draw_bricks(self):
        b = 0
        c = self.brick_offset
        brick_color = 'black'
        for i in range(self.brick_cols):
            for j in range(self.brick_rows):
                self.brick = GRect(self.brick_width, self.brick_height)
                self.brick.count = self.brick_cols*self.brick_rows
                self.brick.filled = True
                if j // 2 == 0:
                    brick_color = 'red'
                elif j//2 == 1:
                    brick_color = 'orange'
                elif j//2 == 2:
                    brick_color = 'yellow'
                elif j//2 == 3:
                    brick_color = 'green'
                elif j//2 == 4:
                    brick_color = 'navy'
                elif j//2 == 5:
                    brick_color = 'purple'
                self.brick.color = brick_color
                self.brick.fill_color = brick_color
                b = i * (self.brick_spacing + self.brick_width)
                c = (j + 1) * (self.brick_spacing + self.brick_height)
                self.window.add(self.brick, b, c)

    def start(self, s):
        # can: open the switch of moving the ball
        # can2: the switch of mouse clicking
        if self.ball_start:
            self.ball_click = True
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = - self.__dx
            self.__dy = INITIAL_Y_SPEED

    def move(self, mouse):
        # turn off the can2 to block the effect of mouse clicking
        if mouse.x <= self.paddle.width//2:
            self.paddle.x = 0
        elif mouse.x >= self.window.width - self.paddle.width//2:
            self.paddle.x = self.window.width - self.paddle.width//2
        else:
            self.paddle.x = mouse.x - self.paddle.width//2

    @property
    def vx(self):
        return self.__dx

    @property
    def vy(self):
        return self.__dy

