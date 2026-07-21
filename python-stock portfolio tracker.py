portfolio = {}

while True:
    print("\n===== Stock Portfolio Tracker =====")
    print("1. Add Stock")
    print("2. Remove Stock")
    print("3. View Portfolio")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter stock name: ").upper()

        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per share: "))

        portfolio[name] = {
            "quantity": quantity,
            "price": price
        }

        print(f"{name} added successfully!")

    elif choice == "2":
        name = input("Enter stock name to remove: ").upper()

        if name in portfolio:
            del portfolio[name]
            print(f"{name} removed successfully!")
        else:
            print("Stock not found!")

    elif choice == "3":
        if not portfolio:
            print("Portfolio is empty.")
        else:
            print("\n----- Your Portfolio -----")
            total_value = 0

            for name, details in portfolio.items():
                value = details["quantity"] * details["price"]
                total_value += value

                print(
                    f"{name}: {details['quantity']} shares × ${details['price']:.2f} = ${value:.2f}"
                )

            print(f"\nTotal Portfolio Value = ${total_value:.2f}")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")
