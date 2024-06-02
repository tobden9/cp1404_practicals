def get_valid_number_of_items():
    while True:
        try:
            num_items = int(input("Number of items: "))
            if num_items < 0:
                print("Invalid number of items!")
            else:
                return num_items
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_total_price(num_items):
    total_price = 0
    for i in range(num_items):
        item_price = float(input("Price of item: "))
        total_price += item_price

    if total_price > 100:
        total_price *= 0.9  # Apply 10% discount

    return total_price


def main():
    num_items = get_valid_number_of_items()
    total_price = calculate_total_price(num_items)
    print(f"Total price for {num_items} items is ${total_price:.2f}")


if __name__ == "__main__":
    main()
