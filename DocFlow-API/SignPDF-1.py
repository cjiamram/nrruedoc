from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign import signers
import PyPDF2
from io import BytesIO


signer = signers.SimpleSigner.load_pkcs12(
    pfx_file='chatchai.j.p12', passphrase=b'Bangy135#'
)

print(signer)

with open('letter.pdf', 'rb') as doc:
    w = IncrementalPdfFileWriter(doc)
    out = signers.sign_pdf(
        w, signers.PdfSignatureMetadata(field_name='Signature1'),
        signer=signer,
    )


signed_pdf_bytes = out.getvalue()
#print(signed_pdf_bytes)

# Specify the output PDF file path
output_pdf_path = 'signed_document.pdf'

# Save the PDF content to a file
with open(output_pdf_path, 'wb') as output_pdf_file:
    output_pdf_file.write(signed_pdf_bytes)

#print('PDF signed and saved to:', output_pdf_path)

# output_pdf_path = 'signed_document.pdf'
# with open(output_pdf_path, 'wb') as output_pdf_file:
# signed_pdf.write(output_pdf_file)

#print(out)

    # do stuff with 'out'
