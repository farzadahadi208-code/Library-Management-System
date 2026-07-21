import sqlite3
from datetime import datetime
def last_row(table):
    last=sqlite3.connect("Library Management System.db")
    cursor=last.cursor()
    cursor.execute(f"SELECT ID FROM {table} ORDER BY ID DESC LIMIT 1 ")
    res=cursor.fetchone()
    new_id=0
    if res is None:
        new_id=1
    else:
        new_id=res[0]+1
    last.close()
    return new_id

class SHOW_BOOK:
    def disply_book(self):
        conn=sqlite3.connect("Library Management System.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM BOOK")
        rows=cursor.fetchall()
        conn.close()
        return rows
        


class SEARCH_BOOK:
    def result(self,parameter,name):
        conn=sqlite3.connect("Library Management System.db")
        cursor=conn.cursor()
        cursor.execute(f"SELECT * FROM BOOK WHERE {parameter} = ? ",(name,) )
        show_result=cursor.fetchone()
        conn.close()
        return show_result



class ADD_BOOK:
    def add(self,ID,TITLE,CATEGORY,CLASSIFICATION,AUTHOR,TRANSLATOR,SHELF,ROW,BINDING,ISBN,VOLUMES,VOLUME,COPIES_TOTAL,COPIES_AVAILABLE,PUBLICATION_INFORMATION,PAGES,UNIT_PRICE,TOTAL_PRICE,YEAR,LANGUAGE,STATUS,NOTES):
        conn=sqlite3.connect("Library Management System.db")
        cursor=conn.cursor()
        query="""
            INSERT INTO BOOK (ID,TITLE,CATEGORY,CLASSIFICATION,AUTHOR,TRANSLATOR,SHELF,ROW,BINDING,ISBN,VOLUMES,VOLUME,COPIES_TOTAL,COPIES_AVAILABLE,PUBLICATION_INFORMATION,PAGES,UNIT_PRICE,TOTAL_PRICE,YEAR,LANGUAGE,STATUS,NOTES)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """
        
        cursor.execute(query,(ID,TITLE,CATEGORY,CLASSIFICATION,AUTHOR,TRANSLATOR,SHELF,ROW,BINDING,ISBN,VOLUMES,VOLUME,COPIES_TOTAL,COPIES_AVAILABLE,PUBLICATION_INFORMATION,PAGES,UNIT_PRICE,TOTAL_PRICE,YEAR,LANGUAGE,STATUS,NOTES,))
        conn.commit()
        conn.close()

class DELETE_BOOK(SEARCH_BOOK):
    def delete(self,deleted_book):
        SEARCH_BOOKS=SEARCH_BOOK()
        target=SEARCH_BOOKS.result("TITLE",deleted_book)
        conn=sqlite3.connect("Library Management System.db")
        cursor=conn.cursor()
        query="DELETE FROM BOOK WHERE ID = ?"
        id=target[0]
        cursor.execute(query,(id,))
        conn.commit()
        conn.close()

class BORROW_BOOK(SEARCH_BOOK):
    def status_of_book(self,name_of_book):
        self.confermation=0
        #self.confermation=0 means we can borrow the book
        #self.confermation=1 means this book does not exist
        #self.confermation=2 means we do not have enough book
        SEARCH_BOOKS=SEARCH_BOOK()
        self.status=SEARCH_BOOKS.result("TITLE",name_of_book)
        
        if self.status:
            pass
        else:
            self.confermation=1
            return 1
        
        copies_availabel=self.status[13]

        if copies_availabel>2:
            pass
        else:
            self.confermation=2
            return 1
    
    def passportGuarante(self,passport_no,fullname,nationality,date_of_birth,place_of_birth,date_of_issue,date_of_expiry,DATE_OF_RECEIVE,DATE_OF_RETURN,Book):
        is_received="No"
        id=last_row("PASSPORT")
        conn=sqlite3.connect("Library Management System.db")
        cursor=conn.cursor()
        query="""INSERT INTO PASSPORT (id,passport_NO,FULL_NAME,NATIONALITY,DATE_OF_BIRTH,PLACE_OF_BIRTH,DATE_OF_ISSUE,DATE_OF_EXPIRY,DATE_OF_RECEIVE,DATE_OF_RETURN,BOOK,IS_RECEIVED)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?) """
        cursor.execute(query,(id,passport_no,fullname,nationality,date_of_birth,place_of_birth,date_of_issue,date_of_expiry,DATE_OF_RECEIVE,DATE_OF_RETURN,Book,is_received,))
        conn.commit()
        conn.close()

    def identityCardGuarantuy(self,ID_NUMBER,FULLNAME,NATIONALITY,DATE_OF_BIRTH,PLACE_OF_BIRTH,DATE_OF_ISSUE,DATE_OF_EXPIRY,GENDER,DATE_OF_RECEIVE,DATE_OF_RETURN,Book):
        id=last_row("IDENTITYCARD")
        is_received="No"
        conn=sqlite3.connect("Library Management System.db")
        cursor=conn.cursor()
        query="""INSERT INTO IDENTITYCARD (id,ID_NUMBER,FULLNAME,NATIONALITY,DATE_OF_BIRTH,PLACE_OF_BIRTH,DATE_OF_ISSUE,DATE_OF_EXPIRY,GENDER,DATE_OF_RECEIVE,DATE_OF_RETURN,BOOK,IS_RECEIVED)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        """
        cursor.execute(query,(id,ID_NUMBER,FULLNAME,NATIONALITY,DATE_OF_BIRTH,PLACE_OF_BIRTH,DATE_OF_ISSUE,DATE_OF_EXPIRY,GENDER,DATE_OF_RECEIVE,DATE_OF_RETURN,Book,is_received,))
        conn.commit()
        conn.close()

   
