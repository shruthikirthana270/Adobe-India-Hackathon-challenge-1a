import fitz
from pathlib import Path

def debug_font_sizes(pdf_path, max_pages=3):
    doc = fitz.open(pdf_path)
    for page_num in range(min(len(doc), max_pages)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]
        print(f"Page {page_num+1}:")
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    size = span["size"]
                    if text:
                        print(f"  Font size: {size}, Text: {text}")
    doc.close()

if __name__ == "__main__":
    pdf_file = Path(r"C:\Users\Dell\Downloads\adobe-pdf-processor\Challenge_1a\sample_dataset\input\file03.pdf")
    debug_font_sizes(pdf_file)