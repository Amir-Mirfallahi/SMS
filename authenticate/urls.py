from django.urls import path
from .views import AuthenticationView, UserLogoutView

urlpatterns = [
    path('login/', AuthenticationView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout")
]
