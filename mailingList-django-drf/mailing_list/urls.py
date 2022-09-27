from django.urls import include, path
from rest_framework import routers
from mail_app import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'mailing-lists', views.MailingListViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('mail_app', include('mail_app.urls', namespace='mail_app')),
]
