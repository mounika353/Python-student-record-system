"""
Student Record System — A Command-Line Python Application
==========================================================
This program manages student records using all Module 1 concepts:
  - Variables & Data Types (str, int, float, bool)
  - Operators (arithmetic, comparison, logical)
  - Strings & String Methods
  - Lists, Tuples, Dictionaries, Sets
  - Control Flow (if / elif / else)
  - Loops (for, while)
  - Functions
  - File I/O (JSON)
  - Exception Handling (try / except / finally)

Author : [Your Name]
Date   : June 2026
"""

import json   # For saving/loading records to a JSON file
import os     # For checking if the data file exists


# ──────────────────────────────────────────────
# CONSTANTS (Variables & Data Types)
# ──────────────────────────────────────────────
DATA_FILE = "students.json"          # str — path to the data file
MAX_GPA = 4.0                        # float — maximum allowed GPA
MIN_GPA = 0.0                        # float — minimum allowed GPA
MIN_AGE = 16                         # int — minimum student age
MAX_AGE = 100                        # int — maximum student age
PROGRAM_TITLE = "Student Record System"  # str — application title

# Tuple — available courses (immutable data)
# Each course is a tuple of (course_code, course_name, credits)
AVAILABLE_COURSES = (
    ("CS101", "Introduction to Computer Science", 3),
    ("MA201", "Calculus II", 4),
    ("PH101", "Physics I", 3),
    ("EN101", "English Composition", 2),
    ("HI150", "World History", 3),
    ("BIO101", "Biology Fundamentals", 3),
)


# ──────────────────────────────────────────────
# FILE I/O FUNCTIONS
# ──────────────────────────────────────────────

def load_students():
    """
    Load student records from the JSON data file.

    Demonstrates: File I/O (reading), Exception Handling, Lists, Dictionaries.

    Returns:
        list: A list of student dictionaries. Returns an empty list if the
              file does not exist or contains invalid JSON.
    """
    # Check if file exists before trying to read (os module)
    if not os.path.exists(DATA_FILE):
        print("[INFO] No existing data file found. Starting with empty records.")
        return []  # Return an empty list

    try:
        # File I/O — open and read the JSON file
        with open(DATA_FILE, "r") as file:
            data = json.load(file)  # Parse JSON into Python objects
            print(f"[INFO] Loaded {len(data)} student record(s) from '{DATA_FILE}'.")
            return data
    except json.JSONDecodeError:
        # Exception Handling — handle corrupted JSON gracefully
        print("[WARNING] Data file is corrupted. Starting with empty records.")
        return []
    except IOError as e:
        # Exception Handling — handle file read errors
        print(f"[ERROR] Could not read data file: {e}")
        return []


def save_students(students):
    """
    Save student records to the JSON data file.

    Demonstrates: File I/O (writing), Exception Handling.

    Args:
        students (list): The list of student dictionaries to save.
    """
    try:
        # File I/O — open and write the JSON file with pretty formatting
        with open(DATA_FILE, "w") as file:
            json.dump(students, file, indent=4)
        print(f"[INFO] Records saved successfully to '{DATA_FILE}'.")
    except IOError as e:
        # Exception Handling — handle file write errors
        print(f"[ERROR] Could not save data: {e}")


# ──────────────────────────────────────────────
# ID GENERATION FUNCTION
# ──────────────────────────────────────────────

def generate_id(students):
    """
    Generate the next unique student ID.

    Demonstrates: Lists, Arithmetic Operators, Control Flow.

    Args:
        students (list): The current list of student records.

    Returns:
        int: The next available student ID.
    """
    if len(students) == 0:  # Comparison operator
        return 1
    else:
        # Arithmetic operator (+) to increment the max existing ID
        max_id = max(student["id"] for student in students)  # Dictionary access
        return max_id + 1


# ──────────────────────────────────────────────
# INPUT VALIDATION HELPERS
# ──────────────────────────────────────────────

