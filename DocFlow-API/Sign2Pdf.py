import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

def add_signature_to_pdf(input_pdf_path, output_pdf_path, signature_image_path):
    # Load the PDF
    pdf_reader = PyPDF2.PdfReader(input_pdf_path)
    pdf_writer = PyPDF2.PdfWriter()

    # Read each page and add the image to it
    L=len(pdf_reader.pages)
    for page_num in range(L):
        page = pdf_reader.pages[page_num]
        page.merge_page(page)

        # Load the image and position it on the page
        img = Image.open(signature_image_path)
        img_width, img_height = img.size
        page.mediabox.lower_left = (100, 100)
        page.mediabox.upper_right = (100 + img_width, 100 + img_height)

        # Add the image to the page
        #page._data['/XObject'] = pdf_writer._add_object(page, pdf_writer._add_object(img))

        # Add the modified page to the PDF writer
    pdf_writer.add_page(page)

    # Write the modified PDF to the output file
    with open(output_pdf_path, 'wb') as output_pdf_file:
        pdf_writer.write(output_pdf_file)

# Paths to the input PDF, output PDF, and signature image
input_pdf_path = 'Letter.pdf'
output_pdf_path = 'output.pdf'
signature_image_path = 'signature.jpg'

# Add the signature image to the PDF
add_signature_to_pdf(input_pdf_path, output_pdf_path, signature_image_path)
