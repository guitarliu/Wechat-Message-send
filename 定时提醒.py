# coding: UTF-8

from datetime import datetime, date

import itchat, sys

import xlrd

from apscheduler.schedulers.background import BlockingScheduler

# reload(sys)

# sys.setdefaultencoding('utf-8')



def SentChatRoomsMsg(name, context, **kwargs):

    group = itchat.get_chatrooms(update = True)   # ����΢��Ⱥ����������Ϣ

    iRoom = itchat.search_chatrooms(name)  # ͨ�����ֲ���ĳ��΢��Ⱥ�������Ϣ

    for item in iRoom:

            userName = item['UserName']

    itchat.send_msg(context, userName)

    print '����ʱ��: ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"

    print "���͵�: " + name + "\n"

    print  "��������: " + context + "\n"

    print "*********************************************************************************"

    scheduler.print_jobs()


def loginCallback():

    print '\n***��¼�ɹ�***\n'



def exitCallback():

    print '\n***���˳�***\n'





itchat.auto_login(hotReload = True, enableCmdQR = True, loginCallback = loginCallback, exitCallback = exitCallback)

workbook = xlrd.open_workbook('C:/Users/24706/desktop/��ʱ����/AutoSentChatroom.xlsx')

sheet = workbook.sheet_by_name("Chatrooms")   # ����sheet���ƻ��sheet����

iRows = sheet.nrows # ��ȡsheet������



scheduler = BlockingScheduler()

index = 1

for i in range(1, iRows):  # �ӵ�һ�е���iRows�У����λ�ȡ��������

    textList = sheet.row_values(i)  # ��ȡ��i�е����ݣ�����һ��list����

    name = textList[0]  # ��ȡ��i�еĵ�һ�������

    context = textList[2]  # ��ȡ��i�еĵ�3������

    float_datetime = textList[1]  # ��ȡ��i�еĵ�2������

    date_value = xlrd.xldate_as_tuple(float_datetime, workbook.datemode)

    date_value = datetime(*date_value[:5])  # ��ʱ��ת��Ϊ�ԡ�****/**/** **:**:**������ʽ

    if datetime.now() > date_value:

        continue

    date_value = date_value.strftime('%Y-%m-%d %H:%M:%S')  # ����ʱʱ��ת��Ϊ�ض���ʽ

    textList[1] = date_value

    scheduler.add_job(SentChatRoomsMsg, 'date', run_date = date_value, kwargs = {'name': name, 'context': context})

    print '����' +str(index) + ':\n'

    print '������ʱ��: ' + date_value + '\n'

    print '�����͵�: '.decode('gbk') + name + '\n'

    print '����������: '.decode('gbk') + context + '\n'

    print '****************************************************************************\n'

    index = index + 1

if index == 1:

    print '\n***û��������Ҫִ��***\n'

scheduler.start()

