import PyPDF2

def sign_pdf_with_fake_signature(input_pdf_path, output_pdf_path):
    # Open the input PDF
    with open(input_pdf_path, 'rb') as input_pdf_file:
        pdf_reader = PyPDF2.PdfReader(input_pdf_file)
        pdf_writer = PyPDF2.PdfWriter()

        # Copy all pages and apply a fake digital signature (not a real signature)
        L= len(pdf_reader.pages)
        for page_num in range(L):
            page = pdf_reader.pages[page_num]
            # Apply some modification to simulate a signature
            page.merge_page(PyPDF2.PdfReader('Signature.pdf').pages[0])
            pdf_writer.add_page(page)

        # Save the signed PDF
        with open(output_pdf_path, 'wb') as output_pdf_file:
            pdf_writer.write(output_pdf_file)

if __name__ == "__main__":
    input_pdf_path = "letter.pdf"  # Replace with the actual input PDF file path
    output_pdf_path = "fake_output.pdf"  # Replace with the desired output PDF file path

    sign_pdf_with_fake_signature(input_pdf_path, output_pdf_path)