def get_valid_name():
    """
    Prompt the user for a valid student name.

    Demonstrates: Strings & String Methods, While Loop, Control Flow.

    Returns:
        str: A properly formatted student name.
    """
    while True:  # While loop — keep asking until valid input
        name = input("  Enter student name: ").strip()  # String method: strip()

        # Control flow — validate the name
        if len(name) == 0:
            print("  [ERROR] Name cannot be empty. Please try again.")
        elif not name.replace(" ", "").isalpha():  # String method: isalpha()
            print("  [ERROR] Name must contain only letters and spaces.")
        else:
            # String method: title() — capitalize each word
            return name.title()


def get_valid_age():
    """
    Prompt the user for a valid student age.

    Demonstrates: Exception Handling, Comparison Operators, While Loop.

    Returns:
        int: A valid student age.
    """
    while True:
        try:
            age = int(input("  Enter student age: "))  # Type conversion to int

            # Comparison operators and logical operator (and)
            if age >= MIN_AGE and age <= MAX_AGE:
                return age
            else:
                print(f"  [ERROR] Age must be between {MIN_AGE} and {MAX_AGE}.")
        except ValueError:
            # Exception Handling — non-integer input
            print("  [ERROR] Please enter a valid whole number.")


def get_valid_gpa():
    """
    Prompt the user for a valid GPA.

    Demonstrates: Exception Handling, Comparison Operators, Float data type.

    Returns:
        float: A valid GPA value.
    """
    while True:
        try:
            gpa = float(input("  Enter GPA (0.0 - 4.0): "))  # Type conversion to float

            # Comparison operators
            if gpa < MIN_GPA or gpa > MAX_GPA:  # Logical operator: or
                print(f"  [ERROR] GPA must be between {MIN_GPA} and {MAX_GPA}.")
            else:
                return round(gpa, 2)  # Round to 2 decimal places
        except ValueError:
            print("  [ERROR] Please enter a valid number (e.g., 3.50).")


def get_active_status():
    """
    Prompt the user for the student's active/inactive status.

    Demonstrates: Boolean data type, String Methods, Control Flow.

    Returns:
        bool: True if the student is active, False otherwise.
    """
    while True:
        status = input("  Is the student currently active? (yes/no): ").strip().lower()

        # Control flow with string comparison
        if status in ("yes", "y"):
            return True   # Boolean — True
        elif status in ("no", "n"):
            return False  # Boolean — False
        else:
            print("  [ERROR] Please enter 'yes' or 'no'.")


def get_subjects():
    """
    Prompt the user to enter subjects for a student.

    Demonstrates: Sets (uniqueness), While Loop, String Methods.

    Returns:
        set: A set of unique subject names.
    """
    subjects = set()  # Set — automatically handles duplicate subjects
    print("  Enter subjects (type 'done' when finished):")

    while True:
        subject = input("    Subject: ").strip().title()  # String methods: strip(), title()

        if subject.lower() == "done":  # String method: lower()
            if len(subjects) == 0:  # Comparison operator
                print("    [ERROR] Please enter at least one subject.")
            else:
                break  # Exit the while loop
        elif subject == "":
            print("    [ERROR] Subject cannot be empty.")
        elif subject in subjects:  # Set membership check
            print(f"    [INFO] '{subject}' is already added (sets prevent duplicates).")
        else:
            subjects.add(subject)  # Set method: add()
            print(f"    [OK] Added '{subject}'. Total subjects: {len(subjects)}")

    return subjects


def get_courses():
    """
    Let the user choose courses from the available list.

    Demonstrates: Tuples (immutable data), For Loop, Lists, Control Flow.

    Returns:
        list: A list of selected course tuples.
    """
    selected_courses = []  # List to hold chosen courses

    print("\n  Available Courses:")
    # For loop — iterate over the tuple of available courses
    for index, course in enumerate(AVAILABLE_COURSES, start=1):
        code, name, credits = course  # Tuple unpacking
        print(f"    {index}. {code} — {name} ({credits} credits)")

    print("  Enter course numbers separated by commas (e.g., 1,3,5):")

    while True:
        try:
            choices = input("    Your choices: ").strip()

            if not choices:
                print("    [ERROR] Please select at least one course.")
                continue

            # String method: split() and list processing
            choice_list = choices.split(",")

            for choice in choice_list:
                num = int(choice.strip())  # String method: strip(), type conversion

                # Comparison operators — validate range
                if num < 1 or num > len(AVAILABLE_COURSES):
                    print(f"    [WARNING] Invalid choice '{num}' — skipped.")
                else:
                    course_tuple = AVAILABLE_COURSES[num - 1]  # Access tuple by index
                    if course_tuple not in selected_courses:  # Avoid duplicates
                        selected_courses.append(course_tuple)  # List method: append()

            if len(selected_courses) > 0:  # Comparison operator
                # For loop to display selections
                print("    Selected courses:")
                for c in selected_courses:
                    print(f"      • {c[0]} — {c[1]} ({c[2]} credits)")
                break
            else:
                print("    [ERROR] No valid courses selected. Try again.")

        except ValueError:
            print("    [ERROR] Please enter numbers separated by commas (e.g., 1,3,5).")

    return selected_courses


