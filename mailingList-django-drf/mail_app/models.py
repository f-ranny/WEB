from django.db import models


class MailingList(models.Model):
    datetime_launch = models.DateTimeField()
    text = models.TextField()
    client_filter = models.CharField(max_length=20)
    datetime_end = models.DateTimeField()


class Client(models.Model):
    import pytz
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    phone_number = models.PositiveIntegerField(unique=True)
    operator_code = models.PositiveSmallIntegerField()
    tag = models.CharField(max_length=20)
    timezone = models.CharField(max_length=40, choices=TIMEZONES, default='UTC')


class Message(models.Model):
    datetime_create = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=4, blank=True)
    mailing_list = models.ForeignKey(MailingList, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

#
# class StatsMailingList(models.Model):
#     mailing_list = models.ForeignKey(MailingList, on_delete=models.CASCADE)
#     total_send_messages = models.IntegerField()
    


