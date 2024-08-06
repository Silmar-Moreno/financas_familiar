from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('erro/', views.erro_view, name='erro'),
    path('logout/', views.logout_view, name='logout'),

]
