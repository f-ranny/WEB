# from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
# from rest_framework import permissions
from mail_app.serializers import ClientSerializer, MessageSerializer, MailingListSerializer

from .models import Client, MailingList, Message


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = [permissions.IsAuthenticated]


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # permission_classes = [permissions.IsAuthenticated]


class MailingListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows mailing lists to be viewed or edited.
    """
    queryset = MailingList.objects.all()
    serializer_class = MailingListSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def list(self, request, *args, **kwargs):
    #     queryset = MailingList.objects.all()
    #     serializer =



# def run_task(request):
#     task = create_task.delay(task_type=1)
#     return JsonResponse({'task_id': task.id}, status=202)
