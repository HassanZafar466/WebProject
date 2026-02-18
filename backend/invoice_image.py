from PIL import Image, ImageDraw, ImageFont
import os

BASE_DIR = os.path.dirname(__file__)
FONT_PATH = os.path.join(BASE_DIR, "fonts", "Courier_New.ttf")

def generate_invoice_image(data, output_path):
    img = Image.new("RGB", (800, 1200), "white")
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(FONT_PATH, 22)
    bold = ImageFont.truetype(FONT_PATH, 26)

    y = 40
    draw.text((280, y), "INVOICE", font=bold, fill="black")
    y += 50

    draw.text((40, y), f"Invoice No: {data['invoice_no']}", font=font, fill="black")
    y += 30
    draw.text((40, y), f"Date: {data['date']}", font=font, fill="black")
    y += 30
    draw.text((40, y), f"Customer: {data['customer']}", font=font, fill="black")
    y += 40

    draw.text((40, y), "Item", font=bold, fill="black")
    draw.text((420, y), "Qty", font=bold, fill="black")
    draw.text((520, y), "Price", font=bold, fill="black")
    draw.text((640, y), "Total", font=bold, fill="black")
    y += 30

    total = 0
    for item in data["items"]:
        line_total = item["qty"] * item["price"]
        draw.text((40, y), item["name"], font=font, fill="black")
        draw.text((420, y), str(item["qty"]), font=font, fill="black")
        draw.text((520, y), f"{item['price']:.2f}", font=font, fill="black")
        draw.text((640, y), f"{line_total:.2f}", font=font, fill="black")
        total += line_total
        y += 28

    y += 30
    draw.line((40, y, 760, y), fill="black", width=2)
    y += 20

    draw.text((520, y), "Net Total:", font=bold, fill="black")
    draw.text((640, y), f"{total:.2f}", font=bold, fill="black")

    y += 60
    draw.text((40, y), "System Generated Document", font=font, fill="gray")

    img.save(output_path)
