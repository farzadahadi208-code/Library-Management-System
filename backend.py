import sqlite3
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


SHOW_BOOKS=SHOW_BOOK()
SEARCH_BOOKS=SEARCH_BOOK()
