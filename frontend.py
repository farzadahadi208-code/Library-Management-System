import sys 
import backend
from PyQt6.QtWidgets import  QApplication,QLabel,QMessageBox,QLineEdit,QPushButton,QComboBox,QWidget, QTableWidget,QTableWidgetItem
#CREATING OBJECTS
app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("Library Management System")
table=QTableWidget(window)
search_window=QWidget()
parameter_box=QComboBox(search_window)
message=QMessageBox()
#SEARCH CLASS OBJECTS
show_search_button=QPushButton(window)
show_search_button.move(0,650)
show_search_button.resize(100,55)
show_search_button.setText("Search Book")
search_window.setWindowTitle("Search Book")
search_button=QPushButton(search_window)
search__parameter_label=QLabel(search_window)
search__name_label=QLabel(search_window)
search_input_parmeter=QLineEdit(search_window)
search_input_name=QLineEdit(search_window)
show_result_table_of_search=QWidget()
#ADD CLASS OBJECTS

show_add_button_window=QPushButton(window)
show_add_button_window.resize(100,55)
show_add_button_window.move(110,650)
show_add_button_window.setText("Add Book")
add_book_window=QWidget()
add_book_window.setWindowTitle("Add Book")
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
#total_copies
add_book_total_copies_input=QLineEdit(add_book_window)
add_book_total_copies_label=QLabel(add_book_window)
#available_copies
add_book_available_copies_input=QLineEdit(add_book_window)
add_book_available_copies_label=QLabel(add_book_window)
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
#NOTES ADDED
add_book_notes_input=QLineEdit(add_book_window)
add_book_notes_label=QLabel(add_book_window)

#DELETE CLASS OBJECTS
show_delete_window=QPushButton(window)
show_delete_window.setText("Delete Book")
delete_window=QWidget()
delete_window.setWindowTitle("Delete Book")
delete_button=QPushButton(delete_window)
show_delete_window.resize(100,55)
show_delete_window.move(220,650)
delete_book_input=QLineEdit(delete_window)
delete_book_label=QLabel(delete_window)

#BORROW CLASS OBJECTS
show_borrow_window=QPushButton(window)
show_borrow_window.resize(100,55)
show_borrow_window.move(330,650)
show_borrow_window.setText("Borrow Book")
borrow_window=QWidget()
borrow_window.setWindowTitle("Borrow Book")
borrow_title_input=QLineEdit(borrow_window)
borrow_title_label=QLabel(borrow_window)
guaranty_button=QPushButton(borrow_window)
guarantyOption=QWidget()
passport_button=QPushButton(guarantyOption)
identityCard_button=QPushButton(guarantyOption)

#passport objects
passport_window=QWidget()
passport_window.setWindowTitle("Passport Information")
passport_Id_input=QLineEdit(passport_window)
passport_Id_label=QLabel(passport_window)

passport_name_input=QLineEdit(passport_window)
passport_name_label=QLabel(passport_window)

passport_nationality_input=QLineEdit(passport_window)
passport_nationality_label=QLabel(passport_window)

passport_date_of_birth_input=QLineEdit(passport_window)
passport_date_of_birth_label=QLabel(passport_window)

passport_place_of_birth_input=QLineEdit(passport_window)
passport_place_of_birth_label=QLabel(passport_window)

passport_date_of_issue_input=QLineEdit(passport_window)
passport_date_of_issue_label=QLabel(passport_window)

passport_date_of_expiry_input=QLineEdit(passport_window)
passport_date_of_expiry_label=QLabel(passport_window)

passport_date_of_receive_input=QLineEdit(passport_window)
passport_date_of_receive_label=QLabel(passport_window)

passport_date_of_return_input=QLineEdit(passport_window)
passport_date_of_return_label=QLabel(passport_window)

passport_book_input=QLineEdit(passport_window)
passport_book_label=QLabel(passport_window)

passport_confirmation_key=QPushButton(passport_window)

#identitycard
identityCard_window=QWidget()
identityCard_window.setWindowTitle("Identitycard Information")
identitycard_id_input=QLineEdit(identityCard_window)
identitycard_id_label=QLabel(identityCard_window)

identitycard_name_input=QLineEdit(identityCard_window)
identitycard_name_label=QLabel(identityCard_window)

identitycard_nationality_input=QLineEdit(identityCard_window)
identitycard_nationality_label=QLabel(identityCard_window)

identitycard_date_of_birth_input=QLineEdit(identityCard_window)
identitycard_date_of_birth_label=QLabel(identityCard_window)

identitycard_place_of_birth_input=QLineEdit(identityCard_window)
identitycard_place_of_birth_label=QLabel(identityCard_window)

identitycard_date_of_issue_input=QLineEdit(identityCard_window)
identitycard_date_of_issue_label=QLabel(identityCard_window)

identitycard_date_of_expiry_input=QLineEdit(identityCard_window)
identitycard_date_of_expiry_label=QLabel(identityCard_window)

