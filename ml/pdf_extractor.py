import pymupdf


def extract_text_from_pdf(pdf_path):
    text_parts = []

    with pymupdf.open(pdf_path) as doc:
        for page in doc:
            text_parts.append(page.get_text())

    return "\n".join(text_parts)
