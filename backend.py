import mysql.connector

class SHOW_BOOKS:
    def SHOW(self):
        self.conn=mysql.connector.connect(
            host='localhost ',
            port='3305',
            user='root',
            password='1234',
            database='library_management_system'
        )
        cursor=self.conn.cursor()
        query="SELECT * FROM BOOKS"
        cursor.execute(query)
        rows=cursor.fetchall()
        self.conn.close()
        return rows
    
class SEARCH_BOOKS:
    def SEARCH(self,book_name):
        conn=mysql.connector.connect(
            host='localhost ',
            port='3305',
            user='root',
            password='1234',
            database='library_management_system'
        )
        cursor=conn.cursor()
        query="SELECT ID FROM BOOKS WHERE TITLE = %s  "
        cursor.execute(query,(book_name,))
        result=cursor.fetchone()
        conn.close()
        if result:
            return True
        else:
            return False
    

    
class ADD_BOOKS:

    def ADD(self,id,title,author_name,category,isbn,published_year,language,copies_total,copies_available,shelf,status):
        conn=mysql.connector.connect(
        host='localhost',
        port='3305',
        user='root',
        password='1234',
        database='library_management_system'
        )
        cursor=conn.cursor()
        query="""INSERT INTO BOOKS (ID,TITLE,AUTHOR_NAME,CATEGORY,ISBN,PUBLISHED_YEAR,LANGUAGE,COPIES_TOTAL,COPIES_AVAILABLE,SHELF,STATUS)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(query,(id,title,author_name,category,isbn,published_year,language,copies_total,copies_available,shelf,status,))
        conn.commit()
        conn.close()

class DELETE_BOOKS:
    def DELETE(self,DELETED_BOOK):
        conn=mysql.connector.connect(
        host='localhost',
        port='3305',
        user='root',
        password='1234',
        database='library_management_system'
        )
        cursor=conn.cursor()
        cursor.execute("SET SQL_SAFE_UPDATES=0;")
        query="DELETE FROM  BOOKS WHERE TITLE = %s"
        cursor.execute(query,(DELETED_BOOK,))
        conn.commit()
        conn.close()
        


SHOW_BOOK=SHOW_BOOKS()
SEARCH_BOOK=SEARCH_BOOKS()
ADD_BOOK=ADD_BOOKS()
DELETE_BOOK=DELETE_BOOKS()


    
