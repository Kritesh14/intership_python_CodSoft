# Simple Calculator with Loop

while True:  # Loop to keep the calculator running
    try:
        # Take input from the user
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Ask the user to choose an operation
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter the number of the operation you want to perform (1/2/3/4): ")

        # Perform the operation based on user choice
        if choice == '1':
            result = num1 + num2
            operation = "Addition"
            symbol = "+"
        elif choice == '2':
            result = num1 - num2
            operation = "Subtraction"
            symbol = "-"
        elif choice == '3':
            result = num1 * num2
            operation = "Multiplication"
            symbol = "*"
        elif choice == '4':
            if num2 != 0:  # Check for division by zero
                result = num1 / num2
                operation = "Division"
                symbol = "/"
            else:
                print("\nError: Division by zero is not allowed!")
                continue  # Go back to start of loop
        else:
            print("\nInvalid operation! Please select a valid option.")
            continue  # Restart loop

        # Display the result
        print(f"\n{operation} Step by Step:")
        print(f"{num1} {symbol} {num2} = {result}")

    except ValueError:
        print("\nError: Please enter valid numeric values!")
        continue  # Restart loop

    # Ask if the user wants to perform another calculation
    again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
    if again != 'yes':
        print("\nThank you for using the calculator! Goodbye.")
        break  # Exit the loop if the user does not want to continue
