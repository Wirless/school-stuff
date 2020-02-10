# ==================================================================
# title           :test_rect.py
# description     :a test file for the Rectangle class
# author          :srattigan
# date            :05 Feb 2020
# version         :1.0
# notes           :starter code provided for testing
#                  based on your reading of the code, you can
#                  complete the code for additional tests
# python_version  :3.7  
# file_version    :1.00
# ==================================================================

# -- IMPORTS --
from rectangle import Rectangle
import operator  # see https://docs.python.org/3/library/operator.html
import random as r
try:  # this coloring only works in the terminal
    import colorama  # see https://pypi.org/project/colorama/
    gtext = colorama.Fore.GREEN
    rtext = colorama.Fore.RED
    txt_rst = colorama.Style.RESET_ALL
except:  # if coloram is not installed, ignore the color codes
    gtext=""
    rtext=""
    txt_rst=""

# -- GLOBALS/CONSTANTS --
RED = (255, 0, 0)
BLUE = (0, 0, 255)
box_bucket = []
# change values you use in your class if instantiating with a single string
op_ref = {"+": operator.add,
          "-": operator.sub,
          "*": operator.mul,
          "/": operator.truediv}  # can change if you need to

my_nums = [100, 200, 10, 80, 60.2, 90.66, 140.8]

# -- FUNCTIONS --
def set_random_color():
    '''
    (None)->tuple of int
    Helper function- Generates a random RGB color for color tests
    '''
    return (r.randrange(255), r.randrange(255), r.randrange(255))
    

def instantiation_tests():
    """
    (None)->bool
    Tests Instantiation
    """
    print("---Instantiation and str tests---")
    try:
        for each in range(len(my_nums)-1):
            box_bucket.append(Rectangle(my_nums[each], my_nums[each+1]))
            box_bucket.append(Rectangle(my_nums[each], my_nums[each+1])) # a duplicate set
        print(f"{gtext}\n\tAll instantiations successful\n{txt_rst}")
        print("These are the units generated that will be used in all tests")
        for each in box_bucket:
            print("\t", each)
        print("Note: All instantiations printed using __str__ method\n")
        return True
    except Warning("Failed Instantiation"):
        print("Something went horribly wrong")
        return False

def change_color_tests():
    """
    (None)->bool
    Test changing the color of half the rectangles
    """
    print("\n\n---Change Color tests---\n")
    try:
        for rect in range(len(box_bucket) // 2):
            print(f"\tBefore:\t", box_bucket[rect])
            box_bucket[rect].color = set_random_color()
            print(f"\tAfter:\t", box_bucket[rect])
        print(f"{gtext}\nNote: All seems to have gone well changing colors- have they changed?{txt_rst}")
        return True
    except Warning(f"{rtext}Failed Color Change{txt_rst}"):
        print(f"{rtext}Something went horribly wrong{txt_rst}")
        return False

def perimeter_tests():
    '''
    (None)->bool
    Tests perimeter values of rectangles
    '''
    print("\n\n---Perimeter tests---\n")
    return False
    
def area_tests():
    '''
    (None)->bool
    Tests area values of rectangles
    '''
    print("\n\n---Area tests---\n")
    try:
        for box in box_bucket:
            print(f"\t", box, "has area of", box.area())
        return True
    except Warning(f"{rtext}Failed Area Test{txt_rst}"):
        print(f"{rtext}Something went horribly wrong{txt_rst}")
        return False
        
    
def operator_plus_minus_tests(ops=["+", "-"]):
    """
    (list of str)->bool
    Tests add and sub arithmetic operators
    """
    print("\n\n-----Testing overloaded add and sub operators-----")
    for op in ops:
        print("\nTesting operator:", op)
        for idx in range(len(box_bucket)-1):
            try:
                result = op_ref[op](box_bucket[idx], box_bucket[idx+1])
                #print("TEST", type(result))
                print(f"\t{box_bucket[idx]} {op}\n\t{box_bucket[idx+1]} =\n\t{result}")
                print(f"\t{box_bucket[idx].area()} {op} {box_bucket[idx+1].area()} = {result.area()}\n")
            except:
                print("Failed with: ", box_bucket[idx], op_ref[op], box_bucket[idx+1])
    print(f"{gtext}All Add/Sub tests have executed{txt_rst}")
    return True

def operator_mul_div_tests(ops=["*", "/"], vals=[2, 10, 3.33]):
    """
    (list of str)->bool
    Tests mul and div arithmetic operators
    """
    print("\n\n-----Testing overloaded mul and div operators-----")
    for op in ops:
        print("\nTesting operator:", op)
        for val in vals:
            for rect in box_bucket:
                try:
                    result = op_ref[op](rect, val)
                    print(f"\t{rect} {op} {val} = \n\t{result}")
                    print(f"\tArea check: {rect.area()} {op} {val} = {result.area()}\n")
                except:
                    print(f"\tFailed with: {rect} {op_ref[op]} {val}")
    print(f"{gtext}All Mul/Div tests have executed{txt_rst}")
    return True

def draw_tests():
    for rect in box_bucket[1:3]:
        rect.draw()
    return True


def operator_logical_tests(ops):
    """
    (list of str)->bool
    Tests a range of arithmetic operators
    """
    print(f"{rtext}\n--Logical operator tests not yet implemented--\n{txt_rst}")
    return False


# main body

if __name__ == "__main__":
    print("\t\t TESTS FOR IMPERIAL CLASS\n")
    created = instantiation_tests()  # returns a bool- True if all instantiations work, False otherwise
    if created:
        try:
            if change_color_tests():
                print(f"{gtext}Tests for changing color ran...{txt_rst}\n\n")
        except:
            print(f"{rtext}Change color tests could not be completed{txt_rst}\n\n")
        
        try:
            if area_tests():
                print(f"{gtext}Tests for areas ran...review values!{txt_rst}\n\n")
        except:
            print(f"{rtext}Area tests could not be completed{txt_rst}\n\n")
        
        try:
            if perimeter_tests():
                print(f"{gtext}Tests for Perimeters ran...review values!{txt_rst}\n\n")
        except:
            print(f"{rtext}Perimeter tests could not be completed{txt_rst}\n\n")
        
        try:
            if operator_plus_minus_tests():
                print(f"{gtext}Tests for Plus/Minus ran...review values!{txt_rst}\n\n")
        except:
            print(f"{rtext}Arithmetic Plus/Minus tests could not be completed{txt_rst}")
    
        try:
            if operator_mul_div_tests():
                print(f"{gtext}Tests for Mul/Div ran...review values!{txt_rst}\n\n")
        except:
            print(f"{rtext}Arithmetic Mul/Div tests could not be completed{txt_rst}\n\n")
        
        try:
            if operator_logical_tests():
                print(f"{gtext}Logic Operator tests ran...review values!{txt_rst}\n\n")
        except:
            print(f"{rtext}Logical tests could not be completed{txt_rst}")
            
        try:
            if draw_tests():
                print(f"{gtext}Draw tests ran...review values!{txt_rst}\n\n")
        except:
            print(f"{rtext}Draw tests could not be completed{txt_rst}")

