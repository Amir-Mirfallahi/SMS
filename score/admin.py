from django.contrib import admin

from .models import Score, Semester, ReportSheetScore


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('student', 'continuous_score')
    search_fields = ('student__profile__user__first_name', 'student__profile__user__last_name')


@admin.register(ReportSheetScore)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('student', 'report_sheet_score')
    search_fields = ('student__profile__user__first_name', 'student__profile__user__last_name')


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('semester',)
