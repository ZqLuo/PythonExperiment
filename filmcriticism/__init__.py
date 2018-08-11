def readFile(filePath):
    file = open(filePath, 'r', encoding='utf-8')
    for line in file:
        print(line)
