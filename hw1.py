def my_func(x1, x2, x3):
    try:
        x1 = float(x1)
        x2 = float(x2)
        x3 = float(x3)
    except:
        print("Error: parameters should be float")
        return
    if (x1 + x2 + x3 == 0):
        return "Not a number – denominator equals zero"
    return ((x1 + x2 + x3) * (x2 + x3) * x3) / (x1 + x2 + x3)


# print(my_func(1, 3, 7))
# print(my_func(-1.5, 3, -2.5))  # accepts float
# print(my_func(-1.5, 3, -1.5))  # denominator equals zero
# print(my_func(-1.5, 'six', -1.5))#not a float


def convert(hours, minutes=None):
    if minutes == None:
        try:
            hours = float(hours)
            if (hours < 0):
                print("Input error!")
            else:
                return hours * 60 * 60
        except:
            print("Error: parameter should be float")

    else:
        if not isinstance(hours, int) or not isinstance(minutes, int):
            print("Error: parameters should be int")
            return
        else:
            if (hours < 0 or minutes < 0):
                print("Input error!")
                return
            else:
                return hours * 60 * 60 + minutes * 60

# print(convert(1.75))
# print(convert(1.75,3))
# print(convert(1,3))
# print(convert(-1.75))
# print(convert(1,-3))
# print(convert('1',3))
