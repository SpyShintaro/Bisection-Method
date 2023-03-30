"""
Bisect Method

Author: Jake Hickey
Date: idk dude it's 10:40pm and I'm on my fifth cup of tea
Description: A python program built for the CAS which calculates the solution of a graph via the bisection method
"""

def main(sol1, sol2, f):
    """
    Takes two points on a graph, as well as its function, to find the x-intercept
    """

    a = sol2
    b = sol1

    a_vals = []
    b_vals = []

    c = get_c(a, b)

    while b - a > 2 * 0.0001 or b - a < -2 * 0.0001:
        func_c = get_f(f, get_c(a, b))
        c = get_c(a, b)

        a_vals.append(a)
        b_vals.append(b)

        print(f"a: {a}, b: {b}, c: {c}, f(c): {func_c}")

        if func_c < 0:
            a = c
        else:
            b = c

    if validate_equation(c, f):
        return c
    else:
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
    return eval(func.replace("x", str(x)))

def get_c(a, b):
    """
    Finds the midpoint between points a and b
    """
    return (a + b) / 2

if __name__ == "__main__":
    get_func = input("Please input the function: ").replace("^", "**") # Needs to be used with get_f to actually do anything
    print(get_func)
    print(main(-1, -2, get_func))