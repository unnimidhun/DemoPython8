from. import views
from django.urls import path



urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('new_page/', views.new_page, name='new_page'),
    path('registration_form/', views.registration_form, name='registration_form'),
    path('get_courses/', views.get_courses, name='get_courses'),
    path('logout', views.logout, name='logout'),
]