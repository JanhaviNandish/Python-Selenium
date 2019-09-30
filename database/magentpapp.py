
import mysql.connector
try:
    print("connecting to database")
    connection = mysql.connector.connect(host='localhost', database='magentodb', user='root', password='root')
    print("connected to database")
    cursor = connection.cursor()
    sql_insert_query = """insert into magentotb(`link`,`user`,`passw`) values ("https://account.magento.com/customer/account/login",'nitinmanjunath1991@gmai.com','Welcome123')"""
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