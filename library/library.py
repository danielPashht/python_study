from book import Book


class Library:
	def __init__(self):
		self.books: list = []

	def add_book(self, book: Book):
		self.books.append(book)
		print(f'Book {book.title} added to the library')

	def remove_book(self, book: Book):
		self.books.remove(book)
		print(f'Book {book.title} removed from the library')

	def get_book_by_author(self, author: str) -> list:
		return [book for book in self.books if book.author == author]

	def borrow(self, book: Book):
		if book.available and book in self.books:
			book.available = False
			print(f'You borrowed book: {book.title}')
		else:
			print(f'Book {book.title} is not available')

	@staticmethod
	def return_book(book: Book):
		if not book.available:
			book.available = True
			print(f'You returned book: {book.title}')
		else:
			print(f'Book {book.title} is already in the library')

	def print_books(self):
		print('\n-------------LIBRARY----------------')
		for book in self.books:
			print(f'{book.title} by {book.author} ({book.publication_year}) - {"available" if book.available else "not available"}\n')
