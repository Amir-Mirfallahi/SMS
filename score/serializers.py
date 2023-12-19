from rest_framework.serializers import ModelSerializer
from .models import Score, ReportSheetScore


class ScoreSerializer(ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'


class ReportSheetScoreSerializer(ModelSerializer):
    class Meta:
        model = ReportSheetScore
        fields = '__all__'
