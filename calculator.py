def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def get_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num < 0:
                print("Please enter a positive integer.")
                continue
            return num
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("Welcome to Simple Calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")

    while True:
        choice = input("Enter your choice (1/2/3): ")

        if choice in ('1', '2', '3'):
            num1 = get_positive_integer("Enter the first positive integer: ")
            num2 = get_positive_integer("Enter the second positive integer: ")

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

        another_calculation = input("Do you want to perform another calculation? (y/n): ")
        if another_calculation.lower() != "y":
            print("Thank you for using the Calculator!")
            break

if __name__ == "__main__":
    main()