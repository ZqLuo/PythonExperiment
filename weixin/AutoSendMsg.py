import platform
from datetime import datetime
import itchat
import os
from apscheduler.schedulers.background import BlockingScheduler

isWindows = platform.system() == 'Windows'

# 发送消息到微信群  name=微信群名称，context=发送内容
def SentChatRoomsMsg(name, context):
    itchat.get_chatrooms(update=True)
    iRoom = itchat.search_chatrooms(name)

    for room in iRoom:
        if room['NickName'] == name:
            userName = room['UserName']
            break
    itchat.send_msg(context, userName)
    print("发送时间：" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
                                                                   "发送到：" + name + "\n"
                                                                                   "发送内容：" + context + "\n")
    print("*********************************************************************************")
    #scheduler.print_jobs()

# 发送消息给好友 name=备注名称，context=发送内容
def SentFriendMsg(name,context):
    iFriends = itchat.search_friends(name)
    userName = None
    for friend in iFriends:
        userName = friend['UserName']
        break
    if(userName != None):
        itchat.send(context, userName)
        print("发送时间：" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
                                                                       "发送到：" + name + "\n"
                                                                                       "发送内容：" + context + "\n")
        print("*********************************************************************************")
    else:
        print("未查询到微信好友：" + name)
        print("*********************************************************************************")

def loginCallback():
    print("***登录成功***")


def exitCallback():
    print("***已退出***")

if(isWindows):
    itchat.auto_login(hotReload=True, enableCmdQR=True, loginCallback=loginCallback, exitCallback=exitCallback)
else:
    itchat.auto_login(hotReload=True, enableCmdQR=2, loginCallback=loginCallback, exitCallback=exitCallback)

if __name__ == '__main__':
    # SentFriendMsg('昵称', "自动发送")
    SentChatRoomsMsg('自动发送微信消息测试', '当前内容为自动发送')