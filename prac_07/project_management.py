import datetime
def load_projects(file_name):
    pass
def save_projects(file_name, projects):
    pass

def display_projects(projects):
    pass
def filter_projects_by_date(projects, date):
    pass
def add_new_project():
    pass

def update_project(projects):
    pass

def main():
    projects = load_projects("projects.txt")

    # Main menu loop
    while True:
        print("Welcome to Pythonic Project Management")
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").strip().lower()

        if choice == 'l':
            # Load projects from file
            file_name = input("Enter file name: ")
            projects = load_projects(file_name)
        elif choice == 's':
            # Save projects to file
            file_name = input("Enter file name: ")
            save_projects(file_name, projects)
        elif choice == 'd':
            # Display projects
            display_projects(projects)
        elif choice == 'f':
            # Filter projects by date
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            filtered_projects = filter_projects_by_date(projects, date)
            display_projects(filtered_projects)
        elif choice == 'a':
            # Add new project
            add_new_project()
        elif choice == 'u':
            # Update project
            update_project(projects)
        elif choice == 'q':
            # Quit
            save_choice = input("Would you like to save to projects.txt? ").strip().lower()
            if save_choice == 'yes' or save_choice == 'y':
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
