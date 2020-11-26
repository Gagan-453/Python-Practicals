from fpdf import FPDF
from pyPDF2 import PDFFileWriter, PDFFileReader

def secure_pdf(file, password):
    parser = PDFFileWriter()
    pdf = PDFFileReader(file)

    for page in range(pdf.numpages):
        parser.add_page(pdf.getpage(page))

    parser.encrypt(password)

    with open(f"encrypted_{file}", "wb") as f:
        parser.write(f)
        f.close()
    print(f"encrypted_{file} created. . .")

if __name__ == "__main__":
    file = "teacher.pdf"
    password = "gagan_genius"
    secure_pdf(file, password)
