def show_work(topic, steps):
    print("\n=== Showing Work ===")
    print(f"Topic: {topic}")
    for step in steps:
        print("- " + step)
    print("====================\n")

def solve_linear_equation():
    print("Solving ax + b = 0")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))

    if a == 0:
        if b == 0:
            show_work("Solve Linear", [
                "Equation is 0x + 0 = 0",
                "Any x works → Infinite solutions"
            ])
            print("Infinite solutions.")
        else:
            show_work("Solve Linear", [
                f"Equation is 0x + {b} = 0",
                "This is impossible → No solution"
            ])
            print("No solution.")
    else:
        x = -b / a
        show_work("Solve Linear", [
            f"Original: {a}x + {b} = 0",
            f"Subtract {b}: {a}x = {-b}",
            f"Divide by {a}: x = {-b}/{a}",
            f"Simplified: x = {x}"
        ])
        print(f"Solution: x = {x}")

def simplify_expression():
    expr = input("Enter an arithmetic expression (e.g., 2*(3+4) - 5): ")
    try:
        result = eval(expr)
        show_work("Simplify Expression", [
            f"Original: {expr}",
            f"Result: {result}"
        ])
        print(f"Simplified: {result}")
    except:
        print("Invalid expression.")

def factor_quadratic():
    print("Factoring ax² + bx + c")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    d = b**2 - 4*a*c
    steps = [
        f"Discriminant: D = b² - 4ac = {b}² - 4*{a}*{c} = {d}"
    ]

    if d < 0:
        steps.append("Since D < 0, cannot factor over real numbers.")
        show_work("Factor Quadratic", steps)
        print("Cannot factor over real numbers.")
    else:
        sqrt_d = d**0.5
        root1 = (-b + sqrt_d) / (2*a)
        root2 = (-b - sqrt_d) / (2*a)
        steps.extend([
            f"Roots: (-b ± √D) / 2a",
            f"Root 1: {root1}",
            f"Root 2: {root2}",
            f"Factored form: a(x - {root1})(x - {root2})"
        ])
        show_work("Factor Quadratic", steps)
        print(f"Factored form: a(x - {root1})(x - {root2})")

def derivative_polynomial():
    print("Derivative of polynomial ax^n + bx^m + ...")
    terms = input("Enter terms separated by + (example: 3x^2 + 2x + 5): ").replace(" ", "").split('+')
    derivative = []
    steps = []

    for term in terms:
        if 'x^' in term:
            coeff, power = term.split('x^')
            coeff = float(coeff) if coeff not in ['', '+'] else 1
            power = int(power)
            new_coeff = coeff * power
            new_power = power - 1
            steps.append(f"{term} → {new_coeff}x^{new_power}")
            if new_power == 0:
                derivative.append(f"{new_coeff}")
            elif new_power == 1:
                derivative.append(f"{new_coeff}x")
            else:
                derivative.append(f"{new_coeff}x^{new_power}")
        elif 'x' in term:
            coeff = float(term.replace('x', '')) if term.replace('x', '') not in ['', '+'] else 1
            steps.append(f"{term} → {coeff}")
            derivative.append(f"{coeff}")

    show_work("Derivative", steps)
    print("Derivative:", " + ".join(derivative))

def calculate_slope():
    print("Slope between (x1, y1) and (x2, y2)")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    steps = [
        f"Slope formula: (y2 - y1) / (x2 - x1)",
        f"Plug in: ({y2} - {y1}) / ({x2} - {x1})"
    ]

    if x2 - x1 == 0:
        steps.append("Division by zero → Slope is undefined (vertical line).")
        show_work("Slope", steps)
        print("Slope is undefined (vertical line).")
    else:
        slope = (y2 - y1) / (x2 - x1)
        steps.append(f"Simplified: Slope = {slope}")
        show_work("Slope", steps)
        print(f"Slope: {slope}")

def exit_program():
    print("Good luck with your homework!")

def invalid_choice():
    print("Invalid choice.")

def main():
    print("=== Math Homework Helper ===")
    print("""
1. Solve linear equation (ax + b = 0)
2. Simplify arithmetic expression
3. Factor quadratic (ax² + bx + c)
4. Derivative of polynomial
5. Find slope between 2 points
6. Exit
""")

    choice = input("Choose an option (1-6): ")

    if choice == '1':
        solve_linear_equation()
    elif choice == '2':
        simplify_expression()
    elif choice == '3':
        factor_quadratic()
    elif choice == '4':
        derivative_polynomial()
    elif choice == '5':
        calculate_slope()
    elif choice == '6':
        exit_program()
    else:
        invalid_choice()

main()