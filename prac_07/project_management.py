import csv
from project import Project
import datetime

def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file, delimiter='\t')
            for row in reader:
                project = Project(row['Name'], row['Start Date'], row['Priority'],
                                  row['Cost Estimate'], row['Completion Percent'])
                projects.append(project)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"Error loading projects: {e}")
    return projects

def save_projects(filename, projects):
    """Save the list of Project objects to a file."""
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter='\t')
            writer.writerow(['Name', 'Start Date', 'Priority', 'Cost Estimate', 'Completion Percent'])
            for project in projects:
                writer.writerow([project.name, project.start_date.strftime('%d/%m/%Y'), project.priority,
                                 project.cost_estimate, project.completion_percent])
    except Exception as e:
        print(f"Error saving projects: {e}")

def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete_projects = [p for p in projects if p.completion_percent < 100]
    completed_projects = [p for p in projects if p.completion_percent == 100]

    incomplete_projects.sort()
    completed_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")

def filter_projects_by_date(projects, date_string):
    """Filter and display projects that start after the given date."""
    try:
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = [p for p in projects if p.start_date > date]
        filtered_projects.sort(key=lambda p: p.start_date)
        for project in filtered_projects:
            print(f"  {project}")
    except ValueError:
        print("Invalid date format. Use dd/mm/yyyy.")

def add_project(projects):
    """Add a new project to the list."""
    print("Let's add a new project")
    try:
        name = input("Name: ")
        start_date = input("Start date (dd/mm/yyyy): ")
        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: "))
        completion_percent = int(input("Percent complete: "))

        project = Project(name, start_date, priority, cost_estimate, completion_percent)
        projects.append(project)
    except ValueError:
        print("Invalid input. Please enter numeric values for priority, cost estimate, and completion percentage.")

def update_project(projects):
    """Update an existing project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        choice = int(input("Project choice: "))
        project = projects[choice]

        print(f"{project}")
        new_completion = input("New Percentage: ")
        new_priority = input("New Priority: ")

        if new_completion:
            project.completion_percent = int(new_completion)
        if new_priority:
            project.priority = int(new_priority)
    except (IndexError, ValueError):
        print("Invalid choice or input.")

def main():
    filename = 'projects.txt'
    projects = load_projects(filename)

    print("Welcome to Pythonic Project Management")
    while True:
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").upper()

        if choice == 'L':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_string)
        elif choice == 'A':
            add_project(projects)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            if input("Would you like to save to projects.txt? (yes/no) ").lower() == 'yes':
                save_projects('projects.txt', projects)
            print("Thank you for using project management software.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()