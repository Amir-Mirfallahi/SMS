from django.urls import path
from .views import *

urlpatterns = [
    path('manage/', SelectClassView.as_view(), name='manage_scores'),
    path('manage/<taughtclass_id>/<semester_id>', EnterScoresView.as_view(), name='enter_scores'),
    path('create-score-api/', ScoreCreateApiView.as_view(), name='create_score')
]