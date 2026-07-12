import sys 
import backend
from PyQt6.QtWidgets import  QApplication,QLabel,QLineEdit,QPushButton,QComboBox,QWidget, QTableWidget,QTableWidgetItem
#CREATING OBJECTS
app=QApplication(sys.argv)
window=QWidget()

table=QTableWidget(window)
search_window=QWidget()
parameter_box=QComboBox(search_window)
#SEARCH CLASS OBJECTS
show_search_button=QPushButton(window)
show_search_button.move(0,650)
show_search_button.resize(100,55)
show_search_button.setText("Search")
search_button=QPushButton(search_window)
search__parameter_label=QLabel(search_window)
search__name_label=QLabel(search_window)
search_input_parmeter=QLineEdit(search_window)
search_input_name=QLineEdit(search_window)

#ADD CLASS OBJECTS

show_add_button_window=QPushButton(window)
show_add_button_window.resize(100,55)
show_add_button_window.move(110,650)
show_add_button_window.setText("Add Book")
add_book_window=QWidget()
add_button=QPushButton(add_book_window)
add_button.resize(485,40)
add_button.move(20,355)
add_button.setText("Add Book")
#TITLE ADDED
add_book_title_input=QLineEdit(add_book_window)
add_book_title_label=QLabel(add_book_window)
#CATEGORY ADDED
add_book_category_input=QLineEdit(add_book_window)
add_book_category_label=QLabel(add_book_window)
#CLASSIFICATION ADDED
add_book_classification_input=QLineEdit(add_book_window)
add_book_classification_label=QLabel(add_book_window)
#AUTHOR ADDED
add_book_author_input=QLineEdit(add_book_window)
add_book_author_label=QLabel(add_book_window)
#TRANSLETOR ADDED
add_book_transletor_input=QLineEdit(add_book_window)
add_book_transletor_label=QLabel(add_book_window)
#SHELF ADDED
add_book_shelf_input=QLineEdit(add_book_window)
add_book_shelf_label=QLabel(add_book_window)
#ROW ADDED
add_book_row_input=QLineEdit(add_book_window)
add_book_row_label=QLabel(add_book_window)
#BINDING ADDED
add_book_binding_input=QLineEdit(add_book_window)
add_book_binding_label=QLabel(add_book_window)
#ISBN ADDED
add_book_ISBN_input=QLineEdit(add_book_window)
add_book_ISBN_label=QLabel(add_book_window)
#VOLUMES ADDED
add_book_volumes_input=QLineEdit(add_book_window)
add_book_volumes_label=QLabel(add_book_window)
#VOLUME ADDED 
add_book_volume_input=QLineEdit(add_book_window)
add_book_volume_label=QLabel(add_book_window)
#COPIES_TOTAL
add_book_copies_total_input=QLineEdit(add_book_window)
add_book_copies_total_label=QLabel(add_book_window)
#COPIES_AVAILABLE
add_book_copies_available_input=QLineEdit(add_book_window)
add_book_copies_available_label=QLabel(add_book_window)
#PUBLICATION INFORMATION
add_book_publication_input=QLineEdit(add_book_window)
add_book_publication_label=QLabel(add_book_window)
#PAGES ADDED
add_book_pages_input=QLineEdit(add_book_window)
add_book_pages_label=QLabel(add_book_window)
#UNIT PRICE ADDED
add_book_unit_price_input=QLineEdit(add_book_window)
add_book_unit_price_label=QLabel(add_book_window)
#TOTAL PRICE
add_book_total_price_input=QLineEdit(add_book_window)
add_book_total_price_label=QLabel(add_book_window)
#YEAR
add_book_year_input=QLineEdit(add_book_window)
add_book_year_label=QLabel(add_book_window)
#LANGUAGE ADDED
add_book_language_input=QLineEdit(add_book_window)
add_book_language_label=QLabel(add_book_window)
#STATUS ADDED
add_book_status_input=QLineEdit(add_book_window)
add_book_status_label=QLabel(add_book_window)
#NOTES ADDED
add_book_notes_input=QLineEdit(add_book_window)
add_book_notes_label=QLabel(add_book_window)

