from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
import os, json

from invoice_image import generate_invoice_image
from prescription_image import generate_prescription_image

app = FastAPI(title="Document Generator API")

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"status": "API running successfully"}

@app.post("/generate-invoice")
def generate_invoice(
    invoice_no: str = Form(...),
    date: str = Form(...),
    customer: str = Form(...),
    items: str = Form(...)
):
    data = {
        "invoice_no": invoice_no,
        "date": date,
        "customer": customer,
        "items": json.loads(items)
    }
    file_path = f"{OUTPUT_DIR}/invoice_{invoice_no}.png"
    generate_invoice_image(data, file_path)
    return FileResponse(file_path, media_type="image/png")

@app.post("/generate-prescription")
def generate_prescription(
    patient: str = Form(...),
    date: str = Form(...),
    doctor: str = Form(...),
    medicines: str = Form(...)
):
    data = {
        "patient": patient,
        "date": date,
        "doctor": doctor,
        "medicines": medicines.split(",")
    }
    file_path = f"{OUTPUT_DIR}/prescription_{patient}.png"
    generate_prescription_image(data, file_path)
    return FileResponse(file_path, media_type="image/png")
