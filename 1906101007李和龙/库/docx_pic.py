

from docx import Document

doc = Document("1906101007李和龙第三章笔记.docx")
pic = doc.inline_shapes[1]._inline.graphic.graphicData.pic.blipFill.blip
rID = pic.embed
document_part = doc.part
image_part = document_part.related_parts[rID]


fr = open("test1.png", "wb")
fr.write(image_part._blob)
fr.close()

"""将图片读取并且保存"""