# OOPs (Object-Oriented Programming)

# OOPS is a programming paradigm that uses "objects and classes" to structure and organize 
# code by modeling real-world entities.

# Class:
# A class is a blueprint/tempelate (guidance ka asa karo) for creating objects. 
# It defines a structure with attributes (variables) and behaviors (methods).

# class declare karna ka liya first letter capital hona chahiyah
class Library():

    # Constructor: A special method that initializes the object's attributes when an instance is created.
    # It is defined using the __init__ method.
    # yh hamesha same hota ha sab ma isa (constructor) kehta hain
    def __init__(self, name, location):  # jab hum koi function yh attributes create krta hain to pehla parameters hamesha self hota ha 
        # class attributes / class variables / parameters
        self.lib_name = name  # self ka sath jo bhi cheez likhain ga wo class ko refer kara gi (self.lib_name)
                              # constructor sab sa pehla chala ga  (= name ) constructor ha 
        self.lib_location = location
        self.books = []  # ek khali list banai jisme books add hongi

    def add_books(self, new_book):
        return self.books.append(new_book)  # new_book ko books list me add karega
    
    def remove_books(self, remove_book):
        return self.books.remove(remove_book)  # remove_book ko books list se remove karega
    
    def get_books(self):
        return self.books  # ab tak jitni books add hui hain un sab ko return karega

# Object:
# An object is an instance of a class. 
# It represents a real-world entity with specific data and behavior defined by its class.

# making an object/ creating an instance
library = Library("The Library", "Karachi")
print(library)

# calling  one by one parameter
print(library.lib_name)       # The Library
print(library.lib_location)   # Karachi

class Book():
    # Constructor
    def __init__(cls, name, author, price, availability):
        # class attributes
        cls.book_name = name
        # cls.book_author = author
        cls.author = "Laiba"  # yh overwrite kr skta ha agr hum jo yahan dain ga wo result ma show ho ga nicha print ma jo value ha wo show nahi ho gi
        cls.book_price = price
        cls.availability = availability

    def borrow(cls):
        return cls.availability  # agar book available ha to True return karega

# Making an object / creating Instance of class
book1 = Book("Python Programming", "John Doe", "$ 500", True)
print(book1.author)         # Laiba (overwrite ho chuka ha)
print(book1.book_name)      # Python Programming
print(book1.book_price)     # $ 500
print(book1.availability)   # True


# Creating more book objects
book2 = Book("Comedy", 'Umer Shareef', "$400", True)
book3 = Book("Tradegy", 'Ahmed', "$400", True)

# Making library object
mylib = Library("My Python Library", "Karachi")
print(mylib.lib_name)       # My Python Library
print(mylib.lib_location)   # Karachi

# Adding books to the library
print(mylib.add_books(book2.book_name))  # None (append returns None)
print(mylib.add_books(book3.book_name))  # None

# Showing all books in library
print(mylib.get_books())  # ['Comedy', 'Tradegy']

# Removing one book from library
print(mylib.remove_books(book3.book_name))  # None
print(mylib.get_books())  # ['Comedy']
