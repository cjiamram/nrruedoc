import PyPDF2
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import pkcs12
from OpenSSL import crypto


def sign_pdf(input_pdf_path, output_pdf_path, pfx_file, pfx_password):
    # Load the PDF file to be signed
    with open(input_pdf_path, 'rb') as input_pdf:
        pdf_reader = PyPDF2.PdfReader(input_pdf)
        pdf_writer = PyPDF2.PdfWriter()

        # Load the PFX file for digital signature
        with open(pfx_file, 'rb') as pfx_file:
            pfx_bytes = pfx_file.read()

        # pfx_certificate = serialization.load_pem_private_key(
        #     pfx_bytes,
        #     password=pfx_password.encode(),
        #     backend=default_backend()
        # )

        pfx_certificate = serialization.load_pem_private_key(
                pfx_bytes,
                password=pfx_password.encode(),
                backend=default_backend()
        )


        for page_number in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_number)
            pdf_writer.addPage(page)

        # Apply the digital signature to the PDF
        pdf_writer.addBlankPage(width=0, height=0)
        pdf_writer.updatePageFormFieldValues(pdf_writer.getPage(pdf_reader.getNumPages()), '/P', '/V')

        pdf_writer.sign(
            page_number,
            pfx_certificate,
            b'',
            pdf_reader.getPage(page_number).mediaBox,
            pdf_writer
        )

        # Save the signed PDF
        with open(output_pdf_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)


def readPDF(pdf):
     with open(pdf, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Print the number of pages in the PDF
        print('Number of pages:', len(pdf_reader.pages))

        # Iterate through each page and extract text
        #for page_number in len(pdf_reader.pages):
        page = pdf_reader.pages[0]
        #print('Text from page', page_number + 1)
        print(page.extract_text())

def load_pkcs12_certificates(pfx_file_path, password):
    with open(pfx_file_path, 'rb') as pfx_file:
        pfx = crypto.load_pkcs12(pfx_file.read(), password)

    certificates = [crypto.dump_certificate(crypto.FILETYPE_PEM, pfx.get_certificate())]

    pkey = crypto.dump_privatekey(crypto.FILETYPE_PEM, pfx.get_privatekey())

    return certificates, pkey

def merge_certificate_to_pdf(input_pdf_path, certificate_pem, output_pdf_path):
    # Create a PDF merger object
    pdf_merger = PyPDF2.PdfMerger()

    # Add the original PDF
    pdf_merger.append(input_pdf_path)

    # Add the certificate as a new page
    pdf_merger.merge(width=0, height=0)
    pdf_merger.updatePageFormFieldValues(pdf_merger.getPage(pdf_merger.getNumPages()), '/P', '/V')

    # Write the merged PDF to the output file
    with open(output_pdf_path, 'wb') as output_pdf:
        pdf_merger.write(output_pdf)

def readPFX(pfx):
    pfx_file_path = pfx
    pfx_password = 'Bangy135#'

    with open(pfx_file_path, 'rb') as pfx_file:
        pfx_bytes = pfx_file.read()

    print(pfx_password.encode())

    #pfx_certificate, pfx_private_key, _ = pkcs12.load_pkcs12_certificates(pfx_bytes, pfx_password.encode())

    # Serialize the private key and certificate to PEM format (optional)
    #pfx_certificate_pem = pfx_certificate.public_bytes(serialization.Encoding.PEM)
    # pfx_private_key_pem = pfx_private_key.private_bytes(
    #     encoding=serialization.Encoding.PEM,
    #     format=serialization.PrivateFormat.TraditionalOpenSSL,
    #     encryption_algorithm=serialization.NoEncryption()
    # )

    # pfx_certificate = serialization.load_pem_private_key(
    #             pfx_bytes,
    #             password=pfx_password.encode(),
    #             backend=default_backend()
    # )





if __name__ == "__main__":
    input_pdf_path = "Letter.pdf"  # Replace with the actual input PDF file path
    output_pdf_path = "Letter Signed.pdf"  # Replace with the desired output path
    pfx_file = "chatchai.j.p12"  # Replace with the path to your PFX certificate file
    pfx_password = "Bangy135#"  # Replace with the password for your PFX certificate

    #readPFX(pfx_file)
    # It 's work.############################
    certificates, private_key=load_pkcs12_certificates(pfx_file, pfx_password)
    print(certificates)
    print(private_key)
    ###################################

    #sign_pdf_with_ca(input_pdf_path, output_pdf_path, private_key)

    #merge_certificate_to_pdf(input_pdf_path, certificates, output_pdf_path)

    #readPDF(input_pdf_path)

    #sign_pdf(input_pdf_path, output_pdf_path, pfx_file, pfx_password)
