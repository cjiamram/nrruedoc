from pyhanko import stamp
from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign import fields, signers


signer = signers.SimpleSigner.load_pkcs12(
    pfx_file='chatchai.j.p12', passphrase=b'Bangy135#'
)
with open('letter.pdf', 'rb') as inf:
    w = IncrementalPdfFileWriter(inf)
    fields.append_signature_field(
        w, sig_field_spec=fields.SigFieldSpec(
            'Signature', box=(200, 50, 400, 180)
        )
    )

    meta = signers.PdfSignatureMetadata(field_name='Signature')
    pdf_signer = signers.PdfSigner(
        meta, signer=signer,
        stamp_style=stamp.StaticStampStyle.from_pdf_file('Stamp.pdf')
    )
    with open('exampdf-signed.pdf', 'wb') as outf:
        pdf_signer.sign_pdf(w, output=outf)
