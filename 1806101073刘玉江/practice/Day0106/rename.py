import os


def readname():
    filePath = 'C:\\Users\\19145\\Desktop\\作业\\作业10'
    name = os.listdir(filePath)
    for i in range(0, 39):
        name[i] = name[i][28:]
    return name


def rename(name):
    filePath = 'C:\\Users\\19145\\Desktop\\作业\\作业10'
    i = 0
    for file in os.listdir(filePath):
        new_name = file.replace(file, 'WEB程序设计2018级信本3班' + name[i])
        os.rename(os.path.join(filePath, file), os.path.join(filePath, new_name))
        i = i + 1
    print('end')


if __name__ == "__main__":
    name = readname()
    rename(name)
