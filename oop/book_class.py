class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def _del_(self):
        print (f"Deleting (title of the book)")
        
    def __str__(self):
        return f"(title) by (author), published in (year)"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year}"