from pdf2docx import Converter

# Function to convert PDF to Word
def convert_pdf_to_word(file_path):
    output_path = file_path.replace(".pdf", ".docx")
    converter = Converter(file_path)
    converter.convert(output_path, start=0, end=None)
    converter.close()
    print(f"Converted {file_path} to {output_path}")