import pandas as pd
import barcode
from barcode.writer import ImageWriter
import os

# Ruta del archivo de Excel
excel_file_path = r"C:\Users\santi\Desktop\Inventario PujVex.xlsx"

# Cargar el archivo de Excel
excel_data = pd.ExcelFile(excel_file_path)

# Cargar la hoja específica que contiene los datos del inventario
inventory_data = excel_data.parse('Inventario')

# Definir la ruta para guardar las imágenes y el archivo de texto
save_path = r"Inventario\Barras"
txt_output_path = r"Inventario\codigos.txt"

# Asegurarse de que la carpeta de destino existe
os.makedirs(save_path, exist_ok=True)

# Filtrar los códigos de la columna B (Codigos Pieza)
codigos = inventory_data['Codigo Pieza'].dropna()

# Crear un archivo de texto para guardar los nombres de los documentos
with open(txt_output_path, 'w') as txt_file:
    # Crear y guardar una imagen por cada código de barras
    for codigo in codigos:
        if codigo.strip():  # Ignorar celdas en blanco o que solo contienen espacios
            # Eliminar caracteres no alfanuméricos del código antes de generarlo
            codigo_limpio = ''.join(filter(str.isalnum, codigo))
            
            # Crear el código de barras usando python-barcode
            codigo_barra = barcode.get('code39', codigo_limpio, writer=ImageWriter())
            
            # Guardar la imagen con el nombre del código
            filename = os.path.join(save_path, codigo_limpio)
            codigo_barra.save(filename)
            
            # Escribir el código limpio en el archivo de texto en el formato deseado
            txt_file.write(f'"{codigo_limpio}",\n')

# Mostrar los primeros códigos como referencia
print(codigos.head())
