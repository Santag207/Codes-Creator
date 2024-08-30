import qrcode

# Crea una instancia de QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Agrega el enlace
qr.add_data('https://livejaverianaedu-my.sharepoint.com/:b:/g/personal/castrozsantiago_javeriana_edu_co/ETjmQrJ2mfZCmxtC6pdTxUcBYc6zx8oJm0S-G_vv9fOjZg?e=ZHXQ39')
qr.make(fit=True)

# Genera la imagen del QR
img = qr.make_image(fill='black', back_color='white')

# Guarda la imagen
img.save('C:\\Users\\santi\\Documents\\Inventario\\qr.png')
