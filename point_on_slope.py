def inputs():
    point_1 = input("Enter 2 numbers separated by a comma: ")
    point_2 = input("Enter another 2 numbers separated by a comma: ")
    point_1_tuple = (point_1.split(","))
    point_2_tuple = (point_2.split(","))
    x1 = int(point_1_tuple[0])
    y1 = int(point_1_tuple[1])
    x2 = int(point_2_tuple[0])
    y2 = int(point_2_tuple[1])
    new_x = int(input("Enter a number: "))
    return x1, y1, x2, y2, new_x


def calculate_y(x1, y1, x2, y2, new_x):
    slope = (y2 - y1) / (x2 - x1)
    constant = y1 - (slope * x1)
    new_y = (new_x * slope) + constant
    return new_y


def program_driver():
    x1, y1, x2, y2, new_x = inputs()
    y, x = calculate_y(x1, y1, x2, y2, new_x)
    print("With an x value of {}, the corresponding y value on the line is {}".format(x, y))


if __name__ == '__main__':
    program_driver()
