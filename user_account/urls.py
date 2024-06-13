from django.urls import  path
from . import views
urlpatterns = [
    path('account/@<str:username>/', views.userProfile, name='viewProfile'),
    path('update/@<str:username>/', views.updateProfile, name='updateProfile'),
    path('profile/@<str:username>/', views.profile, name='profile'),
    path('signup/', views.signUp, name='signUp'),
    path('signup-steps/<int:user_id>/', views.signUpSteps, name='signUpSteps'),
    path('login/', views.signIn, name='signin'),
    path('logout/', views.logOut, name='logout'),
    path('account-notification/', views.accountNotification, name='account_notification'),
    path('account-projects/', views.accountProjects, name='account_projects'),
    path('accountProject/update/<id>/',views.accountProject_update, name="accountProject_update"),
    path('account-projects_delete/<id>', views.delete, name="account-projects_delete"),
    path('wishlist/', views.wishlist, name='wishlist'),
]