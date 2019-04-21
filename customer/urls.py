from django.urls import path
from customer import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.my_login, name='my_login'),
    path('buy_package/', views.buypackage, name='buy_package'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.editprofile, name='edit_profile'),
    path('add_car/', views.addcar, name='add_car'),
    path('change_password/', views.changepassword, name='change_password'),
]