identitycard_gender_input=QLineEdit(identityCard_window)
identitycard_gender_label=QLabel(identityCard_window)

identitycard_date_of_receive_input=QLineEdit(identityCard_window)
identitycard_date_of_receive_label=QLabel(identityCard_window)

identitycard_date_of_return_input=QLineEdit(identityCard_window)
identitycard_date_of_return_label=QLabel(identityCard_window)

identitycard_book_input=QLineEdit(identityCard_window)
identitycard_book_label=QLabel(identityCard_window)

identitycard_conformiton_key=QPushButton(identityCard_window)

#RETURN CLASS OBJECTS
show_return_window=QPushButton(window)
show_return_window.resize(100,55)
show_return_window.move(440,650)
show_return_window.setText("Return Book")
return_window=QWidget()
return_window.setWindowTitle("Return Book")
return_book_name_input=QLineEdit(return_window)
return_book_name_label= QLabel(return_window)

return_Confirmation_button=QPushButton(return_window)
return_Confirmation_button.setText("Ok")

show_window_option_select_passport_idetitycard=QWidget()
parameter_box1_return_window=QComboBox(show_window_option_select_passport_idetitycard)
return_parmeter_input=QLineEdit(show_window_option_select_passport_idetitycard)
return_parmeter_label=QLabel(show_window_option_select_passport_idetitycard)

return_id_input=QLineEdit(show_window_option_select_passport_idetitycard)
return_id_label=QLabel(show_window_option_select_passport_idetitycard)

return_Confirmation_detail_button=QPushButton(show_window_option_select_passport_idetitycard)

#EDIT CALSS OBJECTS
show_edit_window=QPushButton(window)
show_edit_window.setText("Edit Book")
show_edit_window.resize(100,55)
show_edit_window.move(550,650)

edit_window=QWidget()
edit_window.setWindowTitle("Edit Book")
edit_box_parameter_options=QComboBox(edit_window)
edit_name_of_book_input=QLineEdit(edit_window)
edit_name_of_book_lable=QLabel(edit_window)

edit_parameter_input=QLineEdit(edit_window)
edit_parameter_lable=QLabel(edit_window)

edit_isbn_input=QLineEdit(edit_window)
edit_isbn_lable=QLabel(edit_window)

edit_new_value_input=QLineEdit(edit_window)
edit_new_value_lable=QLabel(edit_window)

edit_confirmation_button=QPushButton(edit_window)

#SORT CLASS OBJECTS
show_sort_window=QPushButton(window)
show_sort_window.setText("Sort Books")
show_sort_window.resize(100,55)
show_sort_window.move(660,650)
sort_window=QWidget()
sort_window.setWindowTitle("Sort Books")
sort_sorted_parameter_box_options=QComboBox(sort_window)
sort_sorted_parameter_box_options.resize(115,30)
sort_sorted_parameter_box_options.move(20,30)
sort_method_box_options=QComboBox(sort_window)
sort_method_box_options.resize(115,30)
sort_method_box_options.move(140,30)
sort_sorted_parameter_input=QLineEdit(sort_window)
sort_sorted_parameter_label=QLabel(sort_window)
sort_method_input=QLineEdit(sort_window)
sort_method_label=QLabel(sort_window)
sort_confirmation_butthon=QPushButton(sort_window)
sorted_table_window=QWidget()
sorted_table=QTableWidget(sorted_table_window)

#PATRON CALSS OBJECTS
show_patron_window=QPushButton(window)
show_patron_window.setText("PATRON")
show_patron_window.resize(100,55)
show_patron_window.move(770,650)
patron_window=QWidget()
patron_window.setWindowTitle("Patron")
patron_name_input=QLineEdit(patron_window)
patron_name_label=QLabel(patron_window)
patron_father_name_input=QLineEdit(patron_window)
patron_father_name_label=QLabel(patron_window)
patron_duty_input=QLineEdit(patron_window)
patron_duty_label=QLabel(patron_window)
patron_university_input=QLineEdit(patron_window)
patron_university_label=QLabel(patron_window)
patron_semester_input=QLineEdit(patron_window)
patron_semester_label=QLabel(patron_window)
patron_major_input=QLineEdit(patron_window)
patron_major_label=QLabel(patron_window)
patron_book_input=QLineEdit(patron_window)
patron_book_label=QLabel(patron_window)
patron_confirmation_button=QPushButton(patron_window)

#CURRNT_PATRON CLASS OBJECTS
show_current_parton_button=QPushButton(window)
show_current_parton_button.setText("Current Patrons")
show_current_parton_button.resize(100,55)
show_current_parton_button.move(880,650)
current_patron_window=QWidget()
current_patron_window.setWindowTitle("Current Patron")
current_patrons=QTableWidget(current_patron_window)

