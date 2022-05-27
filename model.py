"""ASCII drawing API

render_canvas with specific height and width
add_shape to a canvas
clear_all shapes from a canvas
create_rectangle
change_fill character for a rectangle
traverse up, down, left, right"""


class Rectangle:
    """a shape on a canvas, has a width """
    
    def __init__(self, width, height, fill, start_x, start_y):
        self.width = width
        self.height = height
        self.fill = fill
        self.start_x = start_x
        self.start_y = start_y


    def change_fill(self, char):
        """change the fill character to a pre-existing rectangle object"""

        self.fill = char

    def __repr__(self):

        shape = (f"{self.fill}" * self.width + "\n") * self.height
        return shape[:-1]
    

class Canvas:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.coordinates = {}

        for i in range(self.height):
            self.coordinates[i] = [" "]*self.width


    def render_canvas(self):
        """prints canvas and its shapes to standard output
        
        takes height as int and width as int
        returns returns an array with height-number strings that have width-number length"""

        for row in self.coordinates.values():
            print("".join(row))


    def add_shape(self, shape):
        """adds a shape to the canvas"""

        start_x = shape.start_x
        start_y = shape.start_y
        width = start_x + shape.width
        height = start_y + shape.height

        for i in range(start_y, height):
            self.coordinates[i][start_x:width] = [shape.fill] * shape.width



    def clear_all(self):
        """remove all shapes from a canvas"""

        ##TODO: need to finish render_canvas


    def create_rectangle(self, start_x, start_y, end_x, end_y, fill_char):
        """creates a rectangle using canvas coordinates
        start_y is index of canvas items, start_x is index within start_y's string - upper left hand corner
        end_y and end_x are same = lower right hand corner
        fill_char is char to change all indexes between start and end to"""

        width = end_x - start_x
        height = end_y - start_y

        rectangle = Rectangle(width, height, fill_char, start_x, start_y)
        self.add_shape(rectangle)
    

    def __repr__(self):
        """  """

        return f"Canvas {self.width} x {self.height}"



def traverse(axis, num):
    """moves a rectangle within a canvas
    axis is direction(x-left/right, y-up/down)
    num is int to move - negative is left/down, positive is right/up"""