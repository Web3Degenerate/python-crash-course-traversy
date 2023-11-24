# https://teamtreehouse.com/library/objectoriented-python-2/constructicons

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)

class Bookcase: 
    def __init__(self, books=None): #set books to None, b/c we don't want a mutable object passed in, like a list
        self.books = books


    # (1:40) create our @classmethod
    # classmethod's don't take self as first argument or instance or anything like that.
    # INSTEAD, classmethod takes the class they are being called on.
    # BUT, we can't use the keyword 'class' so we use 'cls' instead. (or 'klass')
    @classmethod #the '@' symbol is decorator. A function that takes another function, does something, usually returns that fn
    def create_bookcase(cls, book_list):
        books = []
        for title, author in book_list:
            books.append(Book(title, author))
        return cls(books) #uses the class that was passed in to create a new instance. (uses class' init method)
    


#bc = Bookcase() #DON'T instantiate the class by removing the parens ()
bc = Bookcase.create_bookcase([('Moby-Dick', 'Herman Melville'), ('Jungle Book', 'Rudyard Kipling')])

print(f'Bookcase bc OBJECT created was {bc}')
print(f'Bookcase bc books created are {bc.books}')

print(f'first bc title is {bc.books[0]}')
print(f'second bc title is {bc.books[1]}')

# print(f'first bc author is {bc.books[0][1]}')
# print(f'second bc author is {bc.books[1][1]}')



# CHALLENGE: https://teamtreehouse.com/library/objectoriented-python-2/advanced-objects/dream-vacation

# Below is a class called DreamVacation that holds a location and list of activities. 
# Create a @classmethod called rome that will return a new DreamVacation instance with cls() with the following arguments: 
# location = 'Rome' and activities list = ['visit the Colosseum', 'Eat gelato'].
#Hint: The classmethod should take cls instead of self as an argument.

class DreamVacation:
    def __init__(self, location, activities):
        self.location = location
        self.activities = activities

    @classmethod
    def rome(cls, location='Rome', activities=['visit the Colosseum', 'Eat gelato']):
        books = []
        #for title, author in book_list:
        books.append(location, activities)
        return cls(books)