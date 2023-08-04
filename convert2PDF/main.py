from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path, output_file):
    text = extract_text(pdf_path)
    with open(output_file, "w", encoding="utf-8") as output:
        output.write(text)


# Example usage:
pdf_path = "/Users/anjalafghan/Documents/python/convert2PDF/creditcard.PDF"  # Replace this with the actual path to your PDF file
output_file = "output_text.txt"
extracted_text = extract_text_from_pdf(pdf_path, output_file)
