import json
file_name="students.json"
def load_students():
    try:
        with open(file_name,"r") as file:
            return json.load(file)
    except:
        return []
def save_students(students):
    with open(file_name,"w") as file:
        json.dump(students,file,indent=4)
def get_grade(marks):
    if marks>=90:
        return"A+"
    elif marks>=80:
        return"A"
    elif marks>=70:
        return"B"
    elif marks>=60:
        return"C"
    elif marks>=50:
        return"D"
    else:
        return"F"
def add_student(students):
    student_id=input("Enter student ID: ")

    for student in students:
        if student["id"]==student_id:
            print("This ID already exists.")
            return

    name=input("Enter student name: ")
    course=input("Enter course: ")

    try:
        marks=float(input("Enter marks: "))
    except:
        print("Please enter a valid number.")
        return

    if marks<0 or marks>100:
        print("Marks should be between 0 and 100.")
        return

    student = {
        "id":student_id,
        "name":name,
        "course":course,
        "marks":marks,
        "grade":get_grade(marks)
    }

    students.append(student)
    save_students(students)
    print("Student added successfully.")
def show_students(students):
    if len(students)==0:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("--------------------------------------------")

    for student in students:
        print("ID:",student["id"])
        print("Name:",student["name"])
        print("Course:",student["course"])
        print("Marks:",student["marks"])
        print("Grade:",student["grade"])
        print("--------------------------------------------")
def search_student(students):
    student_id=input("Enter student ID: ")

    for student in students:
        if student["id"]==student_id:
            print("\nStudent Found")
            print("Name:",student["name"])
            print("Course:",student["course"])
            print("Marks:",student["marks"])
            print("Grade:",student["grade"])
            return

    print("Student not found.")
def update_student(students):
    student_id=input("Enter student ID: ")

    for student in students:
        if student["id"]==student_id:
            print("Leave blank if you don't want to change something.")

            name=input("Enter new name: ")
            course=input("Enter new course: ")
            marks=input("Enter new marks: ")

            if name!="":
                student["name"] = name

            if course!="":
                student["course"]=course

            if marks!="":
                try:
                    marks=float(marks)

                    if marks<0 or marks>100:
                        print("Marks should be between 0 and 100.")
                        return

                    student["marks"]=marks
                    student["grade"]=get_grade(marks)

                except:
                    print("Invalid marks.")
                    return

            save_students(students)
            print("Student updated successfully.")
            return

    print("Student not found.")
def delete_student(students):
    student_id = input("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully.")
            return

    print("Student not found.")
def main():
    students=load_students()

    while True:
        print("\n===== Student Management System =====")
        print("1.Add Student")
        print("2.Show Students")
        print("3.Search Student")
        print("4.Update Student")
        print("5.Delete Student")
        print("6.Exit")

        choice=input("Enter your choice: ")

        if choice=="1":
            add_student(students)
        elif choice=="2":
            show_students(students)
        elif choice=="3":
            search_student(students)
        elif choice=="4":
            update_student(students)
        elif choice=="5":
            delete_student(students)
        elif choice=="6":
            print("Program ended.")
            break
        else:
            print("Invalid choice.")
main()
