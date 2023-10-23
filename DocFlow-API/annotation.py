from pdf_annotate import PdfAnnotator, Appearance, Location

annotator = PdfAnnotator('Letter.pdf')

annotator.add_annotation(
               'text',
                Location(x1=10, y1=10, x2=100, y2=100, page=0),
                Appearance(content='Review...', font_size=10,  fill=(0,0,0)),
                )

annotator.write('annotated.pdf')
