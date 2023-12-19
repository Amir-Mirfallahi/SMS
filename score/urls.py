from django.urls import path

from .views import *

urlpatterns = [
    # Continuous Score Views
    path('manage/', SelectClassView.as_view(), name='manage_scores'),
    path('manage/<int:taughtclass_id>/<int:semester_id>', EnterScoresView.as_view(), name='enter_scores'),
    path('create-score-api/', ScoreCreateApiView.as_view(), name='create_score'),
    path('update-score-api/<pk>', ScoreUpdateApiView.as_view(), name='update_score'),
    path('destroy-score-api/<pk>', ScoreDestroyApiView.as_view(), name='destroy_score'),
    # ReportSheet Score Views
    path('manage/report-sheet/', SelectReportSheetClassView.as_view(), name='manage_report_sheet_scores'),
    path('manage/report-sheet/<int:taughtclass_id>/<int:semester_id>', EnterReportSheetScoresView.as_view(),
         name='enter_report_sheet_scores'),
    path('get-report-sheet-score/', ReportSheetScoreRetrieve.as_view(), name='report_sheet_retrieve'),
    path('update-report-sheet-score/', ReportSheetScoreUpdate.as_view(), name='report_sheet_retrieve_update')
]
