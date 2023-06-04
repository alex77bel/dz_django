from django.core.mail import send_mail

from config import settings


def sendmail(message):  # отправка письма
    send_mail(
        'Рассылка Django',
        message,
        settings.EMAIL_HOST_USER,
        ['alex77bel@yandex.ru',],
    )
