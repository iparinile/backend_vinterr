import os
import smtplib

from dotenv import load_dotenv

load_dotenv()


def send_email(to_address: list, subject: str, text: str, encode: str = 'utf-8'):
    """
    Отправка электронного письма (email)
    """
    # извлечение переменных из .env
    server = os.getenv('email_server', 'smtp.yandex.ru')
    port = os.getenv('email_port', 587)
    from_address = os.getenv('email_from')
    passwd = os.getenv('email_passwd')
    charset = f'Content-Type: text/html; charset={encode}'
    mime = 'MIME-Version: 1.0'
    # формируем тело письма
    body = "\r\n".join((f"From: {from_address}", f"To: {', '.join(to_address)}",
                        f"Subject: {subject}", mime, charset, "", text))

    try:
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        smtp.login(from_address, passwd)
        smtp.sendmail(from_address, to_address, body.encode(encode))
        smtp.quit()
    except smtplib.SMTPException as err:
        print('Что - то пошло не так...')
        raise err
