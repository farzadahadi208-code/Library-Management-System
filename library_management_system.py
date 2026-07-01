import mysql.connector

def SHOW_BOOK():
    conn=mysql.connector.connect(
        host='localhost ',
        port='3305',
        user='root',
        password='1234',
        database='library_management_system'
    )
    cursor=conn.cursor()
    query="SELECT * FROM BOOKS"
    cursor.execute(query)
    rows=cursor.fetchall()
    conn.close()
    return rows

def SEARCH_BOOKS(book_name):
    conn=mysql.connector.connect(
    host='localhost',
        port='3305',
        user='root',
        password='1234',
        database='library_management_system'
    )
    cursor=conn.cursor()
    query="SELECT ID FROM BOOKS WHERE TITLE = %s "
    cursor.execute(query,(book_name,))
    result=cursor.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False
    

def ADD_BOOKS(id,title,author_name,category,isbn,published_year,language,copies_total,copies_available,shelf,status):
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


def DELETE_BOOK(DELETED_BOOK):
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
        





    
