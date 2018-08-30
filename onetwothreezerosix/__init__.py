import requests
import RequestUtil
import FileUtil


def saveAllStatioinName():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
    html = RequestUtil.getPage(url)
    names = html.split('@')
    FileUtil.writeListToFile(names, 'station_name.txt')


if __name__ == '__main__':
    saveAllStatioinName()
    print('end')