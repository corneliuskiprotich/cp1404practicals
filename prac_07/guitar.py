class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance.

        name: str, the name of the guitar
        year: int, the year the guitar was made
        cost: float, the cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        """Return how old the guitar is in years."""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Return True if the guitar is 50 or more years old, False otherwise."""
        age = self.get_age(current_year)
        return age >= 50

if __name__ == "__main__":
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    current_year = 2024
    print(my_guitar)
    print(f"The guitar is {my_guitar.get_age(current_year)} years old.")

    # Checking if the guitar is vintage
    if my_guitar.is_vintage(current_year):
        print("This guitar is vintage!")
    else:
        print("This guitar is not vintage.")