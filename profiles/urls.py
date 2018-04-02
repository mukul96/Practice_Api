from django.conf.urls import url
from profiles import views

urlpatterns = [
    url(r'^users$', views.users_list,name='users'),
    url(r'^users/(?P<username>[a-zA-z0-9]+)/info$', views.specific_user,name='user_detail'),
    url(r'^users/(?P<username>[a-zA-z0-9]+)/gender$', views.user_gender, name='user_gender'),

]