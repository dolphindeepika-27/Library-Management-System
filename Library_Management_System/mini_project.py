class Library:
    def __init__(self,list,name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"There are following books in our Library: {self.name}")
        for book in self.booksList:
            print(book)


    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. Now you can take the book !!")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")                            

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book-list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    deepika = Library(['Our Mission','Two States', 'Ramayan', 'Mahabharat', 'Python', 'C programming'], "TECHdee")

    while(True):
        print(f"Welcome to the {deepika.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book ")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()                                   
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue 
        else:
            user_choice = int(user_choice)

        if user_choice==1:
            deepika.displayBooks()

        elif user_choice==2:
            book = input("Enter the book that yoy want to lend:")
            user = input("Enter your name")
            deepika.lendBook(user, book)

        elif user_choice==3:
            book = input("Enter the book that yoy want to add:")
            deepika.addBook(book)

        elif user_choice==4:
            book = input("Enter the book that yoy want to return:")
            deepika.returnBook(book)
            
        else:
            print("Not a Valid Option")
 
        
        print("Press Q to quit and C to Continue")
        user_choice2 = ""
        while(user_choice2!="C" and user_choice2!="Q"):
            user_choice2 = input()
            if user_choice2 == "Q":
              exit()
            elif user_choice2 == "C":
                continue