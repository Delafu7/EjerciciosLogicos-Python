"""/*
 * Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente
  * base de datos MySQL:
 * - Host: mysql-5707.dinaserver.com
 * - Port: 3306
 * - User: mouredev_read
 * - Password: mouredev_pass
 * - Database: moure_test
 *
 * Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
 * - SELECT * FROM `challenges`
 *
 * Se pueden usar librerías para realizar la lógica de conexión a la base de datos.
 */"""
import MySQLdb

def conectaryMostrar():
    try:
        # Establecer conexión con la base de datos
        database = MySQLdb.connect(
            host="mysql-5707.dinaserver.com",
            port=3306,
            user="mouredev_read",
            passwd="mouredev_pass",
            db="moure_test"
        )
        
        # Crear un cursor para ejecutar consultas
        cursor = database.cursor()
        # Ejecutar la consulta
        cursor.execute("SELECT * FROM `challenges`")
        
        # Obtener y mostrar los resultados
        for registro in cursor.fetchall():
            print(registro)
        
        # Cerrar el cursor y la conexión
        cursor.close()
        database.close()
    except MySQLdb.Error as e:
        print(f"Error al conectar o realizar una operación en la base de datos: {e}")

conectaryMostrar()