show_current_patron_receive_book_window=QPushButton(current_patron_window)
current_patron_receive_book_window=QWidget()
current_patron_name_input=QLineEdit(current_patron_receive_book_window)
current_patron_name_label=QLabel(current_patron_receive_book_window)

current_patron_book_input=QLineEdit(current_patron_receive_book_window)
current_patron_book_label=QLabel(current_patron_receive_book_window)

current_patron_confirmation_button=QPushButton(current_patron_receive_book_window)

#REPORT CLASS OBJECTS
show_report_window=QPushButton(window)
show_report_window.setText("Report")
show_report_window.resize(100,55)
show_report_window.move(990,650)
report_window=QWidget()
report_window.setWindowTitle("Report")
report_book=QPushButton(report_window)
report_borrowed_book=QPushButton(report_window)
report_potrons=QPushButton(report_window)
report_deleted_book=QPushButton(report_window)
       
def update_sort_method_box_options(text):
    sort_method_input.setText(text)

def update_sort_sorted_parameter_box_options(text):
    sort_sorted_parameter_input.setText(text)

def update_edit_box_parameter_options(text):
    edit_parameter_input.setText(text)

def update_search_box(text):
    search_input_parmeter.setText(text)

def udpdate_return_parameter_box(text):
    return_parmeter_input.setText(text)
