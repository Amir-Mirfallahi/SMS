from django.db import models

from panel.models import Student, TaughtClass


class Semester(models.Model):
    semester = models.CharField(max_length=128, verbose_name='ترم')

    class Meta:
        verbose_name = 'ترم'
        verbose_name_plural = 'ترم ها'

    def __str__(self):
        return self.semester


class Score(models.Model):
    student = models.ForeignKey(Student, models.CASCADE, verbose_name='دانش آموز', related_name='scores')
    taught_class = models.ForeignKey(TaughtClass, models.CASCADE, verbose_name='درس')
    semester = models.ForeignKey(Semester, models.CASCADE)
    continuous_score = models.FloatField(verbose_name='نمره')

    modified_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    update_date = models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        verbose_name = 'نمره'
        verbose_name_plural = 'نمرات'

    def __str__(self):
        return f'{self.student}: {self.continuous_score}'
