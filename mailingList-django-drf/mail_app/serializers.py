import datetime

from django.core.serializers import serialize
from django.utils import timezone
from rest_framework import serializers

from .models import Client, Message, MailingList
from .tasks import send_message


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['phone_number', 'operator_code', 'tag', 'timezone']


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['datetime_create', 'status', 'mailing_list', 'client']


class MailingListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MailingList
        fields = ['datetime_launch', 'text', 'client_filter', 'datetime_end']

    def create(self, validated_data):

        # datetime_launch = validated_data['datetime_launch']
        mailing_list_instance = serializers.HyperlinkedModelSerializer.create(self, validated_data)
        # serialized_data = serialize('json', (mailing_list_instance, ))
        # delta = validated_data['datetime_launch'] - validated_data['datetime_end']
        now = timezone.now()
        # if mailing_list_instance.datetime_launch <= now <= mailing_list_instance.datetime_end:
        #     print('between')
        #     task = send_message.apply_async(
        #         (serialized_data,),
        #         expires=mailing_list_instance.datetime_end
        #     )
        # elif now < mailing_list_instance.datetime_launch:
        #     print('greater')
        #     # delta = mailing_list_instance.datetime_launch - now
        #     task = send_message.apply_async(
        #         (serialized_data,),
        #         eta=mailing_list_instance.datetime_launch,
        #         expires=mailing_list_instance.datetime_end
        #     )

        if mailing_list_instance.datetime_launch <= now <= mailing_list_instance.datetime_end:
            print('between')
            task = send_message.apply_async(
                (mailing_list_instance.pk,),
                expires=mailing_list_instance.datetime_end
            )
        elif now < mailing_list_instance.datetime_launch:
            print('greater')
            # delta = mailing_list_instance.datetime_launch - now
            task = send_message.apply_async(
                (mailing_list_instance.pk,),
                eta=mailing_list_instance.datetime_launch,
                expires=mailing_list_instance.datetime_end
            )
            # return JsonResponse({'task_id': task.id}, status=202)

        return mailing_list_instance
