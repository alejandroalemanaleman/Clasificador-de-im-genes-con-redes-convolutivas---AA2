import os
import shutil
from sklearn.model_selection import train_test_split

def organizar_datos(origen, destino, proporciones=(0.7, 0.15, 0.15)):
    """
    Organiza los datos en carpetas de train, test y validation respetando las proporciones dadas.
    
    :param origen: Ruta de la carpeta con las clases de vehículos.
    :param destino: Ruta de la carpeta donde se crearán las carpetas train, test y validation.
    :param proporciones: Proporciones para train, test y validation (por defecto: 70%, 15%, 15%).
    """
    try:
        # Verificar proporciones
        if sum(proporciones) != 1.0:
            raise ValueError("Las proporciones deben sumar 1.0 (e.g., 0.7, 0.15, 0.15)")

        # Crear carpetas de destino si no existen
        for carpeta in ['train', 'test', 'validation']:
            ruta = os.path.join(destino, carpeta)
            os.makedirs(ruta, exist_ok=True)
        
        # Iterar sobre las clases de vehículos en la carpeta origen
        clases = [d for d in os.listdir(origen) if os.path.isdir(os.path.join(origen, d))]
        
        for clase in clases:
            ruta_clase_origen = os.path.join(origen, clase)
            archivos = os.listdir(ruta_clase_origen)

            # Dividir los archivos en train, test y validation
            train_files, test_valid_files = train_test_split(archivos, test_size=1 - proporciones[0], random_state=42)
            test_files, valid_files = train_test_split(test_valid_files, test_size=proporciones[2] / (proporciones[1] + proporciones[2]), random_state=42)

            # Mover los archivos a las carpetas correspondientes
            for conjunto, archivos_conjunto in zip(['train', 'test', 'validation'], [train_files, test_files, valid_files]):
                ruta_destino = os.path.join(destino, conjunto, clase)
                os.makedirs(ruta_destino, exist_ok=True)
                
                for archivo in archivos_conjunto:
                    shutil.move(os.path.join(ruta_clase_origen, archivo), os.path.join(ruta_destino, archivo))

            print(f"Clase '{clase}' organizada en train, test y validation.")

        print("Organización completada.")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Configura las rutas de origen y destino
origen = "/Users/alejandroalemanaleman/Downloads/AA2_trabajo1/data"
destino = "/Users/alejandroalemanaleman/Downloads/AA2_trabajo1/clean"

organizar_datos(origen, destino)
