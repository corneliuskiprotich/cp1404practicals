"""
CP1404 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    data = get_data()
    for subject, lecturer, num_students in data:
        print(f"{subject} is taught by {lecturer} and has {num_students} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subjects.append(tuple(parts))
    input_file.close()
    return subjects


main()