from django.urls import  path
from . import views
urlpatterns = [
    path('account/@<str:username>/', views.userProfile, name='viewProfile'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signUp, name='signUp'),
    path('signup-steps/', views.signUpSteps, name='signUpSteps'),
    path('login/', views.signIn, name='signin'),
    path('logout/', views.logOut, name='logout'),
    path('delete-account/', views.deleteAccount, name='delete_account'),
    path('account-security/', views.accountSecurity, name='account_security'),
    path('account-notification/', views.accountNotification, name='account_notification'),
    path('account-projects/', views.accountProjects, name='account_projects'),
    path('payment-details/', views.paymentDetails, name='payment_details'),
    path('order/', views.order, name='order'),
    path('wishlist/', views.wishlist, name='wishlist'),
]