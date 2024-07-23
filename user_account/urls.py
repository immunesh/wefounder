from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PasswordReset, PasswordResetConfirm
from .views import search_profiles

urlpatterns = [
    path('account/@<str:username>/', views.userProfile, name='viewProfile'),
    path('update/@<str:username>/', views.updateProfile, name='updateProfile'),
    path('profile/@<str:username>/', views.profile, name='profile'),
    path('signup/', views.signUp, name='signUp'),
    path('signup-steps/<int:user_id>/', views.signUpSteps, name='signUpSteps'),
    path('login/', views.signIn, name='signin'),
    path('logout/', views.logOut, name='logout'),
    path('account-notification/', views.accountNotification, name='account_notification'),
    # path('account-projects/', views.accountProjects, name='account_projects'),
    path('addmyproject/',views.Add_My_Project,name='addmyproject'),
    path('accountProject/update/<int:id>/', views.accountProject_update, name='accountProject_update'),
    path('account-projects_delete/<id>/', views.ProjectDelete, name="account-projects_delete"),
    path('search/', search_profiles, name='search_profiles'),
    path('message/', views.message, name='message'),
    path('chat/<int:user_id>/', views.chat_view, name='chat_user'),
    path('chat/', views.chat_list_view, name='chat_list'),
    path('chat/<int:receiver_id>/', views.chat_view, name='chat'),
    path('chat/messages/', views.chat_messages, name='chat_messages'),
    path('messages/', views.Messages, name='messages'),
    path('chat/', views.chat, name='chat'),
    path('password_reset/', PasswordReset, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirm, name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
    path('set-chat-user/', views.set_chat_user, name='set_chat_user'),    
]
