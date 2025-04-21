student = []

def add_student():
    print("Enter student details")
    name = input("Enter student name: "). capitalize()
    age = input("Enter student age: ")
    student_class = input("Enter student class: "). capitalize()
    if name not in student:
        data = {"Student name": name, "Student age": age, "Student class": student_class}
        student.append(data)
    else:
        print("Student name already exists, overwriting...")
        
        

def view_student():        
    for items in student:
        for item, value in items.items():
            print(item,":", value)
            print()
                
def search_student():
    name_search = input("Enter name of student to be searched: ").capitalize()
    found = False
    for students in student:
        if students["Student name"] == name_search:
            print("Student found:")
            for key, value in students.items():
                print(f"{key}: {value}")
            found = True
            break
    if not found:
        print("Student not found.")
                
while True:               
    print("---STUDENT RECORD MANAGER---")
    print('''
1. ADD NEW STUDENT
2. VIEW ALL STUDENTS 
3. SEARCH STUDENT BY NAME
4. EXIT
''')
    option = input("Enter options (1-4): ")
    if option == "1":
        add_student()
    elif option == "2":
        view_student()
    elif option == "3":
        search_student()
    elif option == "4":
        print("Exiting....")
        break
    else:
        print(" invalid input")
