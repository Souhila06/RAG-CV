from pdf2image import convert_from_path
import os
from pathlib import Path
import PyPDF2

FOLDER = "./data/images"
UPLOAD_DIR = "./data/files"


def convert_pdf(path, name):
    os.makedirs(FOLDER, exist_ok=True)

    try:
        images = convert_from_path(os.path.join(path, name))

        for i, image in enumerate(images):
            output_path = os.path.join(FOLDER, f"{name[:-4]}.jpg")
            image.save(output_path, "JPEG")
            print(f"Saved: {output_path}")

        print(f"Conversion completed. {len(images)} pages saved to {FOLDER}.")

    except Exception as e:
        print(f"An error occurred: {e}")


def get_text_from_pdfs():
    pdf_paths = [
        p
        for p in Path(UPLOAD_DIR).iterdir()
        if p.is_file() and p.suffix.lower() == ".pdf"
    ]

    full_text = []

    for pdf_path in pdf_paths:
        try:
            with open(pdf_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)

                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"

                full_text.append(text)

        except Exception as e:
            print(f"Error processing {pdf_path}: {str(e)}")

    return full_text
