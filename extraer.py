import os
import shutil
import random

def copy_images(source_dir, target_dir, num_images):
    """
    Copia una cantidad espec�fica de im�genes de un directorio a otro.

    Args:
    source_dir (str): El directorio fuente de donde se copiar�n las im�genes.
    target_dir (str): El directorio destino donde se guardar�n las im�genes.
    num_images (int): N�mero de im�genes a copiar.
    """

    # Aseg�rate de que el directorio fuente existe
    if not os.path.exists(source_dir):
        print(f"El directorio fuente {source_dir} no existe.")
        return

    # Crea el directorio destino si no existe
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Obt�n todos los archivos en el directorio fuente
    files = [os.path.join(source_dir, file) for file in os.listdir(source_dir) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    if len(files) < num_images:
        print(f"Solo se encontraron {len(files)} im�genes, que es menos de las {num_images} requeridas para copiar.")
        num_images = len(files)  # Reducir el n�mero si hay menos archivos disponibles

    # Selecciona aleatoriamente im�genes a copiar
    selected_files = random.sample(files, num_images)

    # Copia los archivos seleccionados al directorio destino
    for file in selected_files:
        shutil.copy(file, target_dir)
        print(f"Copiado {file} a {target_dir}")

# Uso de la funci�n
source_directory = '/media/pi/Maxell8/Dataset/Dataset/images/train/platano'
target_directory = '/media/pi/Maxell8/DataAugmentation/platano'
number_of_images = 32  # Cambia esto al n�mero de im�genes que quieras copiar

copy_images(source_directory, target_directory, number_of_images)
