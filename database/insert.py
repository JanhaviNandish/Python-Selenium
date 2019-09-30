#to insert multiple rows into db
import mysql.connector
try:
    print("connecting to database")
    connection = mysql.connector.connect(host='localhost', database='cricketer', user='root', password='root')
    print("connected to database")
    cursor = connection.cursor(prepared=True)
    row_insert=[(12,'Rahul','India'),(14,'Ponting','Australia'),(17,'ABD','SouthAfrica')]
    sql_insert_query = """insert into cricket(cid,cname,country) values (%s,%s,%s)"""
    cursor.executemany(sql_insert_query,row_insert)
    connection.commit()
    print("no of rows updated is:",cursor.rowcount)
except Exception as e:
    print("Exception occured",e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close
        print("connection closed succesfully")