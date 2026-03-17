names = []
detail = ()
skill =set()
info = {}

def addName():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    cname = input("Enter course name: ")
    skill.add(cname)   
    names.append(name)
    info[name] = {"age": age, "skills": {cname}}   
    print("Student added successfully!", name)

def showInfo():
    print("\n Student Information:")
    for student, details in info.items():
        print(student, ":", details)
    print("All Students:", names)
    #print("Course Detail:", detail)
    print("Unique Skills:", skill)
    
    
while True:
    print("\n--- Course Management Menu ---")
    print("1. Add Student")
    print("2. Display Info")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        addName()
    elif choice == "2":
        showInfo()
    elif choice == "3":
        print("Exiting system")
        break
    else:
        print("Invalid choice, try again!")
