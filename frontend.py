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
#QT OBJECTS:
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

#ADD TEXTBOX INPUT
id=QLineEdit(window)
title=QLineEdit(window)
author=QLineEdit(window)
category=QLineEdit(window)
isbn=QLineEdit(window)
published_year=QLineEdit(window)
language=QLineEdit(window)
copies_total=QLineEdit(window)
copies_available=QLineEdit(window)
shelf=QLineEdit(window)
status=QLineEdit(window)

#DELETED TEXBOX INPUT
deleted_book=QLineEdit(window)


class SEARCH_BOOKS:
    def __init__(self):
        textbox.resize(100,40)
        textbox.move(110,650)
        
    def search(self):
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
            
class ADD_BOOKS:  
    def __init__(self): 
        
        self.label_id=QLabel("ID",window)
        self.label_id.move(170,450)
        
        id.move(110,470)

        self.label_title=QLabel("TITLE",window)
        self.label_title.move(170,500)
        
        title.move(110,520)

        self.label_author_name=QLabel("AUTHO NAME",window)
        self.label_author_name.move(140,550)
        
        author.move(110,570)
        #"""""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.label_category=QLabel("CATEGORY",window)
        self.label_category.move(290,450)
        category.move(250,470)

        self.label_isbn=QLabel("isbn",window)
        self.label_isbn.move(300,500)
        isbn.move(250,520)

        self.label_published_year=QLabel("PUBLISDHED YEAR",window)
        self.label_published_year.move(270,550)
        published_year.move(250,570)
        #"""""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.label_language=QLabel("LANGUAGE",window)
        self.label_language.move(440,450)
        language.move(390,470)

        self.label_copies_total=QLabel("COPIES_TOTAL",window)
        self.label_copies_total.move(425,500)
        copies_total.move(390,520)

        self.label_copies_availabe=QLabel("COPIES_AVAILABLE",window)
        self.label_copies_availabe.move(410,550)
        copies_available.move(390,570)
        #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.label_shelf=QLabel("SHELF",window)
        self.label_shelf.move(580,450)
        shelf.move(530,470)

        self.label_status=QLabel("STATUS",window)
        self.label_status.move(580,500)
        status.move(530,520)

    def add(self):
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

class DELETE_BOOKS:
    def __init__(self):
        
        deleted_book.resize(100,40)
        deleted_book.move(340,650)

    def delete(self):
        book_name=deleted_book.text()
        backend.DELETE_BOOK.DELETE(book_name)
        message.warning(
            window,
            "deleted book",
            "this book is deleted forever"
        )  

#OBJECTS
SEARCH_BOOK=SEARCH_BOOKS()
ADD_BOOK=ADD_BOOKS()
DELETE_BOOK=DELETE_BOOKS()

#WINDOW PROPERTY
window.resize(1500,900)
window.setWindowTitle("Library Management System")

#BUTTON`S LICATION
search_botton.resize(100,40)
search_botton.move(0,650)
add_botton.resize(100,40)
add_botton.move(0,530)
delete_button.resize(110,40)
delete_button.move(220,650)

#CREATING TABLES
table=QTableWidget(window)
table.setRowCount(15)
table.setColumnCount(11)
table.setHorizontalHeaderLabels(
    ["id","title","author","category","isbn","published_year","language","copies_total","copies_available","shelf","status"]
)


#DISPLYING BOOKS
table.resize(1150,450)
rows=backend.SHOW_BOOK.SHOW()
for i,row in enumerate(rows):
    for j,value in enumerate(row):
        table.setItem(i,j,QTableWidgetItem(str(value)))


# SEARCH BUTTON
textbox.setPlaceholderText("SEARCH")
search_botton.clicked.connect(SEARCH_BOOKS.search)

#ADD BUTTONS
textbox_add.setPlaceholderText("ADD")
add_botton.clicked.connect(ADD_BOOKS.add)

# DELETE BUTTONS
deleted_book.setPlaceholderText("DELETE")
delete_button.clicked.connect(DELETE_BOOKS.delete)

window.show()
app.exec() 