#DELETE CLASS OBJECTS
show_delete_window=QPushButton(window)
show_delete_window.setText("Delete Book")
delete_window=QWidget()
delete_button=QPushButton(delete_window)
show_delete_window.resize(100,55)
show_delete_window.move(220,650)
delete_book_input=QLineEdit(delete_window)
delete_book_label=QLabel(delete_window)

def update_search_box(text):
    search_input_parmeter.setText(text)


class SHOW_BOOK:
    def __init__(self):
        #creating table
        table.resize(1360,650)
        table.setColumnCount(22)
        table.setRowCount(10000)
        table.setHorizontalHeaderLabels(
            ["ID","TITLE","CATEGORY","CLASS","AUTHOR","TRANSLATOR","SHELF","ROW","BINDING","ISBN","VOLUMES","VOLUME","COPIES_TOTAL","COPIES_AVAILABLE","PUBLICATION","PAGES","UNIT PRICE","TOTAL PRICE","YEAR","LANGUAGE","STATUS","NOTES"]
        )
        #importing data from backend to frontend
        rows=backend.SHOW_BOOKS.disply_book()
        for i,row in enumerate(rows):
            for j,value in enumerate(row):
                table.setItem(i,j,QTableWidgetItem(str(value)))
        table.resizeColumnsToContents()
        window.showMaximized()
        window.show()
        app.exec()
        

class SEARCH_BOOK:
    def __init__(self):
        search_window.resize(450,150) 
        search_window.show()
        search__parameter_label.setText("PARMETER")
        search__parameter_label.show()
        search__parameter_label.move(60,0)
        
        search_input_parmeter.resize(150,30)
        search_input_parmeter.move(20,20)
        

        search__name_label.setText("NAME")
        search__name_label.show()
        search__name_label.move(340,0)
        
        search_input_name.resize(150,30)
        search_input_name.move(280,20)


        search_button.setText("Search")
        search_button.move(170,70)
        search_button.resize(110,40)
        app.exec()


    def find_book(self):
        parameter=parameter_box.currentText()
        name=search_input_name.text()
        answer=backend.SEARCH_BOOKS.result(parameter,name)
        if answer:
            print("it exists")
        else:
            print("it does not exists")

