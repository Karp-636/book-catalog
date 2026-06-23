class Book:
    total_books = 0

    def __init__(self, title, author, page_count, genre):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.genre = genre
        Book.total_books += 1
        self.id = Book.total_books

    def describe(self):
        print(f'"{self.title}" by {self.author} - {self.page_count} pages ({self.genre})')
        print(f'{self.id} out of {self.total_books}')



book1 = Book("Nineteen Eighty-Four", "Geogre Orwell", 328, "fiction")
book2 = Book("Marked - The House of Night", "P.C. Cast and Kristin Cast", 304, "paranormal fantasy" )
book3 = Book("Evermore - The Immortals", "Alyson Noel", 320, "paranormal fantasy")
book4 = Book("The Lightning Thief - Percy Jackson & the Olympians", "Rick Riordan", 377, "greek mythology fantasy")



book1.describe()
book2.describe()
book3.describe()
book4.describe()