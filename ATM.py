balance = 50000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        print(f"Your balance is: {balance}")
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print(f"Deposit successful. New balance: {balance}")
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"Withdrawal successful. New balance: {balance}")
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")