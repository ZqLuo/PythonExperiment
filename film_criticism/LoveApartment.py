# -*- coding: utf-8 -*-
#爱情公寓
import requests
import time
import random
import json


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


def save_to_txt(filmId):
    for i in range(1, 56):

        print("开始保存第%d页" % i)
        url = 'http://m.maoyan.com/mmdb/comments/movie/' + filmId + '.json?_v_=yes&offset=' + str(i)

        html = getPage(url)
        data = parsePage(html)
        for item in data:
            with open('爱情公寓评论.txt', 'a', encoding='utf-8') as f:
                # f.write(item['date'] + ','+item['nickname'] + ',' + item['city'] + ',' + str(item['rate']) + ',' + item['conment']+'\n')
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
                #time.sleep(random.randint(1,100)/20)
        time.sleep(2) #休眠3秒


def delete_repeat(old, new):
    oldfile = open(old, 'r', encoding='utf-8')
    newfile = open(new, 'w', encoding='utf-8')
    content_list = oldfile.readlines() #获取所有评论数据集
    content_alread = [] #存储去重后的评论数据集

    for line in content_list:
        if line not in content_alread:
            newfile.write(line+'\n')
            content_alread.append(line)


if __name__ == '__main__':
    filmId = '1175253' #爱情公寓猫眼ID
    #save_to_txt(filmId)
    delete_repeat('爱情公寓评论.txt', '爱情公寓_new.txt')
    print("end")