from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def print_taxis(taxis):
    """Print out the list of taxis with their details."""
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Prompt user to choose a taxi from the list."""
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input")
        return None


def drive_taxi(taxi):
    """Prompt user to enter distance and drive the chosen taxi."""
    try:
        distance = float(input("Drive how far? "))
        cost = taxi.drive(distance)
        fare = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${fare:.2f}")
        return fare
    except ValueError:
        print("Invalid distance")
        return 0


def taxi_simulator():
    taxis = [
        Taxi("Prius", 100, 1.23),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    total_bill = 0

    while True:
        print("\nLet's drive!")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == 'q':
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            break

        elif choice == 'c':
            print_taxis(taxis)
            current_taxi = choose_taxi(taxis)
            if current_taxi is not None:
                print(f"Bill to date: ${total_bill:.2f}")

        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                trip_cost = drive_taxi(current_taxi)
                total_bill += trip_cost
                print(f"Bill to date: ${total_bill:.2f}")

        else:
            print("Invalid option")
            print(f"Bill to date: ${total_bill:.2f}")


if __name__ == "__main__":
    taxi_simulator()