"""
Bisect Method

Author: Jake Hickey
Date: 30/03/2023
Description: A python program built for the CAS which estimates the solution of a graph via the bisection method
"""

def main(sol1, sol2, f) -> float:
    """
    Estimates the x-intercept of a graph between two given end-points and returns the prediction if it is close enough to the x-axis
    """

    a = sol2
    b = sol1

    while b - a > 2 * 0.0001 or b - a < -2 * 0.0001: # Hardcoded accuracy tests
        c = get_c(a, b)
        func_c = get_f(f, c)

        print(f"a: {a:.6f}, b: {b:.6f}, c: {c:.6f}, f(c): {func_c:.6f}")

        if get_f(f, a) * func_c < 0:
            b = c
        else:
            a = c

        try:
            if validate_equation(f, c):
                return c # Returns the final midpoint value to the function call
        except RecursionError:
            print("Can't find x-intercept in given domain. Check boundary values and try again.")
            return None
    main(sol2, sol1, f) # I hope you liked that function, because if the domain is wrong, we're about to do it 999 more times


def validate_equation(func, x: float) -> bool:
    """
    Returns True if the given x-value correctly returns a y-value of 0 when put back into the equation.
    """
    if round(get_f(func, x), 1) == 0: # Margin of error (might need to fiddle with the number of d.p.)
        return True
    else:
        return

def get_f(func, x: float) -> float:
    """
    Converts input to a function in order to evaluate the given x value
    """

    format_func = func.replace("x", "(" + str(x) + ")") # Substitutes float x into the string (in brackets, to ensure the exponent is applied correctly)
    return eval(format_func) # Converts the text into a mathematical equation, and returns the answer


def get_c(a: float, b: float) -> float:
    """
    Finds the midpoint between given points a and b
    """

    return (a + b) / 2

if __name__ == "__main__": # You're about to witness perfection. Trust me.
    while True: ## Boomers: I hate my wife
        get_func = input("Please input the expression: ").replace("^", "**") # Gets a function as a string to be parsed in get_f
        try:
            get_f(get_func, 1)
            break
        except (SyntaxError, TypeError):
            print("Invalid function.")
    
    while True: ## Millenials: i hate my life
        try:
            a = float(input("What is the lower bound? ")) # Order of a and b don't matter, the program will try both
            break
        except ValueError:
            print("Please enter a floating point number (decimal)")
    
    while True: ## i am actually going to scream.
        try:
            b = float(input("What is the upper bound? "))
            break
        except ValueError:
            print("Please enter a floating point number (decimal)")

    solution = main(a, b, get_func) # how i didn't fail my applied computing sac is beyond me
    if solution:
        print(solution)