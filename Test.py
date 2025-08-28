def add_two_numbers():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {num1 + num2}")
        except ValueError:
            print("Please enter valid numbers.")
            continue

        choice = input("Add two more numbers? (y/n): ").strip().lower()
        if choice != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    add_two_numbers()