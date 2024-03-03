def read_data(filename):
    """
    Reads the Wimbledon data from the provided CSV file.
    Returns a list of lists containing the data.
    """
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            data.append(line.strip().split(","))
    return data


def count_champions(data):
    """
    Counts the number of times each player has won Wimbledon.
    Returns a dictionary with players as keys and their win count as values.
    """
    champions = {}
    for entry in data:
        player = entry[1]
        if player in champions:
            champions[player] += 1
        else:
            champions[player] = 1
    return champions


def get_countries(data):
    """
    Extracts the countries of the champions from the data.
    Returns a set of unique country names.
    """
    countries = set()
    for entry in data:
        country = entry[2]
        countries.add(country)
    return countries


def main():
    filename = "wimbledon.csv"
    data = read_data(filename)
    champions = count_champions(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for player, wins in champions.items():
        print(f"{player}: {wins} wins")

    print("\nCountries of Champions (in alphabetical order):")
    country_str = ", ".join(sorted(countries))
    print(country_str)


if __name__ == "__main__":
    main()
