class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        

book1 = Book("Isang Kaibigan", "VP Sara Duterte")
print(f"Title: {book1.title} - Aupthor: {book1.author}")
del book1.author
print(f"Title: {book1.title} - Author: {book1.author}")

book2 = Book("How to sleep", "Rafael Pelayo MD")
print(f"Title: {book2.title} - Author: {book2.author}")