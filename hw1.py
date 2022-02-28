def my_func(x1, x2, x3):
    if not isinstance(x1, float) or not isinstance(x2, float) or not isinstance(x3, float):
        print("Error: parameters should be float")
        return
    if (x1 + x2 + x3 == 0):
        return "Not a number – denominator equals zero"
    return ((x1 + x2 + x3) * (x2 + x3) * x3) / (x1 + x2 + x3)


# print(my_func(1., 3., 7.))
# print(my_func(-1.5, 3, -2.5))  # dont accepts int
# print(my_func(-1.5, 3., -1.5))  # denominator equals zero
# print(my_func(-1.5, 'six', -1.5))  # not a float


def convert(hours, minutes=None):
    hour_int_float = isinstance(hours, int) or isinstance(hours, float)
    minutes_int_float = isinstance(minutes, int) or isinstance(minutes, float)

    if minutes == None and hour_int_float:
        if (hours < 0):
            print("Input error!")
        else:
            return hours * 60 * 60.

    elif hour_int_float and minutes_int_float:
        if (hours < 0 or minutes < 0):
            print("Input error!")
            return
        else:
            return hours * 60 * 60. + minutes * 60


    else:
        print("The function only accept int or float parameters")
        return

# print(convert(1.75))
# print(convert(1.75,3))
# print(convert(1,3))
# print(convert(-1.75))
# print(convert(1,-3))
# print(convert('1',3))
