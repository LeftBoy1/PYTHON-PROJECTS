class Library:
    def __init__(self):
        self.no_books = 0
        self.books = []
        
    def add_books(self,book):
        self.books.append(book)
        self.no_books = len(self.books)
        
    def showInfo(self):
        print(f"\nThe Library has {self.no_books} Books.\nThe books are:-")
        for i in self.books:
            print(i)
        
    
l1 = Library()
l1.add_books("BHAGWAT GEETA")
l1.add_books("RAMAYAN")
l1.add_books("Harry Potter")
l1.add_books("MONEY PART")
l1.add_books("THE WISE MAN")
l1.add_books("THE MAN")

l1.showInfo()