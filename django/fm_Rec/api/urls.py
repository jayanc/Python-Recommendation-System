from django.conf.urls import url

from .views import UserInfoView

urlpatterns = [
    url(r'^$', UserInfoView.as_view(), name='index'),
]
