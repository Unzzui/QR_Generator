import qrcode

def generar_codigo_qr(enlace):
    # Crea un objeto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    # Agrega los datos (enlace) al código QR
    qr.add_data(enlace)
    
    # Compila el código QR
    qr.make(fit=True)
    
    # Crea una imagen del código QR
    imagen_qr = qr.make_image(fill_color="black", back_color="white")
    
    # Guarda la imagen del código QR en un archivo
    imagen_qr.save("codigo_qr.png")

# Agregar el link correspondiente
link = "https://et-analisis-economico-72b708efbc49.herokuapp.com/"
generar_codigo_qr(link)
