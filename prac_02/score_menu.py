def main():
    MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""

    score = get_valid_score()
    while True:
        print(MENU)
        choice = input("Enter your choice: ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell!")
            break
        else:
            print("Invalid choice. Please choose again.")

#Getting valid score
def get_valid_score():
    while True:
        try:
            score = int(input("Enter a score between 0 and 100: "))
            if 0 <= score <= 100:
                print("Valid score")
                return score
            else:
                print("Invalid score. It must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

#Results
def print_result(score):
    if score < 0:
        print ("Invalid score")
    elif score > 100:
        print ("Invalid score")
    elif score > 50:
        print ("Passable")
    elif score > 90:
        print ("Excellent")
    else:
        print ("Bad")
    print(f"The result for a score of {score} is {print_result}.")


def show_stars(score):
    print("*" * score)


if __name__ == "__main__":
    main()
