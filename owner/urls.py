from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('logout/', views.user_logout, name="logout"),
    # path('profile/', views.profile, name="profile"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('profile/edit', views.edit_profile, name="edit_profile"),
    path('profile/pass_change/', views.pass_change, name="pass_change"),
]