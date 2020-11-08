# coding: utf-8

import itchat, schedule, functools, time


RemarkName = input('请输入好友的备注微信名：')
Send_Message = input('请输入要定时发送的信息：')
itchat.auto_login(enableCmdQR=2, hotReload=True)

# How can I add generic logging to my scheduled jobs?
def with_logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('LOG: Running job "%s"' % func.__name__)
        result = func(*args, **kwargs)
        print('LOG: Job "%s" completed' % func.__name__)
        return result
    return wrapper

# First occation------function with variable
# How can I pass arguments to the job function
# do() passes extra arguments to the job function:
# def greet(name):
#     print('Hello', name)
# schedule.every(2).seconds.do(greet, name='Alice')
# schedule.every(4).seconds.do(greet, name='Bob')
#@with_logging
#def job_send_message(RemarkName, Send_Message):
#    '''
#    UserName: The UserName of wechat friends
#    Send_Message: the message to send
#    '''
#    UserName = itchat.search_friends(RemarkName)[0]['UserName']
#    itchat.send(Send_Message, toUserName=UserName)

# Second occation------function without variable
@with_logging
def job_send_message():
    UserName = itchat.search_friends(RemarkName)[0]['UserName']
    itchat.send(Send_Message, toUserName=UserName)


# schedule.every(10).minutes.do(job_send_message, RemarkName=RemarkName, Send_Message=Send_Message)  # 每隔10分钟发送一次微信消息
# schedule.every(5).seconds.do(job_send_message, RemarkName=RemarkName, Send_Message=Send_Message)   # 每隔5秒钟发送一次微信消息
# schedule.every().hour.do(job_send_message, RemarkName=RemarkName, Send_Message=Send_Message)       # 每隔小时发送一次微信消息
# schedule.every().day.at("10:30").do(job_send_message, RemarkName=RemarkName, Send_Message=Send_Message)  # 每天发送一次微信消息
# schedule.every().monday.do(job_send_message, RemarkName=RemarkName, Send_Message=Send_Message)           # 每月发送一次微信消息
# schedule.every().wednesday.at("13:15").do(job_send_message, RemarkName=RemarkName, Send_Message=Send_Message)  # 每周三13:15发送一次消息
# schedule.every().minute.at(":17").do(job_send_message, RemarkName=RemarkName, Send_Message=Send_Message)  # 在每段时间的第17分钟发送一次消息，例如 08:17发送一次，09:17也会发送一次，依次类推

schedule.every(10).minutes.do(job_send_message)  # 每隔10分钟发送一次微信消息
schedule.every(5).seconds.do(job_send_message)   # 每隔5秒钟发送一次微信消息
schedule.every().hour.do(job_send_message)       # 每隔小时发送一次微信消息
schedule.every().day.at("10:30").do(job_send_message)  # 每天发送一次微信消息
schedule.every().monday.do(job_send_message)           # 每月发送一次微信消息
schedule.every().wednesday.at("13:15").do(job_send_message)  # 每周三13:15发送一次消息
schedule.every().minute.at(":17").do(job_send_message)  # 在每段时间的第17分钟发送一次消息，例如 08:17发送一次，09:17也会发送一次，依次类推


while True:
    schedule.run_pending()
