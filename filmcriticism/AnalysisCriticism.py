import util.FileUtil as fileUtil
import json

list = fileUtil.readFileToList('/Users/zqLuo/Documents/pythoneworkspace/PythonExperiment/filmcriticism/DuplicateRemoval_LoveApartment.txt','\n')
for line in list:
    jsonObj = json.loads(line)
    print(jsonObj['city'])