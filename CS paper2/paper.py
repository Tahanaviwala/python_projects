# view file only
with open('book.txt') as f:
    lines = f.readlines()
for line in lines:
    print(line)


# read files by line no (first line no is 0)
def readline():
    lineNo = int(input("Line No: "))
    lines = open("book.txt", "r").readlines()[lineNo]
    return print(lines)
    file.close()
readline()


# add new book with author and title name
def addbook():
    bookname = input("Book Name: ")
    authname = input("Author name: ")
    lines = open("book.txt", "a")
    lines.write("\n" + bookname + " - " + authname)
    lines.close()
    file = open("book.txt" , "r")
    content = file.read()
    file.close()
    print(content)
addbook()


# add publication year to the book on new file with author and title
def addpub():
    book = input("Book Name: ")
    pubdate = int(input("Publication Year: "))
    a = open("book.txt" , "r")
    for b in a:
        if book in b:
            c = open("book1.txt" , "a")
            c.write(b + "\nPublication Date: " + str(pubdate))
            break
addpub()
