"""ASCII drawing API

render_canvas with specific height and width
add_shape to a canvas
clear_all shapes from a canvas
create_rectangle

change_fill character for a rectangle
traverse a shape around a canvas"""


class Rectangle:
    """a shape on a canvas, takes a fill char a start_x and y, and an end_x and y
    
    Examples:
    >>> Rectangle('X', 0, 0, 1, 1)
    XX
    XX
    """
    
    def __init__(self, fill, start_x, start_y, end_x, end_y):
        self.fill = fill
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y


    def change_fill(self, char):
        """change the fill character to a pre-existing rectangle object
        
        >>> Rectangle('X', 0, 0, 1, 1).change_fill('Y')
        YY
        YY
        """

        self.fill = char

        return self


    def transform(self, axis, num):
        """changes the positioning of the shape. axis is either x or y, num is how many units it should move
        
        >>> Rectangle('X', 0, 0, 1, 1).transform('x', 1)
        'Moved 1 unit[s] to the right'"""

        if axis == "y":
            self.start_y += num
            self.end_y += num
            if num < 0:
                direction = "up"
            else:
                direction = "down"

        elif axis == "x":
            self.start_x += num
            self.end_x += num
            if num < 0:
                direction = "to the left"
            else:
                direction = "to the right"

        return f"Moved {num} unit[s] {direction}"



    def __repr__(self):
        """calling object prints the object as it appears"""

        shape = (f"{self.fill}" * ((self.end_x + 1) - self.start_x) + "\n") * ((self.end_y + 1) - self.start_y)
        return shape[:-1]
    

class Canvas:
    """canvas objects have general width and height, set by units of rows and height
    store shapes in in a list, sets the fill by their coordinates
    
    Example:
    >>> Canvas(5, 5)
    <Canvas 5 x 5>

    """

    def __init__(self, width, height, fill=" "):
        self.width = width
        self.height = height
        self.fill = fill
        self.shapes = []
        ## canvas shapes are stored in coordinates as dictionary
        ## keys are y coordinates, indeces of list values are x coordinates
        self.coordinates = self.clear_all()


    def render_canvas(self):
        """prints canvas and its shapes to standard output
        
        goes through canvas' coordinates, where shapes are placed, prints each row

        >>> Canvas(5,5,"x").render_canvas()
        xxxxx
        xxxxx
        xxxxx
        xxxxx
        xxxxx
        """

        for shape in self.shapes:
            start_x = shape.start_x
            start_y = shape.start_y
            end_x = shape.end_x
            end_y = shape.end_y
            width = (end_x + 1) - start_x

            for i in range(start_y, end_y + 1):
                self.coordinates[i][start_x:end_x + 1] = [shape.fill] * width

        for row in self.coordinates.values():
            print("".join(row))


    def add_shape(self, shape):
        """adds a shape to the canvas' coordinates
        
        >>> Canvas(5,5,'X').add_shape(Rectangle('y',0,0,0,0))
        [y]
        """

        self.shapes.append(shape)

        return self.shapes


    def clear_all(self):
        """remove all shapes from a canvas"""

        self.coordinates = {}
        for i in range(self.height):
            self.coordinates[i] = [self.fill]*self.width

        self.shapes = []

        return self.coordinates


    def create_rectangle(self, fill_char, start_x, start_y, end_x, end_y):
        """creates a rectangle using canvas coordinates
        start_y is index of canvas items, start_x is index within start_y's string - upper left hand corner
        end_y and end_x are same = lower right hand corner
        fill_char is char to change all indexes between start and end to

        >>> Canvas(5,5,'X').create_rectangle('y',1,1,3,3).render_canvas()
        XXXXX
        XyyyX
        XyyyX
        XyyyX
        XXXXX
        
        """

        rectangle = Rectangle(fill_char, start_x, start_y, end_x, end_y)
        self.add_shape(rectangle)

        return self
    

    def __repr__(self):
        """gives canvas details"""

        return f"<Canvas {self.width} x {self.height}>"


if __name__ == "__main__":
    import doctest
    doctest.testmod()