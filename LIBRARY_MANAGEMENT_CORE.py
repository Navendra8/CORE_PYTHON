

import time 
class Library():
    def __init__(self,books_list):
        self.books_list=books_list
        
    def display_available_books(self):
        print("""THE BOOKS AVAILABLE IN LIBRARY ARE AS FOLLOWS  """)
        for books in self.books_list:
            print (books)        
    def lend_books(self,Requestedbooks):
        if Requestedbooks in self.books_list:
            print(f"THE BOOK {Requestedbooks} is lended to You")
            self.books_list.remove(Requestedbooks) 
        else:
            print("Sorry book is not available Please try again ")
            
    def add_books(self,Return_book):
        print("Please wait")
        time.sleep(2)
        print("Your Book has been now return Have a great day ")
        self.books_list.append(Return_book)
        
class Student(Library):
    
    def requestbook(self):
        self.book=input("Enter the Name of the book you would like to borrow")
        print(f"PLEASE WAIT WHILE WE CHECK IN FOR {self.book}")
        time.sleep(2)
        return f"Your book {self.book} is now been borrowed " 
            
            
    def returnbook(self):
        self.book=input("Enter the Name of the book you want to return ")
        print(f"PLEASE WAIT WHILE WE CHECK IN FOR {self.book}")
        time.sleep(2)
        return f"Your book {self.book} is now been returned " 
            
            
            
            
            
            
            
            
