# Data Sharing
#================================
from ti_system import *
#================================

def main(sol1, sol2, f):
    """
    Takes two points on a graph, as well as its function, to find the x-intercept
    """

    a = sol2
    b = sol1

    a_vals = []
    f_a = []
    b_vals = []
    f_b = []
    c_vals = []
    f_c = []

    c = get_c(a, b)

    while b - a > 2 * 0.0001 or b - a < -2 * 0.0001:
        func_c = get_f(f, get_c(a, b))
        c = get_c(a, b)

        a_vals.append(a)
        f_a.append(get_f(f, a))
        b_vals.append(b)
        f_b.append(get_f(f, b))
        c_vals.append(c)
        f_c.append(func_c)

        if func_c < 0:
            a = c
        else:
            b = c
    try:
        if validate_equation(c, f):
            store_list("a", a_vals)
            store_list("f_a", f_a)
            store_list("b", b_vals)
            store_list("f_b", f_b)
            store_list("c", c_vals)
            store_list("f_c", f_c)
            return c
        else:
            main(sol2, sol1, f)
    except RecursionError:
        print("Can't find x-intercept of given domain. Check boundary values and try again.")
        return None
    
    main(sol2, sol1, f)

def validate_equation(x, func):
    """
    Returns x if the 'final answer' correctly returns a y-value of 0 when put back into the equation.
    """
    if round(get_f(func, x), 2) == 0:
        return x
    else:
        return

def get_f(func, x):
    """
    Evaluates inputted function for a given x value
    """
    return eval(func.replace("x", "(" + str(x) + ")"))

def get_c(a, b):
    """
    Finds the midpoint between points a and b
    """
    return (a + b) / 2

while True:
    get_func = input("Please input the expression: ").replace("^", "**")
    try:
        get_f(get_func, 1)
        break
    except (SyntaxError, TypeError):
        print("Invalid function.")

while True:
    try:
        a = float(input("What is the lower bound? "))
        break
    except ValueError:
        print("Please enter a floating point number (decimal)")

while True:
    try:
        b = float(input("What is the upper bound? "))
        break
    except ValueError:
        print("Please enter a floating point number (decimal)")

solution = main(a, b, get_func)
if solution:
    print("Done")
    print("x =", solution)