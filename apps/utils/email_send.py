from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord, UserProfile
from movie.settings import EMAIL_FROM


# 生成随机字符串
def random_str(random_length=8):
    str = ''
    # 生成随机字符串
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str = str + chars[random.randint(0, length)]
    return str


# 发送注册邮件
def send_register_email(email, send_type='register'):
    # 发送之前先保存到数据库，到时候查询链接是否存在
    # 实例化一个EmailVerifyRecord对象
    email_record = EmailVerifyRecord()
    # 生成随机的code放入链接
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type

    email_record.save()

    # 编写邮件
    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '微电影注册激活链接'
        email_body = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        # 如果发送成功
        if send_status:
            pass

    if send_type == 'forget':
        email_title = '微电影账号找回链接'
        email_body = "请点击下面的链接找回你的密码: http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        # 如果发送成功
        if send_status:
            pass

