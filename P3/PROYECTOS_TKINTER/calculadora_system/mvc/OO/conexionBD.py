import mysql.connector

try:
    conexion=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='bd_operaciones_basicas'
    )
    cursor=conexion.cursor(buffered=True)
except:
     print(f"Ocurrio un error con el Sistema por favor verifique ...")