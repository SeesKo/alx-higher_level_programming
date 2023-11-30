#!/usr/bin/python3
import calculator_1 as calc

a = 10
b = 5

if __name__ == "__main__":
    result = calc.add(a, b)
    print("{} + {} = {}".format(a, b, result))
    result = calc.sub(a, b)
    print("{} - {} = {}".format(a, b, result))
    result = calc.mul(a, b)
    print("{} * {} = {}".format(a, b, result))
    result = calc.div(a, b)
    print("{} / {} = {}".format(a, b, result))
