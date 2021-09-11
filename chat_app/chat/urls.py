from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('', views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('friend',views.friend,name='friend'),
    path('login/',LoginView.as_view(template_name='chat/login.html'), name="login"),
]