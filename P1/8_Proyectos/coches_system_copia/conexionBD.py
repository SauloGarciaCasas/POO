import mysql.connector

try:
    conexion=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='bd_cochecitos'
    )
    cursor=conexion.cursor(buffered=True)
except:
    print("Ocurrio un error")