class ADD_BOOK:
    def __init__(self):
        add_book_window.resize(520,400)
        add_book_window.show()
        
        #TITLE ADDED
        add_book_title_input.resize(150,30)
        add_book_title_input.move(20,20)
        add_book_title_label.setText("TITLE (REQURIED)")
        add_book_title_label.move(20,0)
        add_book_title_label.show()
        #CATEGORY ADDED
        add_book_category_input.resize(150,30)
        add_book_category_input.move(20,70)
        add_book_category_label.setText("CATEGORY(REQURIED)")
        add_book_category_label.move(20,50)
        add_book_category_label.show()
        #CLASSIFACATION ADDED
        add_book_classification_input.resize(150,30)
        add_book_classification_input.move(20,120)
        add_book_classification_label.setText("CLASSIFICATION")
        add_book_classification_label.move(20,100)
        add_book_classification_label.show()
        #AUTHOR ADDED
        add_book_author_input.resize(150,30)
        add_book_author_input.move(20,170)
        add_book_author_label.setText("AUTHOR(REQURIED)")
        add_book_author_label.move(20,150)
        add_book_author_label.show()
        #COPIES_AVAILABLE
        add_book_copies_available_input.resize(150,30)
        add_book_copies_available_input.move(20,220)
        add_book_copies_available_label.setText("COPIES_AVAILABLE")
        add_book_copies_available_label.move(20,200)
        add_book_copies_available_label.show()
        #PUBLICATION INFORMATION
        add_book_publication_input.resize(150,30)
        add_book_publication_input.move(20,270)
        add_book_publication_label.setText("PUBLICATION")
        add_book_publication_label.move(20,250)
        add_book_publication_label.show()
        #PAGES ADDED
        add_book_pages_input.resize(150,30)
        add_book_pages_input.move(20,320)
        add_book_pages_label.setText("PAGES")
        add_book_pages_label.move(20,300)
        add_book_pages_label.show()
        #**************************************************
        #TRANSLETOR ADDED
        add_book_transletor_input.resize(150,30)
        add_book_transletor_input.move(190,20)
        add_book_transletor_label.setText("TRANSLETOR")
        add_book_transletor_label.move(190,0)
        add_book_transletor_label.show()
        #SHELF ADDED
        add_book_shelf_input.resize(150,30)
        add_book_shelf_input.move(190,70)
        add_book_shelf_label.setText("SHELF(REQURIED)")
        add_book_shelf_label.move(190,50)
        add_book_shelf_label.show()
        #ROW ADDED
        add_book_row_input.resize(150,30)
        add_book_row_input.move(190,120)
        add_book_row_label.setText("ROW(REQURIED)")
        add_book_row_label.move(190,100)
        add_book_row_label.show()
        #BINDING ADDED
        add_book_binding_input.resize(150,30)
        add_book_binding_input.move(190,170)
        add_book_binding_label.setText("BINDING(REQURIED)")
        add_book_binding_label.move(190,150)
        add_book_binding_label.show()
        #UNIT PRICE ADDED
        add_book_unit_price_input.resize(150,30)
        add_book_unit_price_input.move(190,220)
        add_book_unit_price_label.setText("UNIT PRICE")
        add_book_unit_price_label.move(190,200)
        add_book_unit_price_label.show()
        #TOTAL PRICE
        add_book_total_price_input.resize(150,30)
        add_book_total_price_input.move(190,270)
        add_book_total_price_label.setText("TOTAL PRICE")
        add_book_total_price_label.move(190,250)
        add_book_total_price_label.show()
        #PUBLISHED YEAR ADDED
        add_book_year_input.resize(150,30)
        add_book_year_input.move(190,320)
        add_book_year_label.setText("PUBLISHED YEAR")
        add_book_year_label.move(190,300)
        add_book_year_label.show()

        #********************************************************
        #ISBN ADDED
        add_book_ISBN_input.resize(150,30)
        add_book_ISBN_input.move(350,20)
        add_book_ISBN_label.setText("ISBN(REQURIED)")
        add_book_ISBN_label.move(350,0)
        add_book_ISBN_label.show()
        #VOLUMES ADDED
        add_book_volumes_input.resize(150,30)
        add_book_volumes_input.move(350,70)
        add_book_volumes_label.setText("VOLUMES (REQURIED)")
        add_book_volumes_label.move(350,50)
        add_book_volumes_label.show()  
        #VOLUME ADDED   
        add_book_volume_input.resize(150,30)
        add_book_volume_input.move(350,120)
        add_book_volume_label.setText("VOLUME (REQURIED)")
        add_book_volume_label.move(350,100)
        add_book_volume_label.show()
        #COPIES_TOTAL
        add_book_copies_total_input.resize(150,30)
        add_book_copies_total_input.move(350,170)
        add_book_copies_total_label.setText("COPIES_TOTAL")
        add_book_copies_total_label.move(350,150)
        add_book_copies_total_label.show()
        #LANGUAGE ADDED
        add_book_language_input.resize(150,30)
        add_book_language_input.move(350,220)
        add_book_language_label.setText("LANGUAGE(REQURIED)")
        add_book_language_label.move(350,200)
        add_book_language_label.show()
        #STATUS ADDED
        add_book_status_input.resize(150,30)
        add_book_status_input.move(350,270)
        add_book_status_label.setText("STATUS(REQURIED)")
        add_book_status_label.move(350,250)
        add_book_status_label.show()
        #NOTES
        add_book_notes_input.resize(150,30)
        add_book_notes_input.move(350,320)
        add_book_notes_label.setText("NOTES")
        add_book_notes_label.move(350,300)
        add_book_notes_label.show()


    def add(self):
        last_row=backend.last_row()
        id=last_row[0]+1
        title=add_book_title_input.text()
        add_book_title_input.clear()
        category=add_book_category_input.text()
        add_book_category_input.clear()
        classification=add_book_classification_input.text()
        add_book_classification_input.clear()
        author=add_book_author_input.text()
        add_book_author_input.clear()
        transletor=add_book_transletor_input.text()
        add_book_transletor_input.clear()
        shelf=add_book_shelf_input.text()
        add_book_shelf_input.clear()
        row=add_book_row_input.text()
        add_book_row_input.clear()
        binding=add_book_binding_input.text()
        add_book_binding_input.clear()
        isbn=add_book_ISBN_input.text()
        add_book_ISBN_input.clear()
        volumes=add_book_volumes_input.text()
        add_book_volumes_input.clear()
        volume=add_book_volume_input.text()
        add_book_volume_input.clear()
        copies_total=add_book_copies_total_input.text()
        add_book_copies_total_input.clear()
        copies_available=add_book_copies_available_input.text()
        add_book_copies_available_input.clear()
        publication=add_book_publication_input.text()
        add_book_publication_input.clear()
        pages=add_book_pages_input.text()
        add_book_pages_input.clear()
        unit_price=add_book_unit_price_input.text()
        add_book_unit_price_input.clear()
        total_price=add_book_total_price_input.text()
        add_book_total_price_input.clear()
        year=add_book_year_input.text()
        add_book_year_input.clear()
        language=add_book_language_input.text()
        add_book_language_input.clear()
        status=add_book_status_input.text()
        add_book_status_input.clear()
        notes=add_book_notes_input.text()
        add_book_notes_input.clear()
        backend.ADD_BOOKS.add(id,title,category,classification,author,transletor,shelf,row,binding,isbn,volumes,volume,copies_total,copies_available,publication,pages,unit_price,total_price,year,language,status,notes)
        
