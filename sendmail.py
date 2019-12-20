# encoding: utf-8
import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


# ==============定义发送邮件 ===============

def send_mail():
    report_dir = "D:\\PycharmProjects\\skynetservicetest\\report"
    lists = os.listdir(report_dir)
    lists.sort(key=lambda fn: os.path.getmtime(report_dir + "\\" + fn) if not
    os.path.isdir(report_dir + "\\" + fn) else 0)
    print(u'最新测试生成的报告' + lists[-1])
    new_filename = lists[-1]
    # 找到最新生成的文件
    new_file = os.path.join(report_dir, lists[-1])
    f = open(new_file, 'rb')
    # 读取测试报告正文
    mail_body = f.read()
    f.close()
    # 发件人邮箱
    sender = 'jenny.he@aihuishou.com'
    # 接收人邮箱
    receiver = 'jenny.he@aihuishou.com'
    # 发送邮箱用户信息
    username = 'jenny.he@aihuishou.com'
    # 客户端授权码
    password = 'Hejia764513'

    # 通过模块构造带附件的邮件
    msg = MIMEMultipart()
    text = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(text)
    # 发送附件
    # Header()用于定义邮件标题
    msg['Subject'] = Header('资产门店接口自动化测试报告', 'utf-8')
    # 设置附件的MIME和文件名，这里是html类型:
    msg_file = MIMEText(mail_body, 'html', 'utf-8')
    # 加上必要的头信息:
    msg_file['Content-Type'] = 'application/octet-stream'
    msg_file["Content-Disposition"] = 'attachment; filename='+new_filename
    msg.attach(msg_file)
    # 发送邮件
    msg['from'] = u'何佳 <%s>' % sender
    msg['to'] = receiver
    smtp = smtplib.SMTP()
    smtp.connect('smtp.aihuishou.com')
    smtp.login(username, password)  # 登录的用户名和密码
    smtp.sendmail(msg['from'], msg['to'], msg.as_string())  # 发送邮件
    smtp.quit()
    print('sendmail success')

