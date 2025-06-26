class Library_Management_System:
    
    def _init_(self, Title, Author, Price,Pages):
        self.Title = Title
        self.Author = Author
        self.Price = Price
        self.Pages=Pages

    def get_Title(self):
        return self.Title

    def get_Author(self):
        return self.Author

    def get_Price(self):
        return self.Price
        
    def get_Pages(self):
        return self.Pages


book_1=  Library_Management_System("Wings of Fire", "A.P.J Abdul Kalam", 250,670)
book_2 = Library_Management_System("Wings of Fire", "A.P.J Abdul Kalam", 250,765)
book_3 = Library_Management_System("Happy Prince", "Oscar Wilde", 180,876)
book_4 = Library_Management_System("Harry Potter", "J.K. Rowling", 500,144)
book_5 = Library_Management_System("Black", "John Doe", 220,249)
book_6 = Library_Management_System("White", "Jane Smith", 210,567)


print("Book 1 Title:", book_1.get_Title())
print("Book 2 Title:", book_2.get_Title())
print("Book 3 Title:", book_3.get_Title())
print("Book 4 Title:", book_1.get_Title())
print("Book 5 Title:", book_4.get_Title())
print("Book 1 Author:", book_1.get_Author())
print("Book 2 Author:", book_1.get_Author())
print("Book 3 Author:", book_1.get_Author())
print("Book 4 Author:", book_1.get_Author())
print("Book 5 Author:", book_1.get_Author())
print("Book 1 Price:", book_1.get_Price())
print("Book 2 Price:", book_1.get_Price())
print("Book 3 Price:", book_1.get_Price())
print("Book 4 Price:", book_1.get_Price())
print("Book 5 Price:", book_1.get_Price())
print("Book 1 Pages:", book_1.get_Pages())
print("Book 2 Pages:", book_1.get_Pages())
print("Book 3 Pages:", book_1.get_Pages())
print("Book 4 Pages:", book_1.get_Pages())
print("Book 5 Pages:", book_1.get_Pages())
