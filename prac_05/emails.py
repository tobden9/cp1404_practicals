def extract_name_from_email(email):

    name = email.split('@')[0].replace('.', ' ')
    return name.strip()

def collect_user_data():

    user_data = {}
    while True:
        email = input("Email: ").strip()
        if email == "":
            break

        # Extract the potential name from the email
        name_from_email = extract_name_from_email(email)

        # Display the potential name and ask for confirmation
        print(f"Based on your email, your name might be: {name_from_email}")
        use_extracted_name = input("Would you like to use this name? (Y/n) ").strip().lower()

        if use_extracted_name == 'n':
            name = input("Please enter your name: ").strip()
        else:
            name = name_from_email

        # Store the email and name in the dictionary
        user_data[email] = name

    return user_data


def main():
    # Collect user data
    user_data = collect_user_data()

    # Print out the emails and names
    for email, name in user_data.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()