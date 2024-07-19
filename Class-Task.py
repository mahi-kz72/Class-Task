class LibraryItem:
    def __init__(self, title, author, item_id, available=True):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.available = available

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ID: {self.item_id}, Available: {self.available}"

class Book(LibraryItem):
    def __init__(self, title, author, item_id, isbn, available=True):
        super().__init__(title, author, item_id, available)
        self.isbn = isbn

    def __str__(self):
        return f"Book: {self.title}, Author: {self.author}, ID: {self.item_id}, ISBN: {self.isbn}, Available: {self.available}"

class DVD(LibraryItem):
    def __init__(self, title, author, item_id, director, runtime, available=True):
        super().__init__(title, author, item_id, available)
        self.director = director
        self.runtime = runtime

    def __str__(self):
        return f"DVD: {self.title}, Author: {self.author}, ID: {self.item_id}, Director: {self.director}, Runtime: {self.runtime} min, Available: {self.available}"

class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number, publication_date, available=True):
        super().__init__(title, author, item_id, available)
        self.issue_number = issue_number
        self.publication_date = publication_date

    def __str__(self):
        return f"Magazine: {self.title}, Author: {self.author}, ID: {self.item_id}, Issue: {self.issue_number}, Date: {self.publication_date}, Available: {self.available}"

class Library:
    total_items = 0

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        Library.total_items += 1

    def remove_item(self, item_id):
        self.items = [item for item in self.items if item.item_id != item_id]
        Library.total_items -= 1

    def check_out_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                item.available = False
                return

    def return_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                item.available = True
                return

    def display_available_items(self):
        for item in self.items:
            if item.available:
                print(item)

    def display_items_by_type(self, item_type):
        for item in self.items:
            if isinstance(item, item_type):
                print(item)

def main():
    library = Library()

    book1 = Book("book 1", "author A", "ID001", "ISBN001")
    book2 = Book("book 2", "author B", "ID002", "ISBN002")
    
    dvd1 = DVD("dvd 1", "director A", "ID003", "Director A", 120)
    dvd2 = DVD("dvd 2", "director B", "ID004", "Director B", 90)
    
    magazine1 = Magazine("magazine 1", "editor 1", "ID005", 1, "2024-01")
    magazine2 = Magazine("magazine 2", "editor 2", "ID006", 2, "2024-02")

    library.add_item(book1)
    library.add_item(book2)
    library.add_item(dvd1)
    library.add_item(dvd2)
    library.add_item(magazine1)
    library.add_item(magazine2)

    library.check_out_item("ID001")
    library.check_out_item("ID003")
    library.check_out_item("ID005")

    library.return_item("ID001")

    library.remove_item("ID002")

    library.display_available_items()

    library.display_items_by_type(Book)
    
    library.display_items_by_type(DVD)
    
    library.display_items_by_type(Magazine)

