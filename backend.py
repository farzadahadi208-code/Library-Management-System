import sqlite3
def last_row():
    last=sqlite3.connect("Library Management System.db")
    cursor=last.cursor()
    cursor.execute("SELECT ID FROM BOOK WHERE ID >1 ORDER BY ID DESC LIMIT 1 ")
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
SHOW_BOOKS=SHOW_BOOK()
SEARCH_BOOKS=SEARCH_BOOK()
ADD_BOOKS=ADD_BOOK()


