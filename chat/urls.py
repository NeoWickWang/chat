from django.urls import path
 
from . import views

app_name = 'chat' 

urlpatterns = [
    # path('', views.index, name='index')
    path('room/', views.selectRoom, name='select-room'),   # 房间选择
    path('<str:room_name>/', views.room, name='room'),
    path('login/',views.log_in,name='login'),
    path('logon/',views.logon,name='logon'),
    path('logout/', views.logout, name='logout'),
    path('reset/', views.logout, name='reset'),
    path('main/', views.main, name='main')

]