class RETURN_BOOK:
    def recive_book(self,book_name,id,guaranty):
        #id is the id number of Identity card or the Passport_no
        conn=sqlite3.connect("Library Management System.db")
        cursor=conn.cursor()
        counter=0
        if guaranty=="IdentityCard":
            cursor.execute
            query=f"UPDATE IDENTITYCARD SET IS_RECEIVED='YES' WHERE ID_NUMBER= ? AND BOOK=?"
            cursor.execute(query,(id,book_name,))
            conn.commit()
            conn.close()
            return 1
        if guaranty=="Passport":
            query=f"UPDATE PASSPORT SET IS_RECEIVED ='YES' WHERE Passport_NO =? AND BOOK= ?"
            cursor.execute(query,(id,book_name,))
            conn.commit()
            conn.close()
            return 1

class EDIT_BOOK(SEARCH_BOOK):
    def edit_book(self,name,parameter,isbn,new_value):
        SEARCH_BOOKS=SEARCH_BOOK()
        status_of_book=SEARCH_BOOKS.result("TITLE",name)
        conn=sqlite3.connect("Library Management System.db")
        cursor=conn.cursor()
        query=f"UPDATE BOOK SET {parameter} = ? WHERE TITLE = ?"
        query1=f"UPDATE BOOK SET {parameter} = ? WHERE ISBN = ?"
        if status_of_book is None:
            print("this book does not exist")
            return 1
        elif isbn=="":
            cursor.execute(query,(new_value,name,))
        else:
            cursor.execute(query1,(new_value,isbn,))
        conn.commit()
        conn.close()


class SORT_BOOK:
    def sort_book(self,sorted_parameter,method=""):
        conn=sqlite3.connect("Library Management System.db")
        cursor=conn.cursor()
        query=f"SELECT * FROM BOOK ORDER BY {sorted_parameter}"
        query1=f"SELECT * FROM BOOK ORDER BY {sorted_parameter} DESC"
        if method=="DESC":
            cursor.execute(query1)
        else:
            cursor.execute(query)
        sorted_table=cursor.fetchall()
        return sorted_table

class PATRON:
    def parton(self,name,father_name,duty,university,semester,major,book):
        id=last_row("PATRON")
        date=str(datetime.now().date())
        time_of_receive=str(datetime.now().time())
        conn=sqlite3.connect("Library Management System.db")
        cursor=conn.cursor()
        query="""INSERT INTO PATRON (ID,NAME,FATHER_NAME,DUTY,UNIVERSITY,SEMESTER,MAJOR,BOOK,DATE,TIME_OF_RECEIVE)
        VALUES (?,?,?,?,?,?,?,?,?,?)
        """
        cursor.execute(query,(id,name,father_name,duty,university,semester,major,book,date,time_of_receive,))
        conn.commit()
        conn.close()

class CURRENT_PATRON:
    def currentpatron(self):
        date=datetime.now().date()
        conn=sqlite3.connect("Library Management System.db")
        cursor=conn.cursor()
        query1="DELETE FROM CURRENTPATRON;"
        query2="""
        INSERT INTO CURRENTPATRON (ID,NAME,FATHER_NAME,DUTY,UNIVERSITY,SEMESTER,MAJOR,DATE,BOOK,TIME_OF_RECEIVE,RECEIVED_BOOK)
        SELECT ID,NAME,FATHER_NAME,DUTY,UNIVERSITY,SEMESTER,MAJOR,DATE,BOOK,TIME_OF_RECEIVE,RECEIVED_BOOK FROM PATRON WHERE DATE=?
        """
        query3="SELECT * FROM CURRENTPATRON"
        cursor.execute(query1)
        cursor.execute(query2,(date,))
        cursor.execute(query3)
        currentpatron_table=cursor.fetchall()
        conn.commit()
        conn.close()
        return currentpatron_table
    def recieve_book(self,name,book):
        conn=sqlite3.connect("Library Management System.db")
        cursor=conn.cursor()
        query="UPDATE PATRON SET RECEIVED_BOOK='Received' WHERE NAME= ? AND BOOK=?"
        cursor.execute(query,(name,book,))
        conn.commit()
        conn.close()



SHOW_BOOKS=SHOW_BOOK()
SEARCH_BOOKS=SEARCH_BOOK()
ADD_BOOKS=ADD_BOOK()
DELETE_BOOKS=DELETE_BOOK()
BORROW_BOOKS=BORROW_BOOK()
RETURN_BOOKS=RETURN_BOOK()
EDIT_BOOKS=EDIT_BOOK()
SORT_BOOKS=SORT_BOOK()
PARTONS=PATRON()
CURRENT_PATRONS=CURRENT_PATRON()



