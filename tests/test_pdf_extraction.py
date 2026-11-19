from ml.pdf_extractor import extract_text_from_pdf
from ml.text_preprocessor import clean_text

pdf_path = "Main_Resume.pdf"

# Extract text from PDF
raw_text = extract_text_from_pdf(pdf_path)

# Clean extracted text
cleaned_text = clean_text(raw_text)

print("----- RAW TEXT -----")
print(raw_text)

print("\n----- CLEANED TEXT -----")
print(cleaned_text)
