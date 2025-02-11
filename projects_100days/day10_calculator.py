def add(n1, n2):
    return n1+ n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return n1 / n2

def operation_choice():
    #Store the users choice
    symbol_choice = input("""
+
-
*
/ 
Pick an operation: """)
    if symbol_choice in ["+", "-", "*", "/"]:
        return symbol_choice
    print("Invalid operation. Please choose from '+', '-', '*', or '/'.")

def user_input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
def user_input_n1():
    # Ask user to enter first number
    try:
        first_num = int(input("Enter first number: "))
        return first_num
    except ValueError:
        print("Invalid input, enter a number")
    

def user_input_n2():
        # Ask user to enter first number
    try:
        second_num = int(input("Enter first number: "))
        return second_num
    except ValueError:
        print("Invalid input, enter a number")

#Storing each function as a value
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}


#Program theme
print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|""")
# Main loop for the calculator
while True:
    n1 = user_input_number("Enter first number: ")  # Ask for the first number

    while True:
        symbol = operation_choice()  # Ask user to select an operator
        n2 = user_input_number("Enter second number: ")  # Ask for the second number
        
        result = operations[symbol](n1, n2)  # Perform the calculation

        if result is None:  # Handle division by zero case
            continue  # Skip to the next iteration and ask for a new second number

        # Display the calculation result
        print(f"{n1} {symbol} {n2} = {result}")

        # Ask if the user wants to continue with the current result or start over
        user_input = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if user_input == "y":
            n1 = result  # Use the result as the first number in the next calculation
        else:
            break  # Exit inner loop and start a new calculation from scratch
        