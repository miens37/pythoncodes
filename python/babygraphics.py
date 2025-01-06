"""
File: babygraphics.py
Name: Sung mien huang
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    k = (width - 2 * GRAPH_MARGIN_SIZE)//len(YEARS)
    return GRAPH_MARGIN_SIZE+year_index*k


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for i in range(len(YEARS)):   # because we need year index, i choose for i in range loop in order to get the order
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT, width=LINE_WIDTH)
        year = YEARS[i]
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=year, anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    n = (CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE)/MAX_RANK   # counting the space for ranking spot
    k = 0   # for color choosing
    for name in lookup_names:
        if name in name_data:
            year_rank = name_data[name]
            y = {}       # for getting y coordinate later in line
            for i in range(len(YEARS)):    # due to x coordinate function, we will need the year index
                match = YEARS[i]
                match = str(match)
                y1 = 0
                if match not in name_data[name]:    # if there was no match in YEARS list, add * at the bottom
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=(name, "*"), anchor=tkinter.SW, fill=COLORS[k])
                    y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    y[i] = int(y1)
                for year in year_rank:     # others year we will add the rank on the year of it
                    rank = year_rank[year]
                    rank = int(rank)
                    year = str(year)
                    if year == match:
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, GRAPH_MARGIN_SIZE + rank * n, text=(name, rank), anchor=tkinter.SW, fill=COLORS[k])
                        y1 = GRAPH_MARGIN_SIZE + rank * n
                        y[i] = int(y1)
                if 1 <= i < len(YEARS):  # we add lines from the second spot to the last
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i-1), int(y[i-1]), get_x_coordinate(CANVAS_WIDTH,i), y1, fill=COLORS[k], width=LINE_WIDTH)
            k += 1     # due to the color list we had only 4 color the color will reset while k reaches four
            if k == 4:
                k = 0


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
