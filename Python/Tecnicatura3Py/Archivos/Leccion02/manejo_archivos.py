# Declaramos una variable
try:
    archivo = open('prueba.txt', 'w') # La w es de write que sisgnifica escribir
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n') # \n es para salto de linea
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally: # siempre se ejecuta
    archivo.close() # Con esto se debe cerrar el archivo