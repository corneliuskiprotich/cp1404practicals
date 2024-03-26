from guitar import Guitar

def load_guitars(file_name):
    guitars = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 3:
                    name, year, cost = data
                    guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    return guitars

def save_guitars(file_name, guitars):
    with open(file_name, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

def display_guitars(guitars):
    if guitars:
        print("List of Guitars:")
        for index, guitar in enumerate(guitars, 1):
            print(f"{index}. {guitar}")
    else:
        print("No guitars found.")

def add_new_guitar(guitars):
    name = input("Enter guitar name: ")
    year = int(input("Enter year made: "))
    cost = float(input("Enter cost: "))
    guitars.append(Guitar(name, year, cost))

