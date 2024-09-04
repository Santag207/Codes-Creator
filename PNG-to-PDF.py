import os
from fpdf import FPDF
from PIL import Image

# Definir la carpeta donde están las imágenes
image_folder = r'C:\Users\santi\OneDrive\Escritorio\PNG'

# Crear una carpeta para los PDFs si no existe
pdf_folder = os.path.join(image_folder, 'PDFs')
if not os.path.exists(pdf_folder):
    os.makedirs(pdf_folder)

# Obtener la lista de todas las imágenes en la carpeta
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Iterar sobre las imágenes y convertirlas a PDF
for image_file in image_files:
    # Construir la ruta completa del archivo de imagen
    image_path = os.path.join(image_folder, image_file)
    
    if os.path.exists(image_path):
        # Cargar la imagen
        image = Image.open(image_path)
        
        # Crear el PDF
        pdf = FPDF()
        pdf.add_page()

        # Redimensionar imagen si es necesario para ajustarla
        pdf.image(image_path, x=10, y=10, w=190)  # Ajuste estándar de tamaño

        # Guardar el archivo PDF en la carpeta 'PDFs' con el mismo nombre que la imagen
        pdf_output_path = os.path.join(pdf_folder, f'{os.path.splitext(image_file)[0]}.pdf')
        pdf.output(pdf_output_path)
        
        print(f'Archivo {os.path.splitext(image_file)[0]}.pdf generado correctamente en {pdf_folder}.')
    else:
        print(f'La imagen {image_path} no existe.')
