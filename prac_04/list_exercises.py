NUMBER = 5
def main():
    numbers = []
    for i in range(1, NUMBER+1):
        numbers_to_pick = int(input(" Pick a number: "))
        numbers.append(numbers_to_pick)

    # Output the first number
    print(f"The first number is {numbers[0]}")

    # Output the last number
    print(f"The last number is {numbers[-1]}")

    # Output the smallest number
    print(f"The smallest number is {min(numbers)}")

    # Output the largest number
    print(f"The largest number is {max(numbers)}")

    # Calculate the average of the numbers
    average = sum(numbers) / len(numbers)
    print(f"The average of the numbers is {average}")

main()


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

name = input("What is your name?: ")
if name in usernames:
    print("Access granted")
else:
    print("Access denied")