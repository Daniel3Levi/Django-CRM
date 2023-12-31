from django.urls import path
from . import views

urlpatterns = [
    #hompage
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.single_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('new_record/', views.new_record, name='new_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),

]
