from library import Library
from book import Book

library = Library()
book1 = Book('The Great Gatsby', 'F. Scott Fitzgerald', '1925')
book2 = Book('To Kill a Mockingbird', 'Harper Lee', '1960')
book3 = Book('George Orwell', '1984', '1949')

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.print_books()
library.borrow(book1)
library.remove_book(book3)
library.return_book(book1)
library.borrow(book3)
