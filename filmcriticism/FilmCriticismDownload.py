# -*- coding: utf-8 -*-
#爱情公寓
import requests
import time
import random
import json
import util.DateUtil as dateUtil


def parsePage(html):
    data = json.loads(html)['cmts']#获取评论内容
    for item in data:
        yield{
            'date': item['time'].split(' ')[0],
            'conment': item['content'],
            'nickname': item['nickName'],
            'city': item['cityName'],
            'rate': item['score']

        }
        # return json.loads(html)['cmts']



def getPage(url):
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.text
    return None


def downloadAndSaveFile(filmId, pageCount, filename):
    for i in range(1, pageCount + 1):
        print("%s,page=%d" % (dateUtil.timeToStr(time.localtime()), i))
        url = 'http://m.maoyan.com/mmdb/comments/movie/' + filmId + '.json?_v_=yes&offset=' + str(i)
        html = getPage(url)
        data = parsePage(html)
        for item in data:
            with open(filename + '.txt', 'a', encoding='utf-8') as f:
                # f.write(item['date'] + ','+item['nickname'] + ',' + item['city'] + ',' + str(item['rate']) + ',' + item['conment']+'\n')
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
                #time.sleep(random.randint(1,100)/20)
        time.sleep(2)


def duplicateRemoval(old, new):
    oldfile = open(old, 'r', encoding='utf-8')
    newfile = open(new, 'w', encoding='utf-8')
    content_list = oldfile.readlines()
    content_alread = []
    for line in content_list:
        if line not in content_alread:
            newfile.write(line)
            content_alread.append(line)


if __name__ == '__main__':
    #爱情公寓
    filmId = '1175253'
    filename = '爱情公寓'

    pageCount = 10 #下载页数
    downloadAndSaveFile(filmId, pageCount, filename)
    duplicateRemoval(filename + '.txt', filename + '(去重).txt')
    print("end")