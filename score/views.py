from django.shortcuts import render, redirect
from django.views import View
from rest_framework.generics import CreateAPIView

from panel.models import Profile, Student, TaughtClass
from .models import Semester, Score
from .serializers import ScoreSerializer


class SelectClassView(View):
    def get(self, request):
        if request.user.profile.role == Profile.STUDENT:
            return redirect('dashboard')
        context = {
            "taught_classes": request.user.profile.teacher.taught_class.all(),
            "semesters": Semester.objects.all()
        }
        return render(request, 'panel/score/manage-scores.html', context)


class EnterScoresView(View):
    def get(self, request, taughtclass_id, semester_id):
        if request.user.profile.role == Profile.STUDENT:
            return redirect('dashboard')
        taught_class = TaughtClass.objects.get(id=taughtclass_id)
        if taught_class not in request.user.profile.teacher.taught_class.all():
            return redirect('manage_scores')
        students = Student.objects.filter(_class=taught_class._class)
        context = {
            "students": students,
            'semester': semester_id,
            'taught_class': taught_class.id,
        }
        return render(request, 'panel/score/manage-scores.html', context)


class ScoreCreateApiView(CreateAPIView):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()
