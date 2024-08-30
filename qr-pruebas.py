import qrcode
from PIL import Image
import os

# Directorios
qr_output_dir = r"C:\Users\santi\OneDrive\Documentos\GitHub\Qr-and-BarCode-creator\Inventario\QRs"
logo_dir = r"C:\Users\santi\OneDrive\Documentos\GitHub\Qr-and-BarCode-creator\Inventario\Barras"


# Asegúrate de que el directorio de salida exista
os.makedirs(qr_output_dir, exist_ok=True)

# Función para generar un QR con imagen en el centro
def generate_qr_with_logo(link, document_name):
    # Ruta completa del logo y del QR
    logo_path = os.path.join(logo_dir, f"{document_name}.png")
    save_path = os.path.join(qr_output_dir, f"{document_name}.png")
    
    # Verifica si el logo existe
    if not os.path.exists(logo_path):
        print(f"Logo no encontrado: {logo_path}")
        return
    
    # Crear la instancia de QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Mayor corrección de errores
        box_size=10,
        border=4,
    )
    
    # Agregar el enlace
    qr.add_data(link)
    qr.make(fit=True)

    # Generar la imagen del QR
    img = qr.make_image(fill='black', back_color='white').convert('RGB')

    # Cargar la imagen del logo y convertirla a RGBA
    logo = Image.open(logo_path).convert("RGBA")

    # Calcular el tamaño del logo (20% del tamaño del QR)
    logo_size = int(min(img.size) * 0.4)
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    # Calcular la posición del logo en el centro del QR
    pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)

    # Crear una máscara para el logo
    logo_mask = logo.split()[3]  # Usar el canal alfa como máscara

    # Pegar el logo sobre el QR usando la máscara
    img.paste(logo, pos, mask=logo_mask)

    # Guardar la imagen
    img.save(save_path)
    print(f"QR guardado en: {save_path}")

# Ejemplo de uso
document_names = ["10TS"]  # Lista de nombres de documentos

for doc_name in document_names:
    link = f"https://livejaverianaedu-my.sharepoint.com/:b:/g/personal/castrozsantiago_javeriana_edu_co/EaJ2Y9WM9i1Fhznz1xHS3IkBQopHJPDUoWEdEICtKUNdrg?e=n87TaE"  # Cambia a tus enlaces
    generate_qr_with_logo(link, doc_name)

