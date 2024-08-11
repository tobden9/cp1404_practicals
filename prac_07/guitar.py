import datetime

class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

def main():
    guitars = []

    print("My guitars!")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

if __name__ == "__main__":
    main()