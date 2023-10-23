import PyPDF2
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import pkcs12
from OpenSSL import crypto
def sign_pdf(input_pdf_path, output_pdf_path, signature_text):
    pdf_writer = PyPDF2.PdfWriter()

    # Load the existing PDF
    with open(input_pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        print(pdf_reader)

        # Create a new page with the signature
        page = pdf_reader.pages[0]
        #print(page)
        #page.mergePage(PyPDF2.PdfReader("pdf_signature").pages[0])
        pdf_writer.add_page(page)
        #
        # # Write the signed PDF to the output file
        with open(output_pdf_path, 'wb') as output_pdf:
             pdf_writer.write(output_pdf)

def load_pkcs12_certificates(pfx_file_path, password):
    with open(pfx_file_path, 'rb') as pfx_file:
        pfx = crypto.load_pkcs12(pfx_file.read(), password)
    certificates = [crypto.dump_certificate(crypto.FILETYPE_PEM, pfx.get_certificate())]
    pkey = crypto.dump_privatekey(crypto.FILETYPE_PEM, pfx.get_privatekey())
    return certificates, pkey


def sign_message_with_ca_key(message, ca_private_key_path):
    # Load the CA's private key from a PEM file
    with open(ca_private_key_path, 'rb') as key_file:
        ca_private_key = serialization.load_pem_private_key(
            key_file.read(),
            password='Bangy135#'  # Replace with your password if the key is encrypted
        )

    # Sign the message using the CA's private key
    signature = ca_private_key.sign(
        message.encode('utf-8'),  # Convert message to bytes
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    return signature



if __name__ == "__main__":
    input_pdf_path = "Letter.pdf"  # Replace with the actual input PDF file path
    output_pdf_path = "Letterout.pdf"  # Replace with the desired output path
    signature_text = "Your Digital Signature"
    pfx_file = "chatchai.j.p12"  # Replace with the path to your PFX certificate file
    pfx_password = "Bangy135#"  # Replace with the password for your PFX certificate


    certificates, private_key=load_pkcs12_certificates(pfx_file, pfx_password)
    print(certificates)
    print(private_key)




    #sign_pdf(input_pdf_path, output_pdf_path, certificates)
