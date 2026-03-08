import fitz

pdf_path = "Krystal Aligners_Logo_(5.5x5.5cm).pdf"
png_path = "logo.png"

try:
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
    pix = page.get_pixmap(dpi=300)
    pix.save(png_path)
    print("Logo extracted to logo.png")
except Exception as e:
    print("Error:", e)
