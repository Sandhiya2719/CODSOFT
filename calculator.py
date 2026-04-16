first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

print("\nChoose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4): ")

if choice == '1':
    result = first_number + second_number
    print("Result is:", result)

elif choice == '2':
    result = first_number - second_number
    print("Result is:", result)

elif choice == '3':
    result = first_number * second_number
    print("Result is:", result)

elif choice == '4':
    if second_number != 0:
        result = first_number / second_number
        print("Result is:", result)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid choice, please try again")
