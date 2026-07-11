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
search_button=QPushButton(search_window)
search__parameter_label=QLabel(search_window)
search__name_label=QLabel(search_window)
search_input_parmeter=QLineEdit(search_window)
search_input_name=QLineEdit(search_window)


def update_search_box(text):
    search_input_parmeter.setText(text)


class SHOW_BOOK:
    def __init__(self):
        #creating table
        table.resize(1360,650)
        table.setColumnCount(22)
        table.setRowCount(30)
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


#MAIN
show_search_button.move(0,650)
show_search_button.resize(100,55)
show_search_button.setText("Search")
show_search_button.clicked.connect(SEARCH_BOOK)

search_button.clicked.connect(SEARCH_BOOK.find_book)
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




















