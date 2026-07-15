import sqlite3
def last_row():
    last=sqlite3.connect("Library Management System.db")
    cursor=last.cursor()
    cursor.execute(f"SELECT ID FROM BOOK WHERE ID >1 ORDER BY ID DESC LIMIT 1 ")
    res=cursor.fetchone()
    last.close()
    return res

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

        conn=sqlite3.connect("Library Management System.db")
        cursor=conn.cursor()
        query="""INSERT INTO passportinfo (passport_NO,FULL_NAME,NATIONALITY,DATE_OF_BIRTH,PLACE_OF_BIRTH,DATE_OF_ISSUE,DATE_OF_EXPIRY,DATE_OF_RECEIVE,DATE_OF_RETURN,BOOK)
        VALUES (?,?,?,?,?,?,?,?,?,?,?) """
        cursor.execute(query,(passport_no,fullname,nationality,date_of_birth,place_of_birth,date_of_issue,date_of_expiry,DATE_OF_RECEIVE,DATE_OF_RETURN,Book,))
        conn.commit()
        conn.close()

    def identityCardGuarantuy(self,ID_NUMBER,FULLNAME,NATIONALITY,DATE_OF_BIRTH,PLACE_OF_BIRTH,DATE_OF_ISSUE,DATE_OF_EXPIRY,GENDER,DATE_OF_RECEIVE,DATE_OF_RETURN,Book):
        conn=sqlite3.connect("Library Management System.db")
        cursor=conn.cursor()
        query="""INSERT INTO IDENTITYCARD (ID_NUMBER,FULLNAME,NATIONALITY,DATE_OF_BIRTH,PLACE_OF_BIRTH,DATE_OF_ISSUE,DATE_OF_EXPIRY,GENDER,DATE_OF_RECEIVE,DATE_OF_RETURN,BOOK)
        VALUES (?,?,?,?,?,?,?,?,?,?,?)
        """
        cursor.execute(query,(ID_NUMBER,FULLNAME,NATIONALITY,DATE_OF_BIRTH,PLACE_OF_BIRTH,DATE_OF_ISSUE,DATE_OF_EXPIRY,GENDER,DATE_OF_RECEIVE,DATE_OF_RETURN,Book,))
        conn.commit()
        conn.close()

   


    



SHOW_BOOKS=SHOW_BOOK()
SEARCH_BOOKS=SEARCH_BOOK()
ADD_BOOKS=ADD_BOOK()
DELETE_BOOKS=DELETE_BOOK()
BORROW_BOOKS=BORROW_BOOK()