class SHOW_BOOK:
    def __init__(self):
        #creating table
        table.resize(1360,650)
        table.setColumnCount(21)
        table.setRowCount(10000)
        table.setHorizontalHeaderLabels(
            ["ID","TITLE","CATEGORY","CLASS","AUTHOR","TRANSLATOR","SHELF","ROW","BINDING","ISBN","VOLUMES","VOLUME","TOTAL_COPIES","AVAILABLE_COPIES","PUBLICATION","PAGES","UNIT PRICE","TOTAL PRICE","YEAR","LANGUAGE","NOTES"]
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
        search_result_table=QTableWidget(show_result_table_of_search)
        show_result_table_of_search.resize(500,300)
        show_result_table_of_search.show()
        search_result_table.resize(500,300)
        search_result_table.setColumnCount(21)
        search_result_table.setRowCount(20)
        search_result_table.setHorizontalHeaderLabels(
            ["ID","TITLE","CATEGORY","CLASS","AUTHOR","TRANSLATOR","SHELF","ROW","BINDING","ISBN","VOLUMES","VOLUME","TOTAL_COPIES","AVAILABLE_COPIES","PUBLICATION","PAGES","UNIT PRICE","TOTAL PRICE","YEAR","LANGUAGE","NOTES"]
        )
        search_table=backend.SEARCH_BOOKS.result(parameter,name)
        if search_table:
            for x,row in enumerate(search_table):
                for y,value in enumerate(row):
                    search_result_table.setItem(x,y,QTableWidgetItem(str(value)))

        search_window.close()

class ADD_BOOK:
    def __init__(self):
        add_book_window.resize(520,400)
        add_book_window.show()
        
        #TITLE ADDED
        add_book_title_input.resize(150,30)
        add_book_title_input.move(20,20)
        add_book_title_label.setText("TITLE (REQUIRED)")
        add_book_title_label.move(20,0)
        add_book_title_label.show()
        #CATEGORY ADDED
        add_book_category_input.resize(150,30)
        add_book_category_input.move(20,70)
        add_book_category_label.setText("CATEGORY(REQUIRED)")
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
        add_book_author_label.setText("AUTHOR(REQUIRED)")
        add_book_author_label.move(20,150)
        add_book_author_label.show()
        #available_copies
        add_book_available_copies_input.resize(150,30)
        add_book_available_copies_input.move(20,220)
        add_book_available_copies_label.setText("AVAILABLE_COPIES")
        add_book_available_copies_label.move(20,200)
        add_book_available_copies_label.show()
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
        add_book_shelf_label.setText("SHELF(REQUIRED)")
        add_book_shelf_label.move(190,50)
        add_book_shelf_label.show()
        #ROW ADDED
        add_book_row_input.resize(150,30)
        add_book_row_input.move(190,120)
        add_book_row_label.setText("ROW(REQUIRED)")
        add_book_row_label.move(190,100)
        add_book_row_label.show()
        #BINDING ADDED
        add_book_binding_input.resize(150,30)
        add_book_binding_input.move(190,170)
        add_book_binding_label.setText("BINDING(REQUIRED)")
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
        add_book_ISBN_label.setText("ISBN(REQUIRED)")
        add_book_ISBN_label.move(350,0)
        add_book_ISBN_label.show()
        #VOLUMES ADDED
        add_book_volumes_input.resize(150,30)
        add_book_volumes_input.move(350,70)
        add_book_volumes_label.setText("VOLUMES (REQUIRED)")
        add_book_volumes_label.move(350,50)
        add_book_volumes_label.show()  
        #VOLUME ADDED   
        add_book_volume_input.resize(150,30)
        add_book_volume_input.move(350,120)
        add_book_volume_label.setText("VOLUME (REQUIRED)")
        add_book_volume_label.move(350,100)
        add_book_volume_label.show()
        #total_copies
        add_book_total_copies_input.resize(150,30)
        add_book_total_copies_input.move(350,170)
        add_book_total_copies_label.setText("TOTAL_COPIES")
        add_book_total_copies_label.move(350,150)
        add_book_total_copies_label.show()
        #LANGUAGE ADDED
        add_book_language_input.resize(150,30)
        add_book_language_input.move(350,220)
        add_book_language_label.setText("LANGUAGE(REQUIRED)")
        add_book_language_label.move(350,200)
        add_book_language_label.show()
        #NOTES
        add_book_notes_input.resize(150,30)
        add_book_notes_input.move(350,270)
        add_book_notes_label.setText("NOTES")
        add_book_notes_label.move(350,250)
        add_book_notes_label.show()


    def add(self):
        id=backend.last_row("BOOK")
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
        total_copies=add_book_total_copies_input.text()
        add_book_total_copies_input.clear()
        available_copies=add_book_available_copies_input.text()
        add_book_available_copies_input.clear()
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
        notes=add_book_notes_input.text()
        add_book_notes_input.clear()
        backend.ADD_BOOKS.add(id,title,category,classification,author,transletor,shelf,row,binding,isbn,volumes,volume,total_copies,available_copies,publication,pages,unit_price,total_price,year,language,notes)
        SHOW_BOOK()
        add_book_window.close()

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
        SHOW_BOOK()
        delete_window.close()
    
class BORROW_BOOK:
    def __init__(self):
        borrow_window.resize(250,130)
        borrow_window.show()
        borrow_title_input.resize(100,30)
        borrow_title_input.move(75,30)
        borrow_title_label.setText("Please Enter Title")
        borrow_title_label.move(75,10)
        borrow_title_label.show()
        guaranty_button.setText("Guranty")
        guaranty_button.resize(100,30)
        guaranty_button.move(75,70)
        
        

  
    def status_of_book(self):
        title=borrow_title_input.text()
        backend.BORROW_BOOKS.status_of_book(title)
        status_of_wanted_book=backend.BORROW_BOOKS.confermation
        if status_of_wanted_book==0:
            guarantyOption.resize(260,80)
            guarantyOption.show()
            passport_button.setText("Passport")
            passport_button.resize(100,40)
            passport_button.move(20,20)
            identityCard_button.setText("Identity Card")
            identityCard_button.resize(100,40)
            identityCard_button.move(140,20)

        if status_of_wanted_book==1:
           message.warning(
               borrow_window,
               "Search",
               "This Book Does Not Exist"
           )
        if status_of_wanted_book==2:
            message.warning(
               borrow_window,
               "Search",
               "We Do Not Have Enough Copy Of This Book"
           )
        borrow_window.close()
            
        
    def Passport(self):
        passport_window.resize(360,300)
        passport_window.show()
        passport_Id_input.resize(100,30)
        passport_Id_input.move(20,30)
        passport_Id_label.setText("Passport_No")
        passport_Id_label.move(20,10)
        passport_Id_label.show()

        passport_name_input.resize(100,30)
        passport_name_input.move(20,90)
        passport_name_label.setText("Name")
        passport_name_label.move(20,70)
        passport_name_label.show()

        passport_nationality_input.resize(100,30)
        passport_nationality_input.move(20,150)
        passport_nationality_label.setText("Nationality")
        passport_nationality_label.move(20,130)
        passport_nationality_label.show()

#**********************************************************************
        passport_date_of_birth_input.resize(100,30)
        passport_date_of_birth_input.move(130,30)
        passport_date_of_birth_label.setText("Data Of Birth")
        passport_date_of_birth_label.move(130,10)
        passport_date_of_birth_label.show()

        passport_place_of_birth_input.resize(100,30)
        passport_place_of_birth_input.move(130,90)
        passport_place_of_birth_label.setText("Birth Of Place")
        passport_place_of_birth_label.move(130,70)
        passport_place_of_birth_label.show()
        
        
        passport_date_of_issue_input.resize(100,30)
        passport_date_of_issue_input.move(130,150)
        passport_date_of_issue_label.setText("Data Of Issue")
        passport_date_of_issue_label.move(130,130)
        passport_date_of_issue_label.show()

        passport_book_input.resize(100,30)
        passport_book_input.move(130,210)
        passport_book_label.setText("Name Of Book")
        passport_book_label.move(130,190)
        passport_book_label.show()
#****************************************************************

        passport_date_of_receive_input.resize(100,30)
        passport_date_of_receive_input.move(240,30)
        passport_date_of_receive_label.setText("Data Of Receive")
        passport_date_of_receive_label.move(240,10)
        passport_date_of_receive_label.show()

        passport_date_of_return_input.resize(100,30)
        passport_date_of_return_input.move(240,90)
        passport_date_of_return_label.setText("Data Of Return")
        passport_date_of_return_label.move(240,70)
        passport_date_of_return_label.show()

        passport_date_of_expiry_input.resize(100,30)
        passport_date_of_expiry_input.move(240,150)
        passport_date_of_expiry_label.setText("Date Of Expiry")
        passport_date_of_expiry_label.move(240,130)
        passport_date_of_expiry_label.show()

        passport_confirmation_key.resize(330,30)
        passport_confirmation_key.move(20,250)
        passport_confirmation_key.setText("Confirm The Information")
        
        guarantyOption.close()
        
    
    def savePassportInfo():
        id=passport_Id_input.text()
        name=passport_name_input.text()
        nationality=passport_nationality_input.text()
        date_of_birth=passport_date_of_birth_input.text()
        place_of_birth=passport_place_of_birth_input.text()
        date_of_issue=passport_date_of_issue_input.text()
        date_of_expiry=passport_date_of_expiry_input.text()
        date_of_receive=passport_date_of_receive_input.text()
        date_of_return=passport_date_of_return_input.text()
        book=passport_book_input.text()
        passport_window.close()
        set_information_to_passport_table=backend.BORROW_BOOKS.passportGuarante(id,name,nationality,date_of_birth,place_of_birth,date_of_issue,date_of_expiry,date_of_receive,date_of_return,book)
        SHOW_BOOK()

    def identiyCard(self):
        identityCard_window.resize(400,320)
        identityCard_window.show()

        identitycard_id_input.resize(100,30)
        identitycard_id_input.move(20,30)
        identitycard_id_label.setText("ID_Number")
        identitycard_id_label.move(20,10)
        identitycard_id_label.show()

        identitycard_name_input.resize(100,30)
        identitycard_name_input.move(20,90)
        identitycard_name_label.setText("Full Name")
        identitycard_name_label.move(20,70)
        identitycard_name_label.show()

        identitycard_nationality_input.resize(100,30)
        identitycard_nationality_input.move(20,150)
        identitycard_nationality_label.setText("Nationality")
        identitycard_nationality_label.move(20,130)
        identitycard_nationality_label.show()

        identitycard_gender_input.resize(100,30)
        identitycard_gender_input.move(20,210)
        identitycard_gender_label.setText("Gender")
        identitycard_gender_label.move(20,190)
        identitycard_gender_label.show()
        #**************************************************
        
        identitycard_date_of_birth_input.resize(100,30)
        identitycard_date_of_birth_input.move(130,30)
        identitycard_date_of_birth_label.setText("Date Of Birth")
        identitycard_date_of_birth_label.move(130,10)
        identitycard_date_of_birth_label.show()

        identitycard_place_of_birth_input.resize(100,30)
        identitycard_place_of_birth_input.move(130,90)
        identitycard_place_of_birth_label.setText("Place Of Birth")
        identitycard_place_of_birth_label.move(130,70)
        identitycard_place_of_birth_label.show()

        identitycard_date_of_issue_input.resize(100,30)
        identitycard_date_of_issue_input.move(130,150)
        identitycard_date_of_issue_label.setText("Date Of Issue")
        identitycard_date_of_issue_label.move(130,130)
        identitycard_date_of_issue_label.show()

        identitycard_date_of_expiry_input.resize(100,30)
        identitycard_date_of_expiry_input.move(130,210)
        identitycard_date_of_expiry_label.setText("Date Of Expiry")
        identitycard_date_of_expiry_label.move(130,190)
        identitycard_date_of_expiry_label.show()
        #******************************************************

        identitycard_date_of_receive_input.resize(100,30)
        identitycard_date_of_receive_input.move(240,30)
        identitycard_date_of_receive_label.setText("Date Of Receive")
        identitycard_date_of_receive_label.move(240,10)
        identitycard_date_of_receive_label.show()

        identitycard_date_of_return_input.resize(100,30)
        identitycard_date_of_return_input.move(240,90)
        identitycard_date_of_return_label.setText("Date Of Return")
        identitycard_date_of_return_label.move(240,70)
        identitycard_date_of_return_label.show()

        identitycard_book_input.resize(100,30)
        identitycard_book_input.move(240,150)
        identitycard_book_label.setText("Book")
        identitycard_book_label.move(240,130)
        identitycard_book_label.show()

        identitycard_conformiton_key.resize(340,30)
        identitycard_conformiton_key.move(20,250)
        identitycard_conformiton_key.setText("Confirm The Information")
        guarantyOption.close()
        

    def saveIdentityCardInfo(self):
        id=identitycard_id_input.text()
        name=identitycard_name_input.text()
        nationality=identitycard_nationality_input.text()
        date_of_birth=identitycard_date_of_birth_input.text()
        place_of_birth=identitycard_place_of_birth_input.text()
        date_of_issue=identitycard_date_of_issue_input.text()
        date_of_expiry=identitycard_date_of_expiry_input.text()
        gender=identitycard_gender_input.text()
        date_of_receive=identitycard_date_of_receive_input.text()
        date_of_return=identitycard_date_of_return_input.text()
        book=identitycard_book_input.text()
        identityCard_window.close()
        set_information_to_identityCard_table=backend.BORROW_BOOKS.identityCardGuarantuy(id,name,nationality,date_of_birth,place_of_birth,date_of_issue,date_of_expiry,gender,date_of_receive,date_of_return,book)
        SHOW_BOOK()

class RETURN_BOOK:
    def receive_book(self):
        return_window.resize(250,130)
        return_window.show()
        
        return_book_name_input.resize(100,30)
        return_book_name_input.move(75,40)
        return_book_name_label.setText("Enter Name Of Book")
        return_book_name_label.move(75,20)
        return_book_name_label.show()

        return_Confirmation_button.resize(100,30)
        return_Confirmation_button.move(75,90)

    def show_window_option_choice_passport_idetitycard(self):
        show_window_option_select_passport_idetitycard.resize(300,150)
        show_window_option_select_passport_idetitycard.show()


        return_parmeter_input.resize(100,30)
        return_parmeter_input.move(20,30)
        return_parmeter_label.setText("Choice Parameter")
        return_parmeter_label.move(20,10)
        return_parmeter_label.show()

        return_id_input.resize(150,30)
        return_id_input.move(140,30)
        return_id_label.setText("Passport ID/Identity Number")
        return_id_label.move(140,10)
        return_id_label.show()

        return_Confirmation_detail_button.resize(100,40)
        return_Confirmation_detail_button.move(100,80)
        return_Confirmation_detail_button.setText("Confirm Detail")
        return_window.close()

    def received_book(self):
        book_name=return_book_name_input.text()
        id=return_id_input.text()
        guaranty=return_parmeter_input.text()
        backend.RETURN_BOOKS.recive_book(book_name,id,guaranty)
        show_window_option_select_passport_idetitycard.close()
        SHOW_BOOK()


class EDIT_BOOK:
    def edit_book(self):
        edit_window.resize(260,190)
        edit_window.show()

        edit_name_of_book_input.resize(100,30)
        edit_name_of_book_input.move(20,30)
        edit_name_of_book_lable.setText("Enter Name Of Book")
        edit_name_of_book_lable.move(20,10)
        edit_name_of_book_lable.show()

        edit_parameter_input.resize(100,30)
        edit_parameter_input.move(140,30)
        edit_parameter_lable.setText("Enter Parameter")
        edit_parameter_lable.move(140,10)
        edit_parameter_lable.show()

        edit_isbn_input.resize(100,30)
        edit_isbn_input.move(20,90)
        edit_isbn_lable.setText("Enter isbn")
        edit_isbn_lable.move(20,70)
        edit_isbn_lable.show()

        edit_new_value_input.resize(100,30)
        edit_new_value_input.move(140,90)
        edit_new_value_lable.setText("Enter New Value")
        edit_new_value_lable.move(140,70)
        edit_new_value_lable.show()

        edit_confirmation_button.resize(100,40)
        edit_confirmation_button.setText("Confirm Detail")
        edit_confirmation_button.move(75,130)

    def implement_edition(self):
        edit_name_of_book=edit_name_of_book_input.text()
        parameter=edit_parameter_input.text()
        isbn=edit_isbn_input.text()
        new_value=edit_new_value_input.text()
        backend.EDIT_BOOKS.edit_book(edit_name_of_book,parameter,isbn,new_value)
        edit_window.close()
        SHOW_BOOK()


class SORTED_BOOK:
    def sort_book(self):
        sort_window.resize(270,130)
        sort_window.show()

        sort_sorted_parameter_input.resize(100,30)
        sort_sorted_parameter_input.move(20,30)
        sort_sorted_parameter_label.setText("Sorted Parametr")
        sort_sorted_parameter_label.move(20,10)
        sort_sorted_parameter_label.show()

        sort_method_input.resize(100,30)
        sort_method_input.move(140,30)
        sort_method_label.setText("Method")
        sort_method_label.move(140,10)
        sort_method_label.show()

        sort_confirmation_butthon.resize(100,40)
        sort_confirmation_butthon.move(75,70)
        sort_confirmation_butthon.setText("Sort")
    def implement_sort(self):
        sorted_parameter=sort_sorted_parameter_input.text()
        method=sort_method_input.text()
        table_is_sorted=backend.SORT_BOOKS.sort_book(sorted_parameter,method)
        sorted_table_window.resize(1000,500)
        sorted_table_window.show()
        sorted_table.resize(1000,500)
        sorted_table.setColumnCount(21)
        sorted_table.setRowCount(10000)
        sorted_table.setHorizontalHeaderLabels(
            ["ID","TITLE","CATEGORY","CLASS","AUTHOR","TRANSLATOR","SHELF","ROW","BINDING","ISBN","VOLUMES","VOLUME","TOTAL_COPIES","AVAILABLE_COPIES","PUBLICATION","PAGES","UNIT PRICE","TOTAL PRICE","YEAR","LANGUAGE","NOTES"]
        )
        for i,row in enumerate(table_is_sorted):
            for j,value in enumerate(row):
                sorted_table.setItem(i,j,QTableWidgetItem(str(value)))
        sorted_table.resizeColumnsToContents()
        sort_window.close()

class PATRON:
    def patron(self):
        patron_window.resize(250,260)
        patron_window.show()

        patron_name_input.resize(100,30)
        patron_name_input.move(20,30)
        patron_name_label.setText("Name")
        patron_name_label.move(20,10)
        patron_name_label.show()

        patron_father_name_input.resize(100,30)
        patron_father_name_input.move(20,80)
        patron_father_name_label.setText("Father`s Name")
        patron_father_name_label.move(20,60)
        patron_father_name_label.show()

        patron_duty_input.resize(100,30)
        patron_duty_input.move(20,130)
        patron_duty_label.setText("Duty")
        patron_duty_label.move(20,110)
        patron_duty_label.show()

        patron_book_input.resize(100,30)
        patron_book_input.move(20,180)
        patron_book_label.setText("Book")
        patron_book_label.move(20,160)
        patron_book_label.show()
#**********************************************
        patron_university_input.resize(100,30)
        patron_university_input.move(130,30)
        patron_university_label.setText("University")
        patron_university_label.move(130,10)
        patron_university_label.show()

        patron_semester_input.resize(100,30)
        patron_semester_input.move(130,80)
        patron_semester_label.setText("Semester")
        patron_semester_label.move(130,60)
        patron_semester_label.show()

        patron_major_input.resize(100,30)
        patron_major_input.move(130,130)
        patron_major_label.setText("Major")
        patron_major_label.move(130,110)
        patron_major_label.show()
        patron_confirmation_button.setText("Confirm Informations")
        patron_confirmation_button.resize(210,30)
        patron_confirmation_button.move(20,220)

    def saveInformationsOfPatrons(self):
        name=patron_name_input.text()
        father_name=patron_father_name_input.text()
        duty=patron_duty_input.text()
        university=patron_university_input.text()
        semester=patron_semester_input.text()
        major=patron_major_input.text()
        book=patron_book_input.text()
        backend.PARTONS.parton(name,father_name,duty,university,semester,major,book)
        patron_window.close()

class CURRENT_PATRON:
    def currentPatron(self):
        current_patron_window.resize(740,300)
        current_patron_window.show()
        show_current_patron_receive_book_window.setText("Receive Book")
        show_current_patron_receive_book_window.resize(750,30)
        show_current_patron_receive_book_window.move(0,260)
        current_patron=backend.CURRENT_PATRONS.currentpatron()
        current_patrons.resize(740,250)
        current_patrons.setColumnCount(11)
        current_patrons.setRowCount(100)
        current_patrons.setHorizontalHeaderLabels(
            [
                "ID","NAME","FATHER_NAME","DUTY","UNIVERSITY","SEMESTER","MAJOR","DATE","BOOK","TIME_OF_RECEIVE","RECEIVED BOOK"
            ]
        )
        for x,row in enumerate(current_patron):
            for y,value in enumerate(row):
                current_patrons.setItem(x,y,QTableWidgetItem(str(value)))
        current_patrons.resizeColumnsToContents()

    def receive_book(self):
        current_patron_receive_book_window.resize(250,110)
        current_patron_receive_book_window.show()

        current_patron_name_input.resize(100,30)
        current_patron_name_input.move(20,30)
        current_patron_name_label.setText("Name Of Potron")
        current_patron_name_label.move(20,10)
        current_patron_name_label.show()

        current_patron_book_input.resize(100,30)
        current_patron_book_input.move(130,30)
        current_patron_book_label.setText("Name Of Book")
        current_patron_book_label.move(130,10)
        current_patron_book_label.show()
        current_patron_confirmation_button.setText("Receive Book")
        current_patron_confirmation_button.resize(100,30)
        current_patron_confirmation_button.move(75,70)
        current_patron_window.close()
    def delete_patron(self):
        name=current_patron_name_input.text()
        book=current_patron_book_input.text()
        backend.CURRENT_PATRONS.recieve_book(name,book)
        current_patron_receive_book_window.close() 
        
        

class REPORT: 
    def show_options(self):
        report_window.resize(200,220)
        report_window.show()
        report_book.setText("Book")
        report_book.resize(100,30)
        report_book.move(50,30)

        report_borrowed_book.setText("Borrowed Book")
        report_borrowed_book.resize(100,30)
        report_borrowed_book.move(50,70)

        report_potrons.setText("Patrons")
        report_potrons.resize(100,30)
        report_potrons.move(50,110)

        report_deleted_book.setText("Deleted Book")
        report_deleted_book.resize(100,30)
        report_deleted_book.move(50,150)
    def report_of_all_book(self):
        backend.REPORTS.report_of_all_book()
        report_window.close()

    def report_of_borrowed_book(self):
        backend.REPORTS.borrowed_book_by_passport()
        backend.REPORTS.borrowed_book_by_identitycard()
        report_window.close()

    def report_of_patron(self):
        backend.REPORTS.report_of_patron()
        report_window.close()

    def report_deleted_book(self):
        report_window.close()
        backend.REPORTS.report_of_deleted_book()
        
        
#MAIN

show_search_button.clicked.connect(SEARCH_BOOK)
search_button.clicked.connect(SEARCH_BOOK.find_book)
show_add_button_window.clicked.connect(ADD_BOOK)
add_button.clicked.connect(ADD_BOOK.add)
show_delete_window.clicked.connect(DELETE_BOOK)
delete_button.clicked.connect(DELETE_BOOK.delete)

show_borrow_window.clicked.connect(BORROW_BOOK)
guaranty_button.clicked.connect(BORROW_BOOK.status_of_book)
passport_button.clicked.connect(BORROW_BOOK.Passport)
identityCard_button.clicked.connect(BORROW_BOOK.identiyCard)
passport_confirmation_key.clicked.connect(BORROW_BOOK.savePassportInfo)
identitycard_conformiton_key.clicked.connect(BORROW_BOOK.saveIdentityCardInfo)

show_return_window.clicked.connect(RETURN_BOOK.receive_book)
return_Confirmation_button.clicked.connect(RETURN_BOOK.show_window_option_choice_passport_idetitycard)
return_Confirmation_detail_button.clicked.connect(RETURN_BOOK.received_book)

show_edit_window.clicked.connect(EDIT_BOOK.edit_book)
edit_confirmation_button.clicked.connect(EDIT_BOOK.implement_edition)

show_sort_window.clicked.connect(SORTED_BOOK.sort_book)
sort_confirmation_butthon.clicked.connect(SORTED_BOOK.implement_sort)

show_patron_window.clicked.connect(PATRON.patron)
patron_confirmation_button.clicked.connect(PATRON.saveInformationsOfPatrons)

show_current_parton_button.clicked.connect(CURRENT_PATRON.currentPatron)
show_current_patron_receive_book_window.clicked.connect(CURRENT_PATRON.receive_book)
current_patron_confirmation_button.clicked.connect(CURRENT_PATRON.delete_patron)

show_report_window.clicked.connect(REPORT.show_options)
report_book.clicked.connect(REPORT.report_of_all_book)
report_borrowed_book.clicked.connect(REPORT.report_of_borrowed_book)
report_potrons.clicked.connect(REPORT.report_of_patron)
report_deleted_book.clicked.connect(REPORT.report_deleted_book)
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
    "TOTAL_COPIES",
    "AVAILABLE_COPIES",
    "PUBLICATION INFORMATION",
    "PAGES",
    "UNIT PRICE",
    "TOTAL PRICE",
    "PUBLISHED YEAR",
    "LANGUAGE",
    "NOTES"
    
])
parameter_box.currentTextChanged.connect(update_search_box)
parameter_box.resize(165,30)
parameter_box.move(20,20)

