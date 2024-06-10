#CP1404/CP5632 - Practical

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("denominator cannot be zero!")

    elif numerator == 0:
        print("numerator cannot be zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

"""
Answer the following questions:
1. When will a ValueError occur?
Ans: Value error will occur when the user inputs a string or float value.

2. When will a ZeroDivisionError occur?
Ans: When user inputs 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Ans: Yes we can use conditional statement to avoid ZeroDivisionError.
"""

