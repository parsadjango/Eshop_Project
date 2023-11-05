from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUsView.as_view(), name='contact-us'),
    path('profile/', views.ProfileUserView.as_view(), name='profile-create-page'),
    path('profile-list/', views.ProfilesView.as_view(), name='profile-list')
]
