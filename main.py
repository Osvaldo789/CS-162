#Function 1
# Returns Area of Rectangle
def rect_area(side):
    return side**2
#Function 2
#Returns Surface Area of Rectangular Solid
#written by Osvaldo Contreras
def rect_surface_area():
    """
    Calculates the surface area of a cube by multiplying square by 6

    Returns
    -------
    int : surface area of cube
    """
    return square * 6


#length of the sides of the cube
side = int(input("Enter the length of the the side of the cube as an integer: "))

#stores the value of the area of 1 face of the cube
square = rect_area(side)

print(f"Side = {str(side)}")
print("Total Surface Area = ", str(rect_surface_area()))
print("Area of the rectangle: " + str(rect_area(side)))

