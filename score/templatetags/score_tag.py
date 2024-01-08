from datetime import date

from django.db.models import Avg
from django.template import Library

from panel.models import TaughtClass, Student
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


@register.filter
def get_scores_avg(taught_class_id):
    continuous_scores = Score.objects.filter(taught_class_id=taught_class_id)
    report_sheet_scores = ReportSheetScore.objects.filter(taught_class_id=taught_class_id)
    continuous_scores_avg = continuous_scores.aggregate(Avg('continuous_score'))['continuous_score__avg']
    report_sheet_scores_avg = report_sheet_scores.aggregate(Avg('report_sheet_score'))['report_sheet_score__avg']
    overall_avg = (continuous_scores_avg + report_sheet_scores_avg) / 2
    return round(overall_avg, 2)


@register.filter
def get_student_length(taught_class: TaughtClass):
    students = Student.objects.filter(_class=taught_class._class)
    return len(students)


@register.filter
def get_chart_label(taught_class):
    dates = ['مهر', 'آبان', 'آذر', 'بهمن', 'اسفند', 'فروردین', 'اردیبهشت']
    return dates


@register.filter
def get_chart_data(taught_class):
    dates = {
        'mehr': (date.today().replace(month=9, day=23), date.today().replace(month=10, day=22)),
        'aban': (date.today().replace(month=10, day=23), date.today().replace(month=11, day=22)),
        'azar': (date.today().replace(month=11, day=23), date.today().replace(month=12, day=22)),
        'bahman': (date.today().replace(month=1, day=23), date.today().replace(month=2, day=22)),
        'esfand': (date.today().replace(month=2, day=23), date.today().replace(month=3, day=22)),
        'farvardin': (date.today().replace(month=3, day=23), date.today().replace(month=4, day=22)),
        'ordibehesht': (date.today().replace(month=4, day=23), date.today().replace(month=5, day=22)),
    }
    mehr_scores = Score.objects.filter(modified_date__range=dates['mehr'], taught_class=taught_class)
    aban_scores = Score.objects.filter(modified_date__range=dates['aban'], taught_class=taught_class)
    azar_scores = Score.objects.filter(modified_date__range=dates['azar'], taught_class=taught_class)
    bahman_scores = Score.objects.filter(modified_date__range=dates['bahman'], taught_class=taught_class)
    esfand_scores = Score.objects.filter(modified_date__range=dates['esfand'], taught_class=taught_class)
    farvardin_scores = Score.objects.filter(modified_date__range=dates['farvardin'], taught_class=taught_class)
    ordibehesht_scores = Score.objects.filter(modified_date__range=dates['ordibehesht'], taught_class=taught_class)
    data = [
        mehr_scores if mehr_scores else 0,
        aban_scores if aban_scores else 0,
        azar_scores if azar_scores else 0,
        bahman_scores if bahman_scores else 0,
        esfand_scores if esfand_scores else 0,
        farvardin_scores if farvardin_scores else 0,
        ordibehesht_scores if ordibehesht_scores else 0,
    ]
    return data
