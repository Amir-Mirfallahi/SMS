from django.shortcuts import render, redirect
from django.views import View
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from panel.models import Profile, Student, TaughtClass
from .models import Semester, Score, ReportSheetScore
from .serializers import ScoreSerializer, ReportSheetScoreSerializer


class SelectClassView(View):
    template_name = 'panel/score/manage-continuous-scores.html'

    def get(self, request):
        if request.user.profile.role == Profile.STUDENT:
            return redirect('dashboard')
        context = {
            "taught_classes": request.user.profile.teacher.taught_class.all(),
            "semesters": Semester.objects.all()
        }
        return render(request, self.template_name, context)


class EnterScoresView(View):
    template_name = 'panel/score/manage-continuous-scores.html'

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
        return render(request, self.template_name, context)


class ScoreCreateApiView(CreateAPIView):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()


class ScoreUpdateApiView(UpdateAPIView):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()


class ScoreDestroyApiView(DestroyAPIView):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()


# ReportSheet Score Views
class SelectReportSheetClassView(SelectClassView):
    template_name = 'panel/score/manage-reportsheet-scores.html'


class EnterReportSheetScoresView(EnterScoresView):
    template_name = 'panel/score/manage-reportsheet-scores.html'


class ReportSheetScoreRetrieve(APIView):
    def get(self, request):
        # Using query_parameters instead of POST for a GET request.
        student = request.query_params.get('student_id')
        semester = request.query_params.get('semester_id')
        taught_class = request.query_params.get('taught_class')
        score_type = request.query_params.get('score_type')

        score, _ = ReportSheetScore.objects.get_or_create(
            student_id=student,
            semester_id=semester,
            taught_class_id=taught_class,
            score_type=score_type,
        )

        serializer = ReportSheetScoreSerializer(score)
        return Response(serializer.data)


class ReportSheetScoreUpdate(APIView):
    def put(self, request, *args, **kwargs):
        # Use a serializer for input validation and deserialization
        serializer = ReportSheetScoreSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data

            # Use `validated_data` to prevent any unexpected input.
            score = ReportSheetScore.objects.get(
                student=validated_data.get('student'),
                semester=validated_data.get('semester'),
                taught_class=validated_data.get('taught_class'),
                score_type=validated_data.get('score_type'),
            )
            score.report_sheet_score = validated_data.get('report_sheet_score')
            score.save()

            # Use the serializer instance to return the updated data.
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            # Return a 400 Bad Request response with the validation errors.
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
