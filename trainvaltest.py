import os
import shutil
import random

def partition_images(source_dir, train_dir, val_dir, test_dir, train_frac, val_frac, test_frac):
    """
    Particiona las imágenes en tres grupos (train, validation, test) y las copia a los directorios correspondientes.

    Args:
    source_dir (str): El directorio fuente de donde se copiarán las imágenes.
    train_dir (str): El directorio destino para el conjunto de entrenamiento.
    val_dir (str): El directorio destino para el conjunto de validación.
    test_dir (str): El directorio destino para el conjunto de prueba.
    train_frac (float): Fracción de imágenes para el entrenamiento.
    val_frac (float): Fracción de imágenes para la validación.
    """

    # Verificar existencia del directorio fuente
    if not os.path.exists(source_dir):
        print(f"El directorio fuente {source_dir} no existe.")
        return

    # Crear directorios destino si no existen
    for directory in [train_dir, val_dir, test_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory)

    # Obtener todos los archivos de imagen en el directorio fuente
    files = [os.path.join(source_dir, file) for file in os.listdir(source_dir) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    random.shuffle(files)

    # Calcular los índices de corte para cada subconjunto
    total_images = len(files)
    train_end = int(total_images * train_frac)
    val_end = train_end + int(total_images * val_frac)

    # Dividir archivos
    train_files = files[:train_end]
    val_files = files[train_end:val_end]
    test_files = files[val_end:]

    # Copiar archivos a sus respectivos directorios
    for file, dest in zip(train_files, [train_dir]*len(train_files)):
        shutil.copy(file, dest)
    for file, dest in zip(val_files, [val_dir]*len(val_files)):
        shutil.copy(file, dest)
    for file, dest in zip(test_files, [test_dir]*len(test_files)):
        shutil.copy(file, dest)

# Configuración de directorios y proporciones
source_directory = r'C:\Users\Giancarlos\Documents\Dataset\Dataset\data\image\platano'
train_directory = r'C:\Users\Giancarlos\Documents\Dataset\Dataset\images\train\platano'
val_directory = r'C:\Users\Giancarlos\Documents\Dataset\Dataset\images\val\platano'
test_directory = r'C:\Users\Giancarlos\Documents\Dataset\Dataset\images\test\platano'

# Llamar a la función con las proporciones deseadas
partition_images(source_directory, train_directory, val_directory, test_directory, train_frac=0.60, val_frac=0.20, test_frac=0.20)
