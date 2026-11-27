from datetime import datetime
import operator

# Supported operations
operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def calculator_tool():
    try:
        num1 = float(input("First Number: "))
        op = input("Operator (+, -, *, /): ")
        num2 = float(input("Second Number: "))

        if op not in operations:
            return "Invalid operator."

        result = operations[op](num1, num2)
        return f"Result: {result}"

    except ZeroDivisionError:
        return "Cannot divide by zero."

    except ValueError:
        return "Please enter valid numbers."

def datetime_tool():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def create_file_tool():
    filename = input("Enter file name: ")
    content = input("Enter file content: ")

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

        return f"File '{filename}' created successfully."

    except Exception as e:
        return f"Error: {e}"

def main():

    print("==== Tool Using AI Agent ====")

    while True:

        print("\nAvailable Tools")
        print("1. Calculator")
        print("2. Date and Time")
        print("3. Create File")
        print("4. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            print(calculator_tool())

        elif choice == "2":
            print(datetime_tool())

        elif choice == "3":
            print(create_file_tool())

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
