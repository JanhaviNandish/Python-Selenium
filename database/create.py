#insert one row into the table
import mysql.connector

try:
    print("connecting to database")
    connection = mysql.connector.connect(host='localhost', database='cricketer', user='root', password='root')
    print("connected to database")
    cursor = connection.cursor()
    sql_insert_query = """insert into cricket(`cid`,`cname`,`country`) values (10,'sachin','India')"""
    cursor.execute(sql_insert_query)
    connection.commit()
    print("row inserted")

except Exception as e:
    print("Exception occured",e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close
        print("connection closed succesfully")