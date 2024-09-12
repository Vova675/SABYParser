import smtplib
import email
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import sender_mail, sender_login, sender_pasword, recipient_mail, stmp_adress, excel_file_name

class LetterAbsenderClass:

    def __init__(self):
        """
        Инициализатор.
        Задает сообщение и тело для отправки.
        Использует sender_mail из файла config.py как почту отправителя.
        Использует sender_pasword из файла config.py как почту получателя.
        Использует sender_login из файла config.py как логин отправителя.
        Использует sender_pasword из файла config.py как пароль отправителя.
        Использует stmp_adress из файла config.py как stmp адрес.
        Использует excel_file_name из файла config.py как путь к отправляемому файлу.
        """
        self.__msg = MIMEMultipart()
        self.__msg['Subject'] = "Отчет"
        self.__msg['From'] = sender_mail
        self.__msg['To'] = recipient_mail

    def send_letter(self):
        """
        Метод для формирования структуры письма.
        Задает отправляемое сообщение и прикрепляет файл.
        """
        self.__body = MIMEText("Отчет")
        self.__msg.attach(self.__body)
        # PDF attachment
        filename = excel_file_name
        fp=open(filename,'rb')
        att = MIMEApplication(fp.read(),_subtype="xlsx")
        fp.close()
        att.add_header('Content-Disposition','attachment',filename=filename)
        self.__msg.attach(att)

        server = smtplib.SMTP(stmp_adress)
        server.starttls()
        server.login(sender_login, sender_pasword)
        server.sendmail(sender_mail,recipient_mail, self.__msg.as_string())
        server.quit()