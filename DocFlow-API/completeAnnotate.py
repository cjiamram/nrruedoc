from fitz import fitz, Rect

doc = fitz.open("Letter.pdf")
w = 300
h = 700

def add_footer(pdf):
    img = open("signature.jpg", "rb").read()
    rect = fitz.Rect(0, 600, w, h)

    for i in range(0, pdf.page_count):
        page = pdf[i]
        if not page.is_wrapped:
            page._wrapContents()
        page.insert_image(rect, stream=img)

add_footer(doc)
doc.save('test_pdf5.pdf')
