import fitz  # PyMuPDF

def extract_outline_from_pdf(pdf_path):
    """
    Extract outline from PDF by picking headings based on font size and also include all bold text as headings.
    - Headings by font size:
        * H1: size >= 16
        * H2: size >= 13
    - Additionally, include any bold text as heading (H2 if not already included).
    """
    doc = fitz.open(pdf_path)
    outline = []

    for page_number, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                line_text = ""
                max_size = 0
                is_bold = False
                for span in line["spans"]:
                    line_text += span["text"].strip()
                    max_size = max(max_size, span["size"])
                    if span["flags"] & 2:  # bold flag
                        is_bold = True
                line_text = line_text.strip()

                if not line_text:
                    continue

                # Determine heading level by font size
                if max_size >= 16:
                    level = "H1"
                elif max_size >= 13:
                    level = "H2"
                else:
                    level = None

                # If not heading by size but bold, treat as H2
                if level is None and is_bold:
                    level = "H2"

                if level:
                    outline.append({
                        "level": level,
                        "text": line_text,
                        "page": page_number
                    })

    doc.close()
    return outline