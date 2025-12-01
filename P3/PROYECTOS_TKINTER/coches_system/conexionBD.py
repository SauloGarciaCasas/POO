import mysql.connector

try:
    #Conectar con la BD en MySQL
    conexion=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='bd_cochecitos'
    )
    #Crear un objeto de tipo cursor que se pueda reutilizar nuevamente
    cursor=conexion.cursor(buffered=True)
except:
     print(f"Ocurrio un error con el Sistema por favor verifique ...")    
