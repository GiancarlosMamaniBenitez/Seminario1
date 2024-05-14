import os
import shutil

# Rutas de las carpetas de entrada y salida
carpeta_prueba1 = r"C:\Users\Giancarlos\Documents\Dataset\Dataset\images\train\platano"
carpeta_prueba2 = r"C:\Users\Giancarlos\Documents\Dataset\Dataset\data\label\platano"
carpeta_salida = r"C:\Users\Giancarlos\Documents\Dataset\Dataset\labels\train\platano"

# Asegurarse que la carpeta de salida existe
if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)

# Obtener la lista de archivos en la carpeta prueba1
archivos_prueba1 = os.listdir(carpeta_prueba1)

# Iterar sobre los archivos de prueba1
for archivo in archivos_prueba1:
    # Cambiar la extensión de .jpg a .txt
    nombre_base = os.path.splitext(archivo)[0]
    archivo_txt = nombre_base + ".txt"
    
    # Comprobar si el archivo también está en la carpeta prueba2
    ruta_archivo_prueba2 = os.path.join(carpeta_prueba2, archivo_txt)
    if os.path.exists(ruta_archivo_prueba2):
        # Copiar el archivo de prueba2 a la carpeta de salida
        shutil.copy(ruta_archivo_prueba2, os.path.join(carpeta_salida, archivo_txt))
        print(f"Archivo '{archivo_txt}' copiado a la carpeta de salida.")
    else:
        print(f"Archivo '{archivo_txt}' no encontrado en carpeta prueba2.")

print("Proceso completado.")
