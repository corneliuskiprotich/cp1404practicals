def extract_name(email):
    """
    Extracts the name from the email address.
    """
    name = email.split('@')[0]
    # Split the name by dots or underscores and capitalize each part
    name_parts = [part.capitalize() for part in name.split('.') if part != '']
    # Join the parts with a space
    return ' '.join(name_parts)


def main():
    user_data = {}

    while True:
        email = input("Email: ").strip()
        if email == "":
            break

        name = extract_name(email)
        name_confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if name_confirmation == "" or name_confirmation == "y":
            user_data[email] = name
        else:
            name = input("Name: ").strip().title()
            user_data[email] = name

    print("\nUser data:")
    for email, name in user_data.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
