from guitar import Guitar

def get_guitar_details():
    """Prompt user to input guitar details."""
    name = input("Name: ")
    if not name:
        return None  # Return None if name is blank

    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    return Guitar(name, year, cost)

def main():
    print("My guitars!")
    guitars = []
    while True:
        print(f"Guitar {len(guitars) + 1}:")
        guitar = get_guitar_details()
        if guitar is None:
            break
        guitars.append(guitar)
        print(f"{guitar} added.")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(2024) else ""
        print(f"Guitar {i}: {guitar.name:<20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

if __name__ == "__main__":
    main()
