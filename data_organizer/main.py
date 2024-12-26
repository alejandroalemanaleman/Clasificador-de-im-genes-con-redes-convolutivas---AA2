import os
import random

def eliminar_archivos_aleatorios(carpeta, num_archivos):
    try:
        # Obtener la lista de archivos en la carpeta
        archivos = [f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))]
        
        # Verificar si hay suficientes archivos para eliminar
        if num_archivos > len(archivos):
            print(f"No hay suficientes archivos en la carpeta. Solo hay {len(archivos)} archivo(s).")
            return
        
        # Seleccionar archivos aleatorios
        archivos_a_eliminar = random.sample(archivos, num_archivos)
        
        # Eliminar los archivos seleccionados
        for archivo in archivos_a_eliminar:
            ruta_archivo = os.path.join(carpeta, archivo)
            os.remove(ruta_archivo)
            print(f"Archivo eliminado: {ruta_archivo}")
        
        print("Eliminación completada.")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Especifica la carpeta y el número de archivos a eliminar
#carpeta = "/Users/alejandroalemanaleman/Downloads/AA2_trabajo1/data/helicopter"  # Cambia esto por la ruta a tu carpeta

num_archivos = 850  # Cambia esto por el número de archivos a eliminar

eliminar_archivos_aleatorios(carpeta, num_archivos)
