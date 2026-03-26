'''#student feedback management sys
data store
analyze data
use string n file handling
use string oprn
lower
count
file handling- open read write append
fn use
basic conditions- if else
and also add and store student name and then with feedback so that we can search for an feed back for an particular

add feedback
display feedback
search feedback
feedback analyze- good, bad, worst etc'''

def addfeed():
    name = input("Enter student name: ")
    feedback = input("Enter student feedback: ")
    with open("feedback.txt", "a") as f:
        f.write(name + " : " + feedback + "\n")
    print("Feedback added successfully!")

def showfeed():
    with open("feedback.txt", "r") as f:
            data = f.readlines()
    print("\n All Feedback ")
    for line in data:
            print(line)

def searchfeed():
    find = input("Enter name of student whose feedback you have to know :- ").lower()
    with open("feedback.txt", "r") as f:
            for line in f:
                if find in line.lower():
                   print("Found:", line.strip())            
                else :
                     print("Not found")

def countStud():
    with open("feedback.txt", "r") as f:
        data = f.readlines()
    print("Total number of feedbacks:", len(data))

def analyzefeed():
    with open("feedback.txt", "r") as f:
        data = f.readlines()
    good = bad = worst = 0
    for line in data:
        if "good" in line.lower():
            good += 1
        elif "bad" in line.lower():
            bad += 1
        elif "worst" in line.lower():
            worst += 1
    print("Good feedback: " , good)
    print("Bad feedback: ", bad)
    print("Worst feedback: " , worst)

while True:
    print("\n1. Add Feedback")
    print("2. Show Feedback")
    print("3. Search Feedback")
    print("4. Count Feedback")
    print("5. Analyze Feedback")
    print("6. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        addfeed()
    elif choice == '2':
        showfeed()
    elif choice == '3':
        searchfeed()
    elif choice == '4':
        countStud()
    elif choice == '5':
        analyzefeed()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("O teri.......!!! please try again.")



