from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign import signers


signer = signers.SimpleSigner.load_pkcs12(
    pfx_file='chatchai.j.12', passphrase=b'Bangy135#'
)

with open('Letter.pdf', 'rb') as doc:
    w = IncrementalPdfFileWriter(doc)
    out = signers.sign_pdf(
        w, signers.PdfSignatureMetadata(field_name='Signature1'),
        signer=signer,
    )

    # do stuff with 'out'...
