import csv

def read_csv(filename):
    """Reads the CSV file and returns a list of dictionaries representing each row."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            data.append(row)
    return data

def count_champions(data):
    """Counts the number of wins for each champion."""
    champion_counts = {}
    for row in data:
        champion = row['Champion']
        if champion in champion_counts:
            champion_counts[champion] += 1
        else:
            champion_counts[champion] = 1
    return champion_counts

def get_countries(data):
    """Collects unique countries of the champions."""
    countries = set()
    for row in data:
        country = row['Country']
        countries.add(country)
    return sorted(countries)

def display_results(champion_counts, countries):
    """Displays the processed information."""
    print("Champions and their number of wins:")
    for champion, count in champion_counts.items():
        print(f"{champion}: {count} wins")

    countries_str = ", ".join(countries)
    print("\nCountries of the champions:")
    print(countries_str)

def main():
    filename = "wimbledon.csv"
    data = read_csv(filename)
    champion_counts = count_champions(data)
    countries = get_countries(data)
    display_results(champion_counts, countries)


main()