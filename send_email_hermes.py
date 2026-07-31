"""双击运行即可发送Hermes课程HTML到QQ邮箱"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

QQ = '287257449@qq.com'
AUTH = 'kfabgfcfyhqhcbae'

m = MIMEMultipart()
m['From'] = m['To'] = QQ
m['Subject'] = 'Hermes课程HTML'

body = '用AI Agent打造你的数字员工及AI团队（Hermes实战开发课程）\n线上地址：https://junezhu.com.cn/hermes-course.html'
m.attach(MIMEText(body, 'plain', 'utf-8'))

with open(r'D:\tuv-west-deploy\hermes-course.html', 'rb') as f:
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(f.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', 'attachment', filename='hermes-course.html')
    m.attach(p)

s = smtplib.SMTP('smtp.qq.com', 587, timeout=60)
s.starttls()
s.login(QQ, AUTH)
s.send_message(m)
s.quit()
print('邮件发送成功！')
input('按回车关闭...')
