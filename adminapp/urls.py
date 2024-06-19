from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('editphotofolio/', views.editphotofolio, name='editphotofolio'),
]