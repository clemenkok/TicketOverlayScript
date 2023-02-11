from PIL import Image, ImageFont, ImageDraw

for i in range(1, 451):
    # Overlay text generation
    img = Image.open("ME23 Ticket.png")
    font = ImageFont.truetype("arial.ttf", 24)
    draw = ImageDraw.Draw(img)
    text = str(i)
    draw.text((1850, 50), text, (255, 255, 255), font=font)
    img.save(f'{text}.png')

    # PDF Conversion 
    text = str(i)
    PNG_FILE = f'{text}.png'
    PDF_FILE = f'ME_Ticket_{text}.pdf'
    rgba = Image.open(PNG_FILE)
    rgb = Image.new('RGB', rgba.size, (255, 255, 255))
    rgb.paste(rgba, mask=rgba.split()[3])
    rgb.save(PDF_FILE, 'PDF', resoultion=100.0)
