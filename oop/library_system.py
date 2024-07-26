class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"title: {self.title}, author: {self.author}"
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
        
    def __str__(self):
        return f"title: {self.title}, author: {self.author}, file size: {self.file_size}MB"
    
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
        
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Page Count: {self.page_count} pages"
    
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        if isinstance(book, book):
            self.books.append(book)
        else:
            raise ValueError("Only instances of Book or its subclasses can be added.")
        
    def list_books(self):
        if not self.books:
            print("The library is empty.")
        for book in self.books:
            print(book)