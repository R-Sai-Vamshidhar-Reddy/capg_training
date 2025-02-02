class Book_details:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn

    def display(self):
        print(f"{self.title} - {self.author} - {self.isbn}")

n=int(input("Enter number of inputs: "))
for i in range(n):
    title=input("Enter the title: ")
    author=input("Enter the author: ")
    isbn=int(input("Enter the isbn number: "))
    obj=Book_details(title,author,isbn)
    obj.display()