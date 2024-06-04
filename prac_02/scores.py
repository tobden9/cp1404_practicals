import random
def result(score):
    if score < 0:
        return("Invalid score")
    elif score > 100:
        return("Invalid score")
    elif score > 50:
        return("Passable")
    elif score > 90:
        return("Excellent")
    else:
        return("Bad")

def main():
    score = float(input("Enter score: "))
    print(result(score))
    random_score = random.randint(1, 10)
    print("Random Score: ", random_score)
    print(result(random_score))

main()