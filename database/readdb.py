import mysql.connector
try:
    connection = mysql.connector.connect(host='localhost', database='cricketer', user='root', password='root')
    cursor = connection.cursor()
    sql_select_query = "select * from cricket"
    cursor.execute(sql_select_query)
    result_data = cursor.fetchall()
    print("Records of table is:")
    for row in result_data:
        print("cid:",row[0],end='\t\t')
        print("cname:",row[1],end='\t\t')
        print("country:",row[2])
    print("Rows completely fetched")
except Exception as e:
    print("exception",e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close
        print("connection closed succesfully")