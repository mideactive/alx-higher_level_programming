#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    add1 = add(a, b)
    sub1 = sub(a, b)
    mul1 = mul(a, b)
    div1 = int(div(a, b))
    print("{} + {} = {}".format(a, b, add1), end="\n")
    print("{} + {} = {}".format(a, b, sub1), end="\n")
    print("{} + {} = {}".format(a, b, mul1), end="\n")
    print("{} + {} = {}".format(a, b, div1), end="\n")