parameter_box1_return_window.resize(115,30)
parameter_box1_return_window.move(20,30)
parameter_box1_return_window.addItems(
    [
        "Passport",
        "IdentityCard"
    ]
)
parameter_box1_return_window.currentTextChanged.connect(udpdate_return_parameter_box)
sort_sorted_parameter_box_options.addItems(
    [
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
    "TOTAL_COPIES",
    "AVAILABLE_COPIES",
    "PUBLICATION INFORMATION",
    "PAGES",
    "UNIT PRICE",
    "TOTAL PRICE",
    "PUBLISHED YEAR",
    "LANGUAGE"
    ]
)

sort_sorted_parameter_box_options.currentTextChanged.connect(update_sort_sorted_parameter_box_options)
sort_method_box_options.addItems(
    [
        "ASCD",
        "DESC"
    ]
)
sort_method_box_options.currentTextChanged.connect(update_sort_method_box_options)
edit_box_parameter_options.resize(115,30)
edit_box_parameter_options.move(140,30)
edit_box_parameter_options.currentTextChanged.connect(update_edit_box_parameter_options)
edit_box_parameter_options.addItems(
    [
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
    "TOTAL_COPIES",
    "AVAILABLE_COPIES",
    "PUBLICATION INFORMATION",
    "PAGES",
    "UNIT PRICE",
    "TOTAL PRICE",
    "PUBLISHED YEAR",
    "LANGUAGE"
    ]
)
SHOW_BOOKS=SHOW_BOOK()