# ──────────────────────────────────────────────
# CORE FEATURE FUNCTIONS
# ──────────────────────────────────────────────

def add_student(students):
    """
    Add a new student record to the system.

    Demonstrates: Dictionaries (creating), Functions, all input helpers.

    Args:
        students (list): The list of student records (modified in-place).
    """
    print("\n" + "=" * 50)
    print("  📝  ADD NEW STUDENT")
    print("=" * 50)

    # Collect validated inputs using helper functions
    name = get_valid_name()
    age = get_valid_age()
    gpa = get_valid_gpa()
    active = get_active_status()
    subjects = get_subjects()
    courses = get_courses()

    # Dictionary — create a student record with key-value pairs
    student = {
        "id": generate_id(students),       # int
        "name": name,                       # str
        "age": age,                         # int
        "gpa": gpa,                         # float
        "active": active,                   # bool
        "subjects": list(subjects),         # Convert set → list for JSON
        "courses": [list(c) for c in courses]  # Convert tuples → lists for JSON
    }

    students.append(student)  # List method: append()
    save_students(students)    # Persist to file

    print(f"\n  ✅ Student '{student['name']}' added successfully with ID {student['id']}!")


def view_all_students(students):
    """
    Display all student records in a formatted table.

    Demonstrates: For Loop, String Formatting, Control Flow, Dictionary access.

    Args:
        students (list): The list of student records.
    """
    print("\n" + "=" * 80)
    print("  📋  ALL STUDENT RECORDS")
    print("=" * 80)

    # Control flow — check if there are any records
    if len(students) == 0:
        print("  No student records found. Add a student first!")
        return

    # Header row with string formatting
    print(f"  {'ID':<5} {'Name':<25} {'Age':<6} {'GPA':<7} {'Status':<10} {'Subjects'}")
    print("  " + "-" * 75)

    # For loop — iterate through each student record
    for student in students:
        # Dictionary access using keys
        student_id = student["id"]
        name = student["name"]
        age = student["age"]
        gpa = student["gpa"]

        # Conditional expression (ternary) — convert bool to readable string
        status = "Active" if student["active"] else "Inactive"

        # String method: join() — combine list items into a string
        subjects = ", ".join(student["subjects"])

        # String formatting with alignment
        print(f"  {student_id:<5} {name:<25} {age:<6} {gpa:<7.2f} {status:<10} {subjects}")

    print("  " + "-" * 75)
    print(f"  Total Records: {len(students)}")  # len() function


def search_student(students):
    """
    Search for students by name using partial, case-insensitive matching.

    Demonstrates: String Methods (lower, find/in), For Loop, Lists, Control Flow.

    Args:
        students (list): The list of student records.
    """
    print("\n" + "=" * 50)
    print("  🔍  SEARCH STUDENT")
    print("=" * 50)

    if len(students) == 0:
        print("  No records to search. Add a student first!")
        return

    query = input("  Enter name to search: ").strip().lower()  # String methods

    if not query:
        print("  [ERROR] Search query cannot be empty.")
        return

    # List to store matching results
    results = []

    # For loop — search through all students
    for student in students:
        # String method: lower() for case-insensitive comparison
        # 'in' operator for partial matching (substring check)
        if query in student["name"].lower():
            results.append(student)  # List method: append()

    # Control flow — display results or not-found message
    if len(results) > 0:  # Comparison operator
        print(f"\n  Found {len(results)} matching record(s):\n")
        for s in results:
            status = "Active" if s["active"] else "Inactive"
            subjects_str = ", ".join(s["subjects"])  # String method: join()
            print(f"    ID: {s['id']}  |  Name: {s['name']}  |  Age: {s['age']}  "
                  f"|  GPA: {s['gpa']:.2f}  |  Status: {status}")
            print(f"    Subjects: {subjects_str}")

            # For loop — display courses (tuple data)
            print(f"    Courses:")
            for course in s["courses"]:
                print(f"      • {course[0]} — {course[1]} ({course[2]} credits)")
            print()
    else:
        print(f"  No students found matching '{query}'.")


