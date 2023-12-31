# 4. Write some code to compute the area & perimeter of the following geometrical shapes:
# triangle, square, rectangle, circle,
# Rhombus, Parallelogram, Trapezoid, Pentagon, Hexagon, Decagon.

import math


def triangle():
    base = float(input("Base: "))
    height = float(input("Height: "))
    side1 = float(input("Side 1: "))
    side2 = float(input("Side 2: "))
    print(f"Area: {base*height/2}")
    print(f"Perimeter: {side1 + side2 + base}")
    return


def square():
    side = float(input("Side: "))
    print(f"Area: {side*side}")
    print(f"Perimeter: {4*side}")


def rectangle():
    length = float(input("Length: "))
    width = float(input("Width: "))
    print(f"Area: {length*width}")
    print(f"Perimeter: {2*(length+width)}")


def circle():
    radius = float(input("Radius: "))
    print(f"Area: {math.pi*radius}")
    print(f"Perimeter: {math.pi*math.power(radius, 2)}")


def rhombus():
    diagonal1 = float(input("Diagonal 1: "))
    diagonal2 = float(input("Diagonal 2: "))
    side = float(input("Side: "))
    print(f"Area: {diagonal1*diagonal2/2}")
    print(f"Perimeter: {4*side}")


def parallelogram():
    base = float(input("Base: "))
    height = float(input("Height: "))
    print(f"Area: {base*height}")
    print(f"Perimeter: {2*(base+height)}")


def trapezoid():
    base1 = float(input("Base 1: "))
    base2 = float(input("Base 2: "))
    side1 = float(input("Side 1: "))
    side2 = float(input("Side 2: "))
    height = float(input("Height: "))
    print(f"Area: {(base1+base2)*height/2}")
    print(f"Perimeter: {side1 + side2 + base1 + base2}")


def pentagon():
    side1 = float(input("Side 1: "))
    side2 = float(input("Side 2: "))
    side3 = float(input("Side 3: "))
    side4 = float(input("Side 4: "))
    side5 = float(input("Side 5: "))
    apothem = float(input("Apothem: "))
    print(f"Area: {(side1 + side2 + side3 + side4 + side5)*apothem/2}")
    print(f"Perimeter: {side1 + side2 + side3 + side4 + side5}")


def hexagon():
    side = float(input("Side: "))
    apothem = float(input("Apothem: "))
    print(f"Area: { 6 * side * ( 3 * math.sqrt(3) / 2 )}")
    print(f"Perimeter: {6*side}")


def decagon():
    side = float(input("Side: "))
    apothem = float(input("Apothem: "))
    print(f"Area: {5/2 * math.power(side, 2) * (math.sqrt( 5 + 2 * math.sqrt(5)))}")
    print(f"Perimeter: {10*side}")


def geometrical_shapes_case(geometrical_shape):
    match geometrical_shape:
        case 0:
            return triangle()
        case 1:
            return square()
        case 2:
            return rectangle()
        case 3:
            return circle
        case 4:
            return rhombus()
        case 5:
            return parallelogram()
        case 6:
            return trapezoid()
        case 7:
            return pentagon()
        case 8:
            return hexagon()
        case 9:
            return decagon()
        case default:
            return "not valid :)"


if __name__ == "__main__":
    print("0 -> triangle")
    print("1 -> square")
    print("2 -> rectangle")
    print("3 -> circle")
    print("4 -> rhombus")
    print("5 -> parallelogram")
    print("6 -> trapezoid")
    print("7 -> pentagon")
    print("8 -> hexagon")
    print("9 -> decagon")

    shape = int(input("Choose your shape:"))
    geometrical_shapes_case(shape)
