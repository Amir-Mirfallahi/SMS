from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE, verbose_name='کاربر')
    TEACHER, STUDENT = 'teacher', 'student'
    role = models.CharField(max_length=24, choices=((TEACHER, 'معلم'), (STUDENT, 'دانش آموز')), verbose_name='نقش')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Class(models.Model):
    _class = models.CharField(max_length=128, verbose_name='کلاس')

    class Meta:
        verbose_name = 'کلاس'
        verbose_name_plural = 'کلاس ها'

    def __str__(self):
        return f"{self._class}"


class Subject(models.Model):
    subject = models.CharField(max_length=128, verbose_name='درس')

    class Meta:
        verbose_name = 'درس'
        verbose_name_plural = 'دروس'

    def __str__(self):
        return self.subject


class TaughtClass(models.Model):
    _class = models.ForeignKey(Class, models.CASCADE, verbose_name='کلاس')
    subject = models.ForeignKey(Subject, models.CASCADE, verbose_name='درس')

    class Meta:
        verbose_name = 'کلاس قابل تدریس'
        verbose_name_plural = 'کلاس های قابل تدریس'

    def __str__(self):
        return f"{self._class}-{self.subject}"


class Student(models.Model):
    profile = models.OneToOneField(Profile, models.CASCADE, related_name='student', verbose_name='کاربر', unique=True)
    _class = models.ForeignKey(Class, models.CASCADE, verbose_name='کلاس')

    class Meta:
        verbose_name = 'دانش آموز'
        verbose_name_plural = 'دانش آموزان'

    def __str__(self):
        return self.profile.user.get_full_name()


class Teacher(models.Model):
    profile = models.OneToOneField(Profile, models.CASCADE, related_name='teacher', verbose_name='کاربر', unique=True)
    taught_class = models.ManyToManyField(TaughtClass, related_name='teacher', verbose_name='کلاس ها')

    class Meta:
        verbose_name = 'معلم'
        verbose_name_plural = 'معلمان'

    def __str__(self):
        return self.profile.user.get_full_name()
