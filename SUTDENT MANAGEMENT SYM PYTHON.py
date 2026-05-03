#Student Management System

# ---------------- LOGIN SYSTEM ----------------

USERNAME = "anjali"
PASSWORD = "1234"


def login():

    attempts = 3

    while attempts > 0:

        print("\n========== LOGIN PAGE ==========")

        username = input("Enter Username : ")
        password = input("Enter Password : ")

        if username == USERNAME and password == PASSWORD:
            print("\nLogin Successful!")
            return True

        else:
            attempts -= 1
            print(f"Invalid Username or Password!")
            print(f"Attempts Left : {attempts}")

    print("\nToo Many Failed Attempts!")
    return False


# ---------------- STUDENT CLASS ----------------

class Student:

    def __init__(self, roll_no, name, marks):

        self.roll_no = roll_no
        self.name = name
        self.marks = marks     # dictionary

    # Total Marks
    def total_marks(self):

        return sum(self.marks.values())

    # Average Marks
    def average_marks(self):

        return self.total_marks() / len(self.marks)

    # Grade
    def grade(self):

        avg = self.average_marks()

        if avg >= 90:
            return "A+"

        elif avg >= 75:
            return "A"

        elif avg >= 60:
            return "B"

        elif avg >= 40:
            return "C"

        else:
            return "Fail"

    # Display Student Details
    def display(self):

        print("\n========== STUDENT DETAILS ==========")

        print(f"Roll No      : {self.roll_no}")
        print(f"Name         : {self.name}")

        print("Marks:")

        for subject, score in self.marks.items():
            print(f"  {subject} : {score}")

        print(f"Total Marks  : {self.total_marks()}")
        print(f"Average      : {self.average_marks():.2f}")
        print(f"Grade        : {self.grade()}")

        print("-" * 40)


# ---------------- STUDENT MANAGER ----------------

class StudentManager:

    def __init__(self):

        self.students = []

    # Add Student
    def add_student(self):

        roll_no = input("Enter Roll No : ")

        # Duplicate Roll No Check
        for s in self.students:

            if s.roll_no == roll_no:
                print("Roll Number Already Exists!")
                return

        name = input("Enter Name : ")

        marks = {}

        n = int(input("How Many Subjects? : "))

        for i in range(n):

            subject = input("Enter Subject Name : ")
            score = int(input("Enter Marks : "))

            marks[subject] = score

        student = Student(roll_no, name, marks)

        self.students.append(student)

        print("\nStudent Added Successfully!")

    # Show Students
    def show_students(self):

        if not self.students:
            print("No Students Found!")
            return

        for s in self.students:
            s.display()

    # Search Student
    def search_student(self):

        roll_no = input("Enter Roll No to Search : ")

        for s in self.students:

            if s.roll_no == roll_no:

                print("\nStudent Found")
                s.display()
                return

        print("Student Not Found!")

    # Update Student
    def update_student(self):

        roll_no = input("Enter Roll No to Update : ")

        for s in self.students:

            if s.roll_no == roll_no:

                print("\nCurrent Details")
                s.display()

                s.name = input("Enter New Name : ")

                for subject in s.marks:

                    print(f"Update Marks for {subject}")

                    s.marks[subject] = int(
                        input("Enter New Marks : ")
                    )

                print("\nStudent Updated Successfully!")
                return

        print("Student Not Found!")

    # Delete Student
    def delete_student(self):

        roll_no = input("Enter Roll No to Delete : ")

        for s in self.students:

            if s.roll_no == roll_no:

                self.students.remove(s)

                print("Student Deleted Successfully!")
                return

        print("Student Not Found!")

    # Highest Marks Student
    def highest_marks_student(self):

        if not self.students:
            print("No Students Found!")
            return

        topper = max(
            self.students,
            key=lambda s: s.total_marks()
        )

        print("\n========== TOPPER STUDENT ==========")

        topper.display()

    # Average of All Students
    def class_average(self):

        if not self.students:
            print("No Students Found!")
            return

        total = sum(
            s.average_marks()
            for s in self.students
        )

        avg = total / len(self.students)

        print(f"\nClass Average Marks : {avg:.2f}")

    # Sort Students by Total Marks
    def sort_students(self):

        if not self.students:
            print("No Students Found!")
            return

        sorted_students = sorted(
            self.students,
            key=lambda s: s.total_marks(),
            reverse=True
        )

        print("\n===== STUDENTS SORTED BY TOTAL MARKS =====")

        for s in sorted_students:
            s.display()


# ---------------- MAIN MENU ----------------

def menu():

    if login():

        sm = StudentManager()

        while True:

            print("\n========== STUDENT MANAGEMENT SYSTEM ==========")

            print("1. Add Student")
            print("2. Show Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Highest Marks Student")
            print("7. Class Average")
            print("8. Sort Students by Marks")
            print("9. Exit")

            choice = input("\nEnter Your Choice : ")

            if choice == "1":
                sm.add_student()

            elif choice == "2":
                sm.show_students()

            elif choice == "3":
                sm.search_student()

            elif choice == "4":
                sm.update_student()

            elif choice == "5":
                sm.delete_student()

            elif choice == "6":
                sm.highest_marks_student()

            elif choice == "7":
                sm.class_average()

            elif choice == "8":
                sm.sort_students()

            elif choice == "9":

                print("\nProgram Closed Successfully!")
                break

            else:
                print("\nInvalid Choice! Try Again.")


# ---------------- RUN PROGRAM ----------------

menu()

