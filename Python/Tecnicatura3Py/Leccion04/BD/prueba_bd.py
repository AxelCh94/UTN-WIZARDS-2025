import psycopg2 # Esto es para poder conecctarnos a Postgre

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database= 'test_bd'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia) # de esta manera ejecutamos la sentencia
            registro = cursor.fetchall() # Recuperamos todos los registros que seran una lista
            print(registro)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()