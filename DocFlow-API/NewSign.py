import fitz
import PyPDF2

def sign_pdf_with_fake_signature(input_pdf_path, output_pdf_path):
    # Open the input PDF
    with open(input_pdf_path, 'rb') as input_pdf_file:
        pdf_reader = PyPDF2.PdfReader(input_pdf_file)
        pdf_writer = PyPDF2.PdfWriter()

        # Copy all pages and apply a fake digital signature (not a real signature)
        Lpage=len(pdf_reader.pages)
        for page_num in range(Lpage):
            page = pdf_reader.pages[page_num]
            # Apply some modification to simulate a signature
            page.merge_page(PyPDF2.PdfReader('Signature.pdf').pages[0])
            pdf_writer.add_page(page)

        # Save the signed PDF
        with open(output_pdf_path, 'wb') as output_pdf_file:
            pdf_writer.write(output_pdf_file)

def sign_pdf_with_ca(input_pdf_path, output_pdf_path, ca_private_key_path, ca_certificate_path, signature_field_name):
    # Load the PDF
    pdf_document = fitz.open(input_pdf_path)

    # Get the page to sign (page number 0 in this example)
    page = pdf_document.load_page(0)

    # Load the CA's private key and certificate
    with open(ca_private_key_path, 'rb') as key_file:
        private_key_pem = key_file.read()

    with open(ca_certificate_path, 'rb') as cert_file:
        certificate_pem = cert_file.read()

    # Create a digital signature
    signature = page.insert_pdf_sign(signature_field_name, contents=[], keyfile=private_key_pem, certfile=certificate_pem)

    # Save the signed PDF
    pdf_document.save(output_pdf_path)
    pdf_document.close()
def apply_ca_signature(input_pdf_path, output_pdf_path, signature_image_path, signature_location):
    # Load the PDF
    pdf_document = fitz.open(input_pdf_path)

    # Load the signature image
    signature_image = fitz.open(signature_image_path)

    # Get the page to sign (page number 0 in this example)
    page = pdf_document[0]

    # Create a signature annotation
    rect = fitz.Rect(signature_location[0], signature_location[1],
                     signature_location[0] + signature_image[0].rect.width,
                     signature_location[1] + signature_image[0].rect.height)

    print(rect)

    annot=page.add_rect_annot(rect)

    #annot = page.add_annotation(fitz.PdfAnnot.DRAW_IMAGE, rect)
    #
    # # Set the image as the annotation's appearance
    #annot.set_appearance(signature_image)
    #
    # # Save the signed PDF
    pdf_document.save(output_pdf_path)
    pdf_document.close()

if __name__ == "__main__":
    input_pdf_path = "Letter.pdf"  # Replace with the actual input PDF file path
    output_pdf_path = "Out1.pdf"  # Replace with the desired output PDF file path
    ca_private_key_path = "chatchai.j.key.pem"  # Replace with the actual CA private key path
    ca_certificate_path = "chatchai.j.cert.pem"  # Replace with the actual CA certificate path
    signature_field_name = "SignatureField"  # Replace with the desired signature field name
    signature_image_path='Signature.pdf'
    signature_location = (100, 100)

    #apply_ca_signature(input_pdf_path, output_pdf_path, signature_image_path, signature_location)

    sign_pdf_with_fake_signature(input_pdf_path, output_pdf_path)
    #sign_pdf_with_ca(input_pdf_path, output_pdf_path, ca_private_key_path, ca_certificate_path, signature_field_name)
