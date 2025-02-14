from dbm.ndbm import library


# LibraryManagementSystem.py

# Library Management System

#     1. Should display all the books in library
#     2. Customer can request to barrow a book
#     3. Update the library collection when customer returns a book

class LibraryManagementSystem :
    # list of books { name : status }
    libraryCollection = {
        "The Secret" : "Available",
        "Python For Begineers" : "Available",
        "Learning Python" : "Available",
        "Python Crash Course" : "Available",
        "Python For Data Analysis" : "Available"
    }

    # initial function and to ask to borrow
    def init(self) :
        self.displayList()

        # To borrow a book
        borrow = input("Do you want to borrow a book? Yes/No :: ")
        if borrow.lower() == 'yes' :
            bookSelected = input("Please enter the book you need : ")
            print(self.bookRequest(bookSelected))
        elif borrow.lower == 'no' :
            return

        print()

    # display the book collection
    def displayList(self) :
        print()
        for book, status in self.libraryCollection.items():
            # The formatted string (f"") inserts book and status values dynamically.
            print(f"{book}: {status}")
        print()

    # Borrwing a book
    def bookRequest(self, name) :
        if name == '':
            return "Please provide the book name"

        if name not in self.libraryCollection :
            print("Not Available")
            return

        if self.libraryCollection[name] == "Available" :
            self.libraryCollection[name] = "Not Available"
            print("The book is under your name now.")
        else:
            print("Sorry, this book is already borrowed.")
        
        self.displayList()
        # To return a book
        print()
        returnBook = input("Do you want to return a book? Yes/No :: ")
        if returnBook.lower() == 'yes' :
            returnBook = input("Please enter the book you want to return : ")
            print(self.bookReturn(returnBook))

    # Returning a book
    def bookReturn(self, name) :
        if name not in self.libraryCollection:
            print("This book does not belong to our library.")
            return

        if self.libraryCollection[name] == "Not Available" :
            self.libraryCollection[name] = "Available"
            print("Thanks for returning!!")
        else :
            print("You have not borrowed the book.")
        self.displayList()

librarySystem =  LibraryManagementSystem()
librarySystem.init()
            


