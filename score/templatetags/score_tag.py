from django.db.models import Avg
from django.template import Library

from score.models import Score, ReportSheetScore

register = Library()


@register.filter
def average_score(taught_class):
    average = Score.objects.filter(taught_class=taught_class).aggregate(
        Avg('continuous_score'))['continuous_score__avg']
    return round(average, 2) if average is not None else 'NA'


@register.filter
def average_report_sheet_score(taught_class):
    average = ReportSheetScore.objects.filter(taught_class=taught_class).aggregate(
        Avg('report_sheet_score'))['report_sheet_score__avg']
    return round(average, 2) if average is not None else 'NA'


@register.filter
def score_filter(scores, taught_class):
    return scores.filter(taught_class_id=taught_class)
