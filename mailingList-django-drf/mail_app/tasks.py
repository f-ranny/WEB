import json

from django.core.serializers import deserialize

import requests

from celery import shared_task

from .models import Client, Message, MailingList
from mailing_list import settings


@shared_task
def send_message(mailing_list_instance_pk: int):
    session = requests.Session()
    session.headers.update({'Authorization': f'bearer {settings.ACCESS_TOKEN}'})
    # mailing_list_instance = next(deserialize('json', mailing_list_instance))[0]
    mailing_list_instance = MailingList.objects.get(pk=mailing_list_instance_pk)
    if mailing_list_instance.client_filter.isnumeric():
        filtered_clients = Client.objects.filter(operator_code=mailing_list_instance.client_filter)
    else:
        filtered_clients = Client.objects.filter(tag=mailing_list_instance.client_filter)

    try:
        for client in filtered_clients:
            message = Message.objects.create(mailing_list=mailing_list_instance, client=client)
            r = session.post(f'https://probe.fbrq.cloud/v1/send/{message.pk}', data=json.dumps({
                'id': message.pk,
                'phone': message.client.phone_number,
                'text': message.mailing_list.text,
            }))
            message.status = r.json().get('message')
            message.save()
    except Exception as err:
        print(f'Some error while sending request: {err}')

    return True
