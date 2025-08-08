import csv
class book:
    def __init__(self,title,authour,price):
        self.title=title
        self.authour=authour
        self.__price=price
    
    def get_info(self):
        return f"Title ={self.title}, Authour = {self.authour}, price ={self.__price}"

class library:
    def __init__(self):
        self.books=[]
 
    def add_book(self, book):
        self.books.append(book)
    
    def show_info(self):
        for book in self.books:
            print(book.get_info())

    def save_to_csv(self,):
        with open('hub.csv',mode='w',newline='') as f:
            writer=csv.writer(f)
            writer.writerow(["title","authour","price"])
            for book in self.books:
                writer.writerow([book.title,book.authour,book._book__price])

class user():
    def __init__(self,name):
        self.name=name
    
    def borrow_book(self,title,library):
        for book in library.books:
            if book.title.lower()==title.lower():
                library.books.remove(book)
                print(f'{self.name} Borrowed {book.title} from library' )
                return
        print(f'Book not found')

    def return_book(self,book,library):
        library.books.append(book)
        print(f'{self.name} returned {book.title} to the library')


b1 = book("Harry Potter", "J.K. Rowling", 500)
b2 = book("The Alchemist", "Paulo Coelho", 350)

lib = library()
lib.add_book(b1)
lib.add_book(b2)


u1=user('Abhi')

u1.borrow_book("Harry Potter",lib)

print("\n Library after borrowing")
lib.show_info()

u1.return_book(b1,lib)

print("\n Library after returning")
lib.show_info()
lib.save_to_csv()
print(f'books are saved')