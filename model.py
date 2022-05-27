"""ASCII drawing API

render_canvas with specific height and width
add_shape to a canvas
clear_all shapes from a canvas
create_rectangle
change_fill character for a rectangle
traverse up, down, left, right"""


def render_canvas(height, width):
    """prints canvas and its shapes to standard output
    
    takes height as int and width as int
    returns returns an array with height-number strings that have width-number of spaces"""

    x = " "*width
    canvas = [x]*height

    for lst in canvas:
        print(lst)


def add_shape(shape):
    """adds a shape to the canvas"""


def clear_all():
    """remove all shapes from a canvas"""


def create_rectangle(start_x, start_y, end_x, end_y, fill_char):
    """creates a rectangle using canvas coordinates
    start_y is index of canvas items, start_x is index within start_y's string - upper left hand corner
    end_y and end_x are same = lower right hand corner
    fill_char is char to change all indexes between start and end to"""

    


def change_fill(char):
    """change the fill character to a pre-existing rectangle object"""


def traverse(axis, num):
    """moves a rectangle within a canvas
    axis is direction(x-left/right, y-up/down)
    num is int to move - negative is left/down, positive is right/up"""