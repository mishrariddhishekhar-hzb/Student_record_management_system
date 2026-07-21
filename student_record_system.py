import json
import os

DATA_FILE = "students.json"


# ---------------------------------------------------------------------
# File Handling Functions
# ---------------------------------------------------------------------

def load_data():
    
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: Could not read data file ({e}). Starting fresh.")
        return {}


def save_data(data):
    
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")


# ---------------------------------------------------------------------
# Core Operations
# ---------------------------------------------------------------------

def add_student(data):
    print("\n--- Add New Student ---")
    roll = input("Enter Roll Number: ").strip()

    if roll in data:
        print(f"A student with Roll Number '{roll}' already exists.")
        return

    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    course = input("Enter Course: ").strip()

    try:
        marks = float(input("Enter Marks/Percentage: ").strip())
    except ValueError:
        print("Invalid marks entered. Setting marks to 0.")
        marks = 0.0

    data[roll] = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    save_data(data)
    print(f"Student '{name}' added successfully.")


def view_students(data):
    print("\n--- All Student Records ---")
    if not data:
        print("No records found.")
        return

    print(f"{'Roll No':<10}{'Name':<20}{'Age':<6}{'Course':<15}{'Marks':<8}")
    print("-" * 60)
    for roll, info in data.items():
        print(f"{roll:<10}{info['name']:<20}{info['age']:<6}"
              f"{info['course']:<15}{info['marks']:<8}")


def search_student(data):
    print("\n--- Search Student ---")
    roll = input("Enter Roll Number to search: ").strip()

    if roll in data:
        info = data[roll]
        print(f"\nRoll No : {roll}")
        print(f"Name    : {info['name']}")
        print(f"Age     : {info['age']}")
        print(f"Course  : {info['course']}")
        print(f"Marks   : {info['marks']}")
    else:
        print(f"No student found with Roll Number '{roll}'.")


def update_student(data):
    print("\n--- Update Student ---")
    roll = input("Enter Roll Number to update: ").strip()

    if roll not in data:
        print(f"No student found with Roll Number '{roll}'.")
        return

    info = data[roll]
    print("Leave a field blank to keep its current value.")

    name = input(f"Name [{info['name']}]: ").strip()
    age = input(f"Age [{info['age']}]: ").strip()
    course = input(f"Course [{info['course']}]: ").strip()
    marks = input(f"Marks [{info['marks']}]: ").strip()

    if name:
        info["name"] = name
    if age:
        info["age"] = age
    if course:
        info["course"] = course
    if marks:
        try:
            info["marks"] = float(marks)
        except ValueError:
            print("Invalid marks entered. Keeping previous value.")

    data[roll] = info
    save_data(data)
    print("Student record updated successfully.")


def delete_student(data):
    print("\n--- Delete Student ---")
    roll = input("Enter Roll Number to delete: ").strip()

    if roll not in data:
        print(f"No student found with Roll Number '{roll}'.")
        return

    confirm = input(f"Are you sure you want to delete record '{roll}'? (y/n): ").strip().lower()
    if confirm == "y":
        removed = data.pop(roll)
        save_data(data)
        print(f"Student '{removed['name']}' deleted successfully.")
    else:
        print("Deletion cancelled.")


# ---------------------------------------------------------------------
# Menu / Main Program
# ---------------------------------------------------------------------

def show_menu():
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def main():
    data = load_data()

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            update_student(data)
        elif choice == "5":
            delete_student(data)
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()