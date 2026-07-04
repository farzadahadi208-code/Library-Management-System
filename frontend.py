import sys
import backend
from PyQt6.QtWidgets import(
QApplication,
QWidget,
QLabel,
QPushButton,
QTableWidget,
QLineEdit,
QMessageBox,
QTableWidgetItem
)   
app=QApplication(sys.argv)
message=QMessageBox()
window=QWidget()
search_botton=QPushButton("Search",window)
add_botton=QPushButton("ADD BOOK",window)
delete_button=QPushButton("DELETE BOOK",window)
label=QLabel()
textbox=QLineEdit(window)
textbox_add=QLineEdit(window)
deleted_book=QLineEdit(window)




def search():
    book_name=textbox.text()
    status=backend.SEARCH_BOOK.SEARCH(book_name)

    if status:
        message.information(
            window,
            "Search",
            "This Book Exists"
    )
    else:
        message.information(
            window,
            "Search",
            "This Book Does`t Exists"
    )
        
def add_book():
    id_book = id.text()
    title_book = title.text()
    author_book_book = author.text()
    category_book = category.text()
    isbn_book=isbn.text()
    published_year_book=published_year.text()
    language_book=language.text()
    copies_total_book=copies_total.text()
    copies_available_book=copies_available.text()
    shelf_book=shelf.text()
    status_book=status.text()

    backend.ADD_BOOK.ADD(id_book,title_book,author_book_book,category_book,isbn_book,published_year_book,language_book,copies_total_book,copies_available_book,shelf_book,status_book)
 
    message.information(
        window,
        "add book",
        "your book is added"
    )

def delete():
    book_name=deleted_book.text()
    backend.DELETE_BOOK.DELETE(book_name)
    message.warning(
        window,
        "deleted book",
        "this book is deleted forever"
    )

# windows functions

window.resize(1500,900)
window.setWindowTitle("Library Management System")

#botton functions
#layout
search_botton.resize(100,40)
search_botton.move(0,650)
add_botton.resize(100,40)
add_botton.move(0,530)
delete_button.resize(110,40)
delete_button.move(220,650)
#TABEL PART
table=QTableWidget(window)
table.setRowCount(15)
table.setColumnCount(11)
table.setHorizontalHeaderLabels(
    ["id","title","author","category","isbn","published_year","language","copies_total","copies_available","shelf","status"]
)
#show book
table.resize(1150,450)
rows=backend.SHOW_BOOK.SHOW()
for i,row in enumerate(rows):
    for j,value in enumerate(row):
        table.setItem(i,j,QTableWidgetItem(str(value)))


#search a book in GUI WAY
search_botton.clicked.connect(search)
textbox.resize(100,40)
textbox.move(110,650)
textbox.setPlaceholderText("SEARCH")

#add book
textbox_add.setPlaceholderText("ADD")

label_id=QLabel("ID",window)
label_id.move(170,450)
id=QLineEdit(window)
id.move(110,470)

label_title=QLabel("TITLE",window)
label_title.move(170,500)
title=QLineEdit(window)
title.move(110,520)

label_author_name=QLabel("AUTHO NAME",window)
label_author_name.move(140,550)
author=QLineEdit(window)
author.move(110,570)
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
label_category=QLabel("CATEGORY",window)
label_category.move(290,450)
category=QLineEdit(window)
category.move(250,470)

label_isbn=QLabel("isbn",window)
label_isbn.move(300,500)
isbn=QLineEdit(window)
isbn.move(250,520)

label_published_year=QLabel("PUBLISDHED YEAR",window)
label_published_year.move(270,550)
published_year=QLineEdit(window)
published_year.move(250,570)
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
label_language=QLabel("LANGUAGE",window)
label_language.move(440,450)
language=QLineEdit(window)
language.move(390,470)

label_copies_total=QLabel("COPIES_TOTAL",window)
label_copies_total.move(425,500)
copies_total=QLineEdit(window)
copies_total.move(390,520)

label_copies_availabe=QLabel("COPIES_AVAILABLE",window)
label_copies_availabe.move(410,550)
copies_available=QLineEdit(window)
copies_available.move(390,570)
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
label_shelf=QLabel("SHELF",window)
label_shelf.move(580,450)
shelf=QLineEdit(window)
shelf.move(530,470)

label_status=QLabel("STATUS",window)
label_status.move(580,500)
status=QLineEdit(window)
status.move(530,520)

add_botton.clicked.connect(add_book)


# DELETE BOOKS
deleted_book=QLineEdit(window)
deleted_book.resize(100,40)
deleted_book.move(340,650)
deleted_book.setPlaceholderText("DELETE")
delete_button.clicked.connect(delete)


window.show()
app.exec() 