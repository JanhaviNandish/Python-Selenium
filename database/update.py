import mysql.connector
try:
    connection = mysql.connector.connect(host='localhost', database='cricketer', user='root', password='root')
    cursor = connection.cursor()

    print("the table content before deleting")
    sql_select_query = "select * from cricket"
    cursor.execute(sql_select_query)
    result_data = cursor.fetchall()
    print(result_data)

    sql_update_query= """update cricket set cname='Tendulkar' where cid='10'"""

    #sql_delete_query = """delete from cricket where cid='14'"""
    cursor.execute(sql_update_query)
    connection.commit()
    print()

    print("the table content after updating")
    cursor.execute(sql_select_query)
    result_data=cursor.fetchall()
    print(result_data)

except Exception as e:
    print("exception",e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close
        print("connection closed succesfully")