def update_student(students):
    """
    Update an existing student's information.

    Demonstrates: Dictionary (modifying), Exception Handling, Control Flow, While Loop.

    Args:
        students (list): The list of student records (modified in-place).
    """
    print("\n" + "=" * 50)
    print("  ✏️  UPDATE STUDENT")
    print("=" * 50)

    if len(students) == 0:
        print("  No records to update. Add a student first!")
        return

    try:
        student_id = int(input("  Enter Student ID to update: "))
    except ValueError:
        print("  [ERROR] Invalid ID. Please enter a number.")
        return

    # Search for the student by ID using a for loop
    target = None  # Variable initialized to None
    for student in students:
        if student["id"] == student_id:  # Comparison operator
            target = student
            break  # Exit the for loop early

    # Control flow — check if student was found
    if target is None:
        print(f"  Student with ID {student_id} not found.")
        return

    print(f"\n  Current record for '{target['name']}':")
    print(f"    1. Name:     {target['name']}")
    print(f"    2. Age:      {target['age']}")
    print(f"    3. GPA:      {target['gpa']}")
    print(f"    4. Status:   {'Active' if target['active'] else 'Inactive'}")
    print(f"    5. Subjects: {', '.join(target['subjects'])}")
    print(f"    6. Courses")
    print(f"    0. Cancel")

    try:
        field_choice = int(input("\n  Select field to update (1-6): "))
    except ValueError:
        print("  [ERROR] Invalid choice.")
        return

    # Control flow — if/elif/else to handle each field
    if field_choice == 1:
        target["name"] = get_valid_name()  # Dictionary modification
    elif field_choice == 2:
        target["age"] = get_valid_age()
    elif field_choice == 3:
        target["gpa"] = get_valid_gpa()
    elif field_choice == 4:
        target["active"] = get_active_status()
    elif field_choice == 5:
        new_subjects = get_subjects()
        target["subjects"] = list(new_subjects)  # Convert set → list
    elif field_choice == 6:
        new_courses = get_courses()
        target["courses"] = [list(c) for c in new_courses]  # Convert tuples → lists
    elif field_choice == 0:
        print("  Update cancelled.")
        return
    else:
        print("  [ERROR] Invalid choice. No changes made.")
        return

    save_students(students)  # Persist changes
    print(f"\n  ✅ Student '{target['name']}' updated successfully!")


def delete_student(students):
    """
    Delete a student record by ID with confirmation.

    Demonstrates: List method (remove), Control Flow, String Methods.

    Args:
        students (list): The list of student records (modified in-place).
    """
    print("\n" + "=" * 50)
    print("  🗑️  DELETE STUDENT")
    print("=" * 50)

    if len(students) == 0:
        print("  No records to delete.")
        return

    try:
        student_id = int(input("  Enter Student ID to delete: "))
    except ValueError:
        print("  [ERROR] Invalid ID.")
        return

    # Find the student using a for loop
    target = None
    for student in students:
        if student["id"] == student_id:
            target = student
            break

    if target is None:
        print(f"  Student with ID {student_id} not found.")
        return

    # Confirmation prompt — String method: lower()
    print(f"\n  ⚠️  Are you sure you want to delete '{target['name']}'?")
    confirm = input("  Type 'yes' to confirm: ").strip().lower()

    if confirm == "yes":
        students.remove(target)  # List method: remove()
        save_students(students)
        print(f"  ✅ Student '{target['name']}' deleted successfully.")
    else:
        print("  Deletion cancelled.")


def calculate_statistics(students):
    """
    Calculate and display statistics about student records.

    Demonstrates: Arithmetic Operators (+, /, //), Comparison Operators,
                  For Loop, Variables, Functions (len, sum, max, min, round).

    Args:
        students (list): The list of student records.
    """
    print("\n" + "=" * 50)
    print("  📊  STUDENT STATISTICS")
    print("=" * 50)

    if len(students) == 0:
        print("  No records available for statistics.")
        return

    # Variables to accumulate statistics
    total_students = len(students)                  # int
    total_gpa = 0.0                                 # float accumulator

    # Counters — int variables
    active_count = 0
    inactive_count = 0

    highest_gpa = students[0]["gpa"]                # Initialize with first record
    lowest_gpa = students[0]["gpa"]
    highest_gpa_student = students[0]["name"]
    lowest_gpa_student = students[0]["name"]

    # Set to collect all unique subjects across students
    all_subjects = set()

    total_age = 0  # For calculating average age

    # For loop — iterate through all students to compute statistics
    for student in students:
        gpa = student["gpa"]
        total_gpa = total_gpa + gpa     # Arithmetic operator: addition

        total_age = total_age + student["age"]

        # Comparison operators — track highest and lowest GPA
        if gpa > highest_gpa:
            highest_gpa = gpa
            highest_gpa_student = student["name"]
        if gpa < lowest_gpa:
            lowest_gpa = gpa
            lowest_gpa_student = student["name"]

        # Logical operator (if/else) — count active vs inactive
        if student["active"]:
            active_count = active_count + 1   # Arithmetic: increment
        else:
            inactive_count = inactive_count + 1

        # Set — union of all subjects for uniqueness
        for subject in student["subjects"]:
            all_subjects.add(subject)  # Set method: add()

    # Arithmetic operators: division for averages
    average_gpa = total_gpa / total_students      # float division
    average_age = total_age // total_students      # integer (floor) division

    # Display results with string formatting
    print(f"\n  Total Students     : {total_students}")
    print(f"  Active Students    : {active_count}")
    print(f"  Inactive Students  : {inactive_count}")
    print(f"  Average GPA        : {average_gpa:.2f}")
    print(f"  Highest GPA        : {highest_gpa:.2f} ({highest_gpa_student})")
    print(f"  Lowest GPA         : {lowest_gpa:.2f} ({lowest_gpa_student})")
    print(f"  Average Age        : {average_age}")
    print(f"  Unique Subjects    : {len(all_subjects)}")
    print(f"  All Subjects       : {', '.join(sorted(all_subjects))}")  # sorted() + join()


def filter_students(students):
    """
    Filter students by various criteria.

    Demonstrates: Logical Operators (and, or, not), Comparison Operators,
                  For Loop, Control Flow, Lists.

    Args:
        students (list): The list of student records.
    """
    print("\n" + "=" * 50)
    print("  🔎  FILTER STUDENTS")
    print("=" * 50)

    if len(students) == 0:
        print("  No records to filter.")
        return

    print("  Filter by:")
    print("    1. GPA Range")
    print("    2. Active Status")
    print("    3. Subject")
    print("    4. Age Range")
    print("    0. Cancel")

    try:
        filter_choice = int(input("\n  Select filter (0-4): "))
    except ValueError:
        print("  [ERROR] Invalid choice.")
        return

    filtered = []  # List to store filtered results

    if filter_choice == 1:
        # ── Filter by GPA Range ──
        try:
            min_gpa = float(input("  Enter minimum GPA: "))
            max_gpa = float(input("  Enter maximum GPA: "))
        except ValueError:
            print("  [ERROR] Invalid GPA value.")
            return

        # For loop with logical operator (and) for range check
        for student in students:
            # Comparison + Logical operators: >= and <=
            if student["gpa"] >= min_gpa and student["gpa"] <= max_gpa:
                filtered.append(student)

    elif filter_choice == 2:
        # ── Filter by Active Status ──
        status_input = input("  Show active or inactive students? (active/inactive): ").strip().lower()

        if status_input == "active":
            target_status = True    # bool
        elif status_input == "inactive":
            target_status = False   # bool
        else:
            print("  [ERROR] Invalid status.")
            return

        for student in students:
            if student["active"] == target_status:  # Comparison operator
                filtered.append(student)

    elif filter_choice == 3:
        # ── Filter by Subject ──
        subject_query = input("  Enter subject to filter by: ").strip().title()

        for student in students:
            # 'in' operator — check if subject exists in the student's list
            if subject_query in student["subjects"]:
                filtered.append(student)

    elif filter_choice == 4:
        # ── Filter by Age Range ──
        try:
            min_age = int(input("  Enter minimum age: "))
            max_age = int(input("  Enter maximum age: "))
        except ValueError:
            print("  [ERROR] Invalid age value.")
            return

        for student in students:
            # Logical operator: and
            if student["age"] >= min_age and student["age"] <= max_age:
                filtered.append(student)

    elif filter_choice == 0:
        print("  Filter cancelled.")
        return
    else:
        print("  [ERROR] Invalid choice.")
        return

    # Display filtered results
    if len(filtered) > 0:
        print(f"\n  Found {len(filtered)} matching student(s):\n")
        print(f"  {'ID':<5} {'Name':<25} {'Age':<6} {'GPA':<7} {'Status':<10} {'Subjects'}")
        print("  " + "-" * 75)

        for s in filtered:
            status = "Active" if s["active"] else "Inactive"
            subjects = ", ".join(s["subjects"])
            print(f"  {s['id']:<5} {s['name']:<25} {s['age']:<6} {s['gpa']:<7.2f} {status:<10} {subjects}")
    else:
        print("\n  No students matched the filter criteria.")


# ──────────────────────────────────────────────
# MAIN MENU & PROGRAM ENTRY POINT
# ──────────────────────────────────────────────

def display_menu():
    """
    Display the main menu options.

    Demonstrates: String formatting, Print function.
    """
    print("\n" + "=" * 50)
    print(f"  🎓  {PROGRAM_TITLE.upper()}")  # String method: upper()
    print("=" * 50)
    print("    1.  Add Student")
    print("    2.  View All Students")
    print("    3.  Search Student")
    print("    4.  Update Student")
    print("    5.  Delete Student")
    print("    6.  Calculate Statistics")
    print("    7.  Filter Students")
    print("    8.  Exit")
    print("=" * 50)


def main():
    """
    Main function — entry point of the application.

    Demonstrates: While Loop (menu loop), Control Flow (if/elif),
                  Function calls, Exception Handling.
    """
    # Load existing records from file on startup (File I/O)
    students = load_students()  # List of dictionaries

    # Bool variable to control the main loop
    running = True

    print("\n" + "🎓 " * 15)
    print(f"  Welcome to the {PROGRAM_TITLE}!")
    print("🎓 " * 15)

    # While loop — keep the program running until the user exits
    while running:
        display_menu()  # Function call

        try:
            choice = int(input("\n  Enter your choice (1-8): "))
        except ValueError:
            # Exception Handling — non-integer menu choice
            print("  [ERROR] Please enter a number between 1 and 8.")
            continue  # Skip to the next iteration of the while loop

        # Control flow — if/elif/else to route to the correct function
        if choice == 1:
            add_student(students)         # Function call
        elif choice == 2:
            view_all_students(students)
        elif choice == 3:
            search_student(students)
        elif choice == 4:
            update_student(students)
        elif choice == 5:
            delete_student(students)
        elif choice == 6:
            calculate_statistics(students)
        elif choice == 7:
            filter_students(students)
        elif choice == 8:
            # Save before exiting (File I/O)
            save_students(students)
            print("\n  👋 Thank you for using the Student Record System. Goodbye!\n")
            running = False  # Bool — set to False to exit the while loop
        else:
            print("  [ERROR] Invalid choice. Please enter a number between 1 and 8.")


# ──────────────────────────────────────────────
# PROGRAM EXECUTION
# ──────────────────────────────────────────────

# This ensures the program runs only when executed directly,
# not when imported as a module.
if __name__ == "__main__":
    main()
