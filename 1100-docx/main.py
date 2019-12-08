from docx import Document
from docx.shared import Inches

document = Document('demo.docx')

print(document.element.xml)
for i, p in enumerate(document.inline_shapes):
    print(i, p.text)


