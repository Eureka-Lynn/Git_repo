from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

 
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr ='eureka_lynn@163.com'

password = 'PAERBPQKBSQKZHXX'

to_addr = '3426144438@qq.com'

smtp_server = 'smtp.163.com'
for i in range(300):
        
    msg = MIMEMultipart()
    msg['From'] = _format_addr('喜欢我黑曼巴吗 <%s>' % from_addr)
    msg['To'] = _format_addr('洛杉矶糊人 <%s>' % to_addr)
    msg['Subject'] = Header('喜欢我黑曼巴吗', 'utf-8').encode()

    # 邮件正文是MIMEText:
    msg.attach(MIMEText('<html><body bgcolor="#E6E6FA"><h1>喜欢我黑曼巴吗</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open('D:/PY/test.jpg', 'rb') as f:

    # 设置附件的MIME和文件名，这里是jpg类型:
        mime = MIMEBase('image', 'jpg', filename='test.jpg')

    # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='test.png')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')

    # 把附件的内容读进来:
        mime.set_payload(f.read())

    # 用Base64编码:
        encoders.encode_base64(mime)

    # 添加到MIMEMultipart:
        msg.attach(mime)


    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()