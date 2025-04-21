student = {}

def add_student():
    print("Enter student details")
    name = input("Enter student name: ").upper()
    age = input("Enter student age: ")
    student_class = input("Enter student class: ").upper()
    if name not in student:
        data = {"Student name": name, "Student age": age, "Student class": student_class}
        student[name] = data
    else:
        print("Student name already exists, overwriting...")
        
     

def view_student():
      for items, record in student.items():
        for item, value in record.items():
            print(item, ":", value)
          
                
def search_student():
    name_search = input("Enter name of student to be searched: ").upper()
    found = False
    for students, record in student.items():
      if record["Student name"] == name_search:
            print("Student found:")
            for key, value in record.items():
                  print(f"{key}: {value}")
                  found = True
                  
      if not found:
            print("Student not found.")

def delete_student():
    delete_name = input("Name of student to be deleted: ").upper()
    found = False
    if delete_name in student:
            del student[delete_name]
            print(f"{delete_name} has been deleted")
            found = True
            
    if not found:
        print("Student not found.")
                
while True:               
    print("---STUDENT RECORD MANAGER---")
    print('''
1. ADD NEW STUDENT
2. VIEW ALL STUDENTS 
3. SEARCH STUDENT BY NAME
4. DELETE STUDENT
5. EXIT
''')
    option = input("Enter options (1-5): ")
    if option == "1":
        add_student()
    elif option == "2":
        view_student()
    elif option == "3":
        search_student()
    elif option == "4":
        delete_student()
    elif option == "5":
        print("Exiting....")
        break
    else:
        print(" invalid input")