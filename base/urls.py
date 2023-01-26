from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.loginPage,name='login'),
     path('register/',views.registerPage,name='register'),
    path('logout/',views.logoutUser,name='logout'),

    path('',views.home,name='home'),
    path('room/<str:pk>/',views.room,name='room'),
     path('profile/<str:pk>/',views.userProfile,name='user-profile'),
    path('create-room/',views.CreateRoom,name='create-room'),
    path('update-room/<str:pk>/',views.updateRoom,name='update-room'),
    path('delete-room/<str:pk>/',views.deleteRoom,name='delete-room'),
    path('message-delete/<str:pk>/',views.deleteMessage,name='message-delete'),

    path('update-user/',views.UpdateUser,name='update-user'),
    path('topics/',views.TopicsPage,name='topics'),
    path('activity/',views.activityPage,name='activity'),
]
