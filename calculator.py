def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two numbers, handles division by zero."""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def calculator():
    """Main function for the calculator application."""
    print("\n--- SIMPLE PYTHON CALCULATOR ---")
    print("Available Operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
    print("--------------------------------")

    while True:
        try:
            # [cite_start]Prompt the user to input an operation choice [cite: 45]
            choice = input("Enter operation number (1/2/3/4/5): ")
            
            if choice == '5':
                print("Exiting Calculator. Goodbye!")
                break

            if choice in ('1', '2', '3', '4'):
                # [cite_start]Prompt the user to input two numbers [cite: 45]
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = None
                operation_symbol = ""

                # [cite_start]Perform the calculation based on the choice [cite: 46]
                if choice == '1':
                    result = add(num1, num2)
                    operation_symbol = "+"
                elif choice == '2':
                    result = subtract(num1, num2)
                    operation_symbol = "-"
                elif choice == '3':
                    result = multiply(num1, num2)
                    operation_symbol = "*"
                elif choice == '4':
                    result = divide(num1, num2)
                    operation_symbol = "/"
                
                # [cite_start]Display the result [cite: 46]
                print(f"\nResult: {num1} {operation_symbol} {num2} = {result}")
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculator()