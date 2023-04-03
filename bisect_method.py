"""
Bisect Method

Author: Jake Hickey
Date: idk dude it's 10:40pm and I'm on my fifth cup of tea
Description: A python program built for the CAS which estimates the solution of a graph via the bisection method
"""

def main(sol1, sol2, f):
    """
    Estimates the x-intercept of a graph between two given end-points and returns the prediction if it is close enough to the x-axis
    """

    a = sol2
    b = sol1

    a_vals = []
    b_vals = []

    c = get_c(a, b)
    try:
        while b - a > 2 * 0.0001 or b - a < -2 * 0.0001:
            func_c = get_f(f, c)
            c = get_c(a, b)

            a_vals.append(a)
            b_vals.append(b)

            print(f"a: {a}, b: {b}, c: {c}, f(c): {func_c}")

            if func_c < 0:
                a = c
            else:
                b = c
    except RecursionError:
        print("Cannot find x-intercept within endpoints given. Check boundary values and try again.")
    
    if validate_equation(c, f):
        return c # Returns the final midpoint value to the function call
    else:
        main(sol2, sol1, f)

def validate_equation(x, func):
    """
    Returns True if the given x-value correctly returns a y-value of 0 when put back into the equation.
    """
    if round(get_f(func, x), 1) == 0: # Margin of error (might need to fiddle with the number of d.p.)
        return True
    else:
        return

def get_f(func, x):
    """
    Converts input to a function in order to evaluate the given x value
    """
    format_func = func.replace("x", "(" + str(x) + ")") # Substitutes float x into the string (in brackets, to ensure the exponent is applied correctly)
    print(format_func)
    return eval(format_func) # Converts the text into a mathematical equation, and returns the answer

def get_c(a, b):
    """
    Finds the midpoint between given points a and b
    """
    return (a + b) / 2

if __name__ == "__main__":
    get_func = input("Please input the function: ").replace("^", "**") # Needs to be used with get_f to actually do anything
    a = float(input("What is the lower bound? ")) # The order of these variables don't actually matter, the program will try both
    b = float(input("What is the upper bound? "))
    print(main(a, b, get_func))