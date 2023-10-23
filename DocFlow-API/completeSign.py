from pyhanko import stamp
from pyhanko.pdf_utils import text, images
from pyhanko.pdf_utils.font import opentype
from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign import fields, signers


signer = signers.SimpleSigner.load_pkcs12(
    pfx_file='chatchai.j.p12', passphrase=b'Bangy135#'
)
with open('Letter.pdf', 'rb') as inf:
    w = IncrementalPdfFileWriter(inf)
    fields.append_signature_field(
        w, sig_field_spec=fields.SigFieldSpec(
            'Signature', box=(200, 50, 400, 110)
        )
    )

    meta = signers.PdfSignatureMetadata(field_name='Signature')
    pdf_signer = signers.PdfSigner(
        meta, signer=signer, stamp_style=stamp.TextStampStyle(
            # the 'signer' and 'ts' parameters will be interpolated by pyHanko, if present
            #stamp_text='Test Digital Siganture TUC!\n sign by: %(signer)s\nTime: %(ts)s',
            # text_box_style=text.TextBoxStyle(
            #     # font=opentype.GlyphAccumulatorFactory('signature.jpg')
            # ),
            background=images.PdfImage('Stamp.jpg')

        ),
    )
    with open('example-signed.pdf', 'wb') as outf:
        pdf_signer.sign_pdf(w, output=outf)
