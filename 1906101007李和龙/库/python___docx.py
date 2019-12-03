import docx

def read(path):
    document = docx.Document(path)
    for paragraph in document.paragraphs:
        print(paragraph.text)
if __name__ == "__main__":
    path = input("请输入绝对路径：")
    print(read(path))