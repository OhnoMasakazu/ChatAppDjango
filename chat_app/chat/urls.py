from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('friend',views.friend,name='friend'),
    path('login',LoginView.as_view(template_name='chat/login.html'), name='login'),
    path('talk_room/<friendname>',views.talk,name='talk'),
    path('setting',views.setting,name='setting'),
    path('username_change',views.username_change,name='username_change'),
    path('mail_change',views.mail_change,name='mail_change'),
    path('icon_change',views.icon_change,name='icon_change'),
    path('password_change',views.password_change,name='password_change'),
    path('username_done',views.username_done,name='username_done'),
    path('mail_done',views.mail_done,name='mail_done'),
    path('icon_done',views.icon_done,name='icon_done'),
    path('password_done',views.password_done,name='password_done'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('logout',views.logout,name='logout'),
]