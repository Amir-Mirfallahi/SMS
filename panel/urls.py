from django.urls import path, include
from .views import *

urlpatterns = [
    path("", DashboardView.as_view(), name='dashboard'),
    path("scores/", include('score.urls'))
]
