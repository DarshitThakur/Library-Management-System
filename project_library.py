books = ["Chemistry","Physics","MAths","Java","C++"]
issuedBook = []

def avaliable():
    for i in books:
        print(i)

def addBooks():
    Book = input("Enter Book Name :- ")
    books.append(Book)
    avaliable()

def issue():
    avaliable()
    Book = input("Enter Book Name :- ")
    issuedBook.append(Book)
    books.append(issuedBook)
    print ("Book issued Sccucessfully: - ",Book )
    if (Book not in books):
         print("Book Not Avaliable ! Please try again ")

def returnBook():
    print(issuedBook)
    returnBook = []
    Book = input("Enter Book you want to Return :- ")
    returnBook.append(Book)
    books.append(returnBook)
    print("Book return Succesfullu:- ", Book)
    avaliable()    
    if (Book not in books):
         print("Book Not Issued ! Please try again ")

while True:
        print("\nLibrary Book Management")
        print("1:- Available Books")
        print("2:- Add books")
        print("3:- Book issue")
        print("4:- Return book")
        print("5:- Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            avaliable()
        elif choice == 2:
            addBooks()
        elif choice == 3:
            issue()
        elif choice == 4:
                returnBook()
        elif choice == 5:
                print("Exiting...")
                break
        else:
                print("Invalid choice. Please try again.")
        
