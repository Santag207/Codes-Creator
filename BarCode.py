import pandas as pd
import barcode
from barcode.writer import ImageWriter
import os

# Ruta del archivo de Excel
excel_file_path = r"C:\Users\santi\OneDrive\Documentos\GitHub\Qr-and-BarCode-creator\Inventario\Inventario PujVex.xlsx"

# Cargar el archivo de Excel
excel_data = pd.ExcelFile(excel_file_path)

# Cargar la hoja específica que contiene los datos del inventario
inventory_data = excel_data.parse('Inventario')

# Definir la ruta para guardar las imágenes
save_path = r"C:\Users\santi\OneDrive\Documentos\GitHub\Qr-and-BarCode-creator\Inventario\Barras"

# Asegurarse de que la carpeta de destino existe
os.makedirs(save_path, exist_ok=True)

# Filtrar los códigos de la columna B (Codigos Pieza)
codigos = inventory_data['Codigo Pieza'].dropna()

# Crear y guardar una imagen por cada código de barras
for codigo in codigos:
    if codigo.strip():  # Ignorar celdas en blanco o que solo contienen espacios
        # Crear el código de barras usando python-barcode
        codigo_barra = barcode.get('code39', codigo, writer=ImageWriter())
        
        # Guardar la imagen con el nombre del código
        filename = os.path.join(save_path, codigo)
        codigo_barra.save(filename)

# Mostrar los primeros códigos como referencia
print(codigos.head())
