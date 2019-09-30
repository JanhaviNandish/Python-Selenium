import mysql.connector
try:
    connection = mysql.connector.connect(host='localhost', database='cricketer', user='root', password='root')
    cursor = connection.cursor()
    sql_select_query = "select * from cricket where cid = '14'"
    cursor.execute(sql_select_query)
    result_data = cursor.fetchone()
    print("printing the record")
    print(result_data)
    print("Rows completely fetched")
except Exception as e:
    print("exception",e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close
        print("connection closed succesfully")