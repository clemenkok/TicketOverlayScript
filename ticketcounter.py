from PIL import Image, ImageFont, ImageDraw

for i in range(1, 451):
    # Overlay text generation
    img = Image.open("ME23 Ticket.png")
    font = ImageFont.truetype("arial.ttf", 24)
    draw = ImageDraw.Draw(img)
    text = str(i)
    draw.text((1850, 50), text, (255, 255, 255), font=font)
    img.save(f'{text}.png')
    
    # Overlay QR Code
    text = str(i)
    numbered_image = f'{text}.png'
    no_qr_code = Image.open(numbered_image)
    qr = qrcode.QRCode(
    version=12,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=3,
    border=12
    )
    qr.add_data(f'ME ticket number {text}')
    qr.make()
    qrcode_img = qr.make_image(fill_color="white", back_color="#000000")
    no_qr_code.paste(qrcode_img)
    no_qr_code.save(f'{text}_qr.png')
    
    # PDF Conversion 
    text = str(i)
    PNG_FILE = f'{text}.png'
    PDF_FILE = f'ME_Ticket_{text}.pdf'
    rgba = Image.open(PNG_FILE)
    rgb = Image.new('RGB', rgba.size, (255, 255, 255))
    rgb.paste(rgba, mask=rgba.split()[3])
    rgb.save(PDF_FILE, 'PDF', resoultion=100.0)
