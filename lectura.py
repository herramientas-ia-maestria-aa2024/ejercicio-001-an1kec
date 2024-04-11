# Abre el archivo en modo lectura
with open('informacion.txt', 'r') as archivo:
    # Lee el contenido del archivo
    contenido = archivo.read()
    # Imprime el contenido del archivo
    print(contenido)
