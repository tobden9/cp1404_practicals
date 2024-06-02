password_min = 8
def main():
    password = input("Enter a password: ")
    if len(password) < password_min:
        print(f"Password needs to be at least {password_min} letters.")
    else:
        print("*" * len(password))

main()