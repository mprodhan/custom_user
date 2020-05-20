from django.urls import path
from  custom_user_app import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('login/', views.loginview),
    path('logout/', views.logout),
    path("signup/", views.signup)
]

