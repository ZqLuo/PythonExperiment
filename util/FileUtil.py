def readFileToList(filePath,strip):
    file = open(filePath, 'r', encoding='utf-8')
    strList = []
    for line in file:
        strList.append(line.strip(strip))
    return strList


def writeListToFile(comment,filePath):
    for item in comment:
        with open(filePath, 'a', encoding='utf-8') as f:
            f.write(item + '\n')