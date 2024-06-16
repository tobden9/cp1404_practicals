import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
QUICK_PICK_TOTAL = 6


def main():
    quick_pick = int(input("Enter how many quick picks to generate: "))
    for _ in range(quick_pick):
        numbers = generate_quick_pick()
        print(numbers)


def generate_quick_pick():
    number = []
    #generate random numbers for quick pick
    while len(number) < QUICK_PICK_TOTAL:
        new_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if new_number not in number:
            number.append(new_number)

    number.sort()
    return number


main()
