from PIL import Image, ImageDraw, ImageFont
import os

BASE_DIR = os.path.dirname(__file__)
FONT_PATH = os.path.join(BASE_DIR, "fonts", "Courier_New.ttf")

def generate_prescription_image(data, output_path):
    img = Image.new("RGB", (800, 1000), "white")
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(FONT_PATH, 22)
    bold = ImageFont.truetype(FONT_PATH, 26)

    y = 40
    draw.text((250, y), "PRESCRIPTION", font=bold, fill="black")
    y += 50

    draw.text((40, y), f"Patient: {data['patient']}", font=font, fill="black")
    y += 30
    draw.text((40, y), f"Date: {data['date']}", font=font, fill="black")
    y += 40

    draw.text((40, y), "Medicines:", font=bold, fill="black")
    y += 30

    for med in data["medicines"]:
        draw.text((60, y), f"- {med}", font=font, fill="black")
        y += 28

    y += 40
    draw.text((40, y), f"Doctor: {data['doctor']}", font=font, fill="black")

    y += 60
    draw.text((40, y), "System Generated Prescription", font=font, fill="gray")

    img.save(output_path)
