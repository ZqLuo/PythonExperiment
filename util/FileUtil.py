def readFileToList(filePath,strip):
    file = open(filePath, 'r', encoding='utf-8')
    strList = []
    for line in file:
        strList.append(line.strip(strip))
    return strList