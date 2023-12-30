from django.urls import path
 
from . import views

app_name = 'chat' 

urlpatterns = [
    path('room/', views.index, name='index'),   # 房间选择
    path('room/<str:room_name>/', views.room, name='room'),
    path('login/',views.log_in,name='login'),
    path('logon/',views.logon,name='logon'),
    path('logout/', views.logout, name='logout'),
    path('reset/', views.logout, name='reset'),

]