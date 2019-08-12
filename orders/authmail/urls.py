from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import signup_views


urlpatterns = [
    path('signup/', signup_views, name='signup'),
    path('login/', LoginView.as_view(template_name='authmail/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='authmail/logout.html'), name='logout'),
]
