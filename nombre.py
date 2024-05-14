import os

def rename_files(directory, start_num, increment):
    # Obtener la lista de archivos en el directorio
    files = os.listdir(directory)
    
    # Ordenar los archivos alfabéticamente
    files.sort()
    
    # Inicializar el contador para el nombre de archivo
    num = start_num
    
    # Iterar sobre los archivos y cambiarles el nombre
    for filename in files:
        # Construir el nuevo nombre de archivo
        new_filename = str(num) + os.path.splitext(filename)[1]
        
        # Construir la ruta completa del archivo antiguo y nuevo
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        
        # Renombrar el archivo
        os.rename(old_path, new_path)
        
        # Incrementar el contador
        num += increment

# Directorio donde se encuentran los archivos
#directory = 'C:\\Users\\redes\\Downloads\\12'
directory = r'C:\Users\redes\Downloads\12'
# Número inicial para el nombre de archivo
start_num = 12

# Incremento para el nombre de archivo (la razón)
increment = 5

# Llamar a la función para cambiar los nombres de los archivos
rename_files(directory, start_num, increment)
