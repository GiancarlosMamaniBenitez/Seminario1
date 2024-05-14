import os

def check_duplicates(folder1, folder2, folder3):
    # Leer los nombres de archivos de cada carpeta
    files1 = set(os.listdir(folder1))
    files2 = set(os.listdir(folder2))
    files3 = set(os.listdir(folder3))

    # Encuentra intersecciones (archivos duplicados) entre las carpetas
    duplicates = files1.intersection(files2).union(files1.intersection(files3)).union(files2.intersection(files3))

    if duplicates:
        print(f"Hay {len(duplicates)} archivos repetidos.")
        for file in duplicates:
            print(file)
    else:
        print("No hay archivos repetidos.")

# Definir las rutas a las carpetas
folder_path1 = r'C:\Users\Giancarlos\Documents\Dataset\Dataset\images\train\platano'
folder_path2 = r'C:\Users\Giancarlos\Documents\Dataset\Dataset\images\val\platano'
folder_path3 = r'C:\Users\Giancarlos\Documents\Dataset\Dataset\images\test\platano'

# Llamar a la función
check_duplicates(folder_path1, folder_path2, folder_path3)