class DELETE_BOOK:
    def __init__(self):
        delete_window.resize(200,100)
        delete_window.show()
        delete_book_input.resize(100,30)
        delete_book_input.move(50,20)
        delete_book_label.setText("Enter Title")
        delete_book_label.move(50,5)
        delete_book_label.show()
        delete_button.resize(100,40)
        delete_button.move(50,55)
        delete_button.setText("Delete")
    
    def delete():
        name_of_book=delete_book_input.text()
        delete_book_input.clear()
        backend.DELETE_BOOKS.delete(name_of_book)





    
            

    




#MAIN

show_search_button.clicked.connect(SEARCH_BOOK)
search_button.clicked.connect(SEARCH_BOOK.find_book)
show_add_button_window.clicked.connect(ADD_BOOK)
add_button.clicked.connect(ADD_BOOK.add)
show_delete_window.clicked.connect(DELETE_BOOK)
delete_button.clicked.connect(DELETE_BOOK.delete)
parameter_box.addItems([
    "ID",
    "TITLE",
    "CATEGORY",
    "CLASSIFICATION",
    "AUTHOR",
    "TRANSLATOR",
    "SHELF",
    "ROW",
    "BINDING",
    "ISBN",
    "NUMBER OF VOLUMES",
    "VOLUME",
    "COPIES_TOTAL",
    "COPIES_AVAILABLE",
    "PUBLICATION INFORMATION",
    "PAGES",
    "UNIT PRICE",
    "TOTAL PRICE",
    "PUBLISHED YEAR",
    "LANGUAGE",
    "STATUS",
    "NOTES"
    
])
parameter_box.resize(165,30)
parameter_box.move(20,20)
parameter_box.currentTextChanged.connect(update_search_box)
SHOW_BOOKS=SHOW_BOOK()




















