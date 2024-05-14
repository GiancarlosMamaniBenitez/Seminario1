import os
import shutil

# Rutas de las carpetas de entrada y salida
carpeta_prueba1 = r"C:\Users\redes\Downloads\prueba1"
carpeta_prueba2 = r"C:\Users\redes\Downloads\prueba2"
carpeta_salida = r"C:\Users\redes\Downloads\salida"

# Obtener la lista de archivos en la carpeta prueba1
archivos_prueba1 = os.listdir(carpeta_prueba1)

# Iterar sobre los archivos de prueba1
for archivo in archivos_prueba1:
    # Comprobar si el archivo también está en la carpeta prueba2
    if os.path.exists(os.path.join(carpeta_prueba2, archivo)):
        # Copiar el archivo de prueba2 a la carpeta de salida
        shutil.copy(os.path.join(carpeta_prueba2, archivo), carpeta_salida)
        print(f"Archivo '{archivo}' copiado a la carpeta de salida.")

print("Proceso completado.")