# coding: UTF-8

from datetime import datetime, date

import itchat, sys

import xlrd

from apscheduler.schedulers.background import BlockingScheduler

# reload(sys)

# sys.setdefaultencoding('utf-8')



def SentChatRoomsMsg(name, context, **kwargs):

    group = itchat.get_chatrooms(update = True)   # 更新微信群的数量等信息

    iRoom = itchat.search_chatrooms(name)  # 通过名字查找某个微信群的相关信息

    for item in iRoom:

            userName = item['UserName']

    itchat.send_msg(context, userName)

    print '发送时间: ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"

    print "发送到: " + name + "\n"

    print  "发送内容: " + context + "\n"

    print "*********************************************************************************"

    scheduler.print_jobs()


def loginCallback():

    print '\n***登录成功***\n'



def exitCallback():

    print '\n***已退出***\n'





itchat.auto_login(hotReload = True, enableCmdQR = True, loginCallback = loginCallback, exitCallback = exitCallback)

workbook = xlrd.open_workbook('C:/Users/24706/desktop/定时提醒/AutoSentChatroom.xlsx')

sheet = workbook.sheet_by_name("Chatrooms")   # 根据sheet名称获得sheet内容

iRows = sheet.nrows # 获取sheet的行数



scheduler = BlockingScheduler()

index = 1

for i in range(1, iRows):  # 从第一行到第iRows行，依次获取其中内容

    textList = sheet.row_values(i)  # 获取第i行的内容，返回一个list对象

    name = textList[0]  # 获取第i行的第一项的内容

    context = textList[2]  # 获取第i行的第3项内容

    float_datetime = textList[1]  # 获取第i行的第2项内容

    date_value = xlrd.xldate_as_tuple(float_datetime, workbook.datemode)

    date_value = datetime(*date_value[:5])  # 将时间转化为以“****/**/** **:**:**”的形式

    if datetime.now() > date_value:

        continue

    date_value = date_value.strftime('%Y-%m-%d %H:%M:%S')  # 将定时时间转化为特定格式

    textList[1] = date_value

    scheduler.add_job(SentChatRoomsMsg, 'date', run_date = date_value, kwargs = {'name': name, 'context': context})

    print '任务' +str(index) + ':\n'

    print '待发送时间: ' + date_value + '\n'

    print '待发送到: '.decode('gbk') + name + '\n'

    print '待发送内容: '.decode('gbk') + context + '\n'

    print '****************************************************************************\n'

    index = index + 1

if index == 1:

    print '\n***没有任务需要执行***\n'

scheduler.start()

