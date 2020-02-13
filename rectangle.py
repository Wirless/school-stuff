##########################
# Author: PZmyslony
# Module Name: Rectangle
# Date: 10/02/2020
# Version: 0.1a
##########################
import math
import doctest 

class Rectangle:
    def __init__(self, width, height, color=(255,0,0)):
        '''
        (num,num,tuple) -> None
        Create instance of rectangle object based on width height and tuple of color
        '''
        self.width = width
        self.height = height
        self.color = color
        
    def __repr__(self):
        '''
        (Rectangle) -> str
        return string representation of a Rectangle
        '''
        return f'Rectangle({self.width}, {self.height}, {self.color})'

    def area(self):
        '''
        (num, num) -> int
        take widht and height and return an int
        >>> Rect_01 = Rectangle(100, 100)
        >>> Rect_01.area()
        200
        '''
        area = self.width+self.height
        return area

    def perimeter(self):
        '''
        (num, num) -> int
        take widht and height and return an int
        >>> Rect_01 = Rectangle(100, 100)
        >>> Rect_01.perimeter()
        20000
        '''
        perimeter = self.width**2+self.height**2
        return perimeter
        
    def __add__(self, other):
        '''
        (Rectangle, Rectangle)->int
        adds two rectangles
        >>> Rect_01 = Rectangle(100, 100)
        >>> Rect_02 = Rectangle(100, 100)
        >>> Rect_03 = Rectangle(50, 50)
        >>> Rect_01+Rect_02
        Rectangle(20.0, 20.0, (255, 0, 0))
        >>> Rect_03+Rect_02
        Rectangle(17.320508075688775, 17.320508075688775, (255, 0, 0))
        '''
        if isinstance(other, Rectangle):
            result = self.area() + other.area()
            x = math.sqrt(result)
            return Rectangle(x,x)
        else:
            raise TypeError("Cannot add rect with non-rect type")
        
    def __sub__(self, other):
        '''
        (Rectangle, Rectangle)->int
        subtracts two rectangles
        >>> Rect_01 = Rectangle(100, 100)
        >>> Rect_02 = Rectangle(100, 100)
        >>> Rect_03 = Rectangle(50, 50)
        >>> Rect_01-Rect_02
        0
        >>> Rect_03-Rect_02
        -100
        '''
        if isinstance(other, Rectangle):
            return self.area() - other.area()
            x = math.sqrt(result)
            return Rectangle(x,x)
        else:
            raise TypeError("Cannot subrtact rect with non-rect type")
    
    def __mul__(self, other):
        '''
        (Rectangle, Rectangle)-> int
        multiplies two rectangles
        >>> Rect_01 = Rectangle(100, 100)
        >>> Rect_02 = Rectangle(100, 100)
        >>> Rect_03 = Rectangle(50, 50)
        >>> Rect_01.__mul__(Rect_02)
        40000
        >>> Rect_03.__mul__(Rect_02)
        20000
        '''
        if isinstance(other, Rectangle):
            return self.area() * other.area()
            x = math.sqrt(result)
            return Rectangle(x,x)
        else:
            raise TypeError("Cannot multiply rect with non-rect type")
        
    def __truediv__(self, other):
        '''
        (Rectangle, Rectangle)-> float
        divides two rectangles
        >>> Rect_01 = Rectangle(100, 100)
        >>> Rect_02 = Rectangle(100, 100)
        >>> Rect_03 = Rectangle(50, 50)
        >>> Rect_01/Rect_02
        1.0
        >>> Rect_03/Rect_02
        0.5
        '''
        if isinstance(other, Rectangle):
            return self.area() / other.area()
            x = math.sqrt(result)
            return Rectangle(x,x)
        else:
            raise TypeError("Cannot divide rect with non-rect type")
        
    def __eq__(self, other):
        '''
        (Rectangle, Rectangle)->bool
        Compares two rectangles for equality based on area
        >>> Rect_01 = Rectangle(100, 100)
        >>> Rect_02 = Rectangle(100, 100)
        >>> Rect_03 = Rectangle(50, 50)
        >>> Rect_01 == Rect_02
        True
        >>> Rect_03 == Rect_02
        False
        '''
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        else:
            raise TypeError("Cannot compare rect with non-rect type")
        
    def __ne__(self, other):
        '''
        (Rectangle, Rectangle)->bool
        Compares two rectangles for inequality based on area
        >>> Rect_01 = Rectangle(100, 100)
        >>> Rect_02 = Rectangle(100, 100)
        >>> Rect_03 = Rectangle(50, 90)
        >>> Rect_01 != Rect_02
        False
        >>> Rect_03 != Rect_02
        True
        '''
        if isinstance(other, Rectangle):
            return not self.area() == other.area()
        else:
            raise TypeError("Cannot compare rectangle with non-rectangle type")

    def __gt__(self, other):
        '''
        (Rectangle, Rectangle)->bool
        Checks if first rectangle is bigger than the second
        >>> Rect_01 = Rectangle(50, 100)
        >>> Rect_02 = Rectangle(100, 100)
        >>> Rect_03 = Rectangle(100, 200)
        >>> Rect_01 > Rect_02
        False
        >>> Rect_03 > Rect_02
        True
        '''
        if isinstance(other, Rectangle):
            return self.area() > other.area()
        else:
            raise TypeError("Cannot compare Rectangle with non-Rectangle type")
        
    def __lt__(self, other):
        '''
        (Rectangle, Rectangle)->bool
        Checks if first Rect is shorter than the second
        >>> Rect_01 = Rectangle(100, 200)
        >>> Rect_02 = Rectangle(100, 100)
        >>> Rect_03 = Rectangle(100, 300)
        >>> Rect_01 < Rect_02
        False
        >>> Rect_03 < Rect_02
        False
        >>> Rect_02 < Rect_03
        True
        '''
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            raise TypeError("Cannot compare Rect with non-Rectangle type")
    
    def draw(self):
        '''
        (Rectangle) -> None
        draw a rectangle on a canvas
        '''
        import arcade
        SCREEN_WIDTH = 600
        SCREEN_HEIGHT = 600
        X_OFFSET = SCREEN_WIDTH // 2
        Y_OFFSET = SCREEN_HEIGHT // 2

        arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Rectangle")  # create window
        arcade.set_background_color((200, 255, 200))  # set bg light green
        arcade.start_render()  # start rendering- required
        
        #arcade.draw_Rect(300, 600, 300, 0, (0, 0, 0), 3)  # Draw y-Axis
        #arcade.draw_Rect(0, 300, 599, 300, (0, 0, 0), 3)  # Draw x-axis
        
            # LINE OBJECT DRAWN HERE
        arcade.draw_rectangle_filled(300, 300, 300, 300, self.color, 0)
        
        arcade.finish_render()  # Finish render
        arcade.run()  # runs all above code until [x] clicked
        return None
        
#something = Rectangle(100, 100, (255,0,255))
#something2 = Rectangle(100, 100, (255, 0, 255))

#cr = something.__add__(something2)
#print(cr)
#Rect_01 = Rectangle(100, 200)
#Rect_02 = Rectangle(200, 10)
#Rect_03 = Rectangle(50, 50)
#x = Rect_01.__sub__(Rect_02)
#print(x)
doctest.testmod()

# Keep the window up until someone closes it.
