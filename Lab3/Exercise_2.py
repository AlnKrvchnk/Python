class Book:
    def __init__(self,title,author,id=None):
        self.__title=title
        self.__author=author
        self.__id=id
    def setcode(self,code):
        self.__id=code
    def __str__(self): 
        return "[%s] %s '%s'" % (str(self.__id), self.__author, self.__title)
    def tag(self):
        return ["".join([s for s in tag if s.isalpha()]) for tag in self.__title.split(" ") if tag.istitle()]
class Library(Book):
    code=1
    def __init__(self,num,address):
        self.__num=num
        self.__address=address
        self.__books=[]
    def __iadd__(self, book):
        book.setcode(self.code)
        self.code+=1
        self.__books.append(book)
        return self
    def __iter__(self): 
        return iter(self.__books)  

lib = Library(1, '51 Some str., NY')
lib += Book('Leo Tolstoi', 'War and Peace')
lib += Book('Charles Dickens', 'David Copperfield')
for book in lib:
# вывод в виде: [1] L.Tolstoi ‘War and Peace’
    print(book)
# вывод в виде: [‘War’, ‘Peace’]
    print(book.tag())
