from rest_framework import serializers
from .models import CrimeReport, Upvote
from bson import ObjectId

class CrimeReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrimeReport
        fields = '__all__'

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        """ Convert ObjectId to string when serializing """
        return str(value) if isinstance(value, ObjectId) else value

class UpvoteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()  # Keep `id` as an integer
    crime_report = ObjectIdField(source="crime_report_id")

    class Meta:
        model = Upvote
        fields = ['id', 'crime_report', 'officer_name', 'officer_email', 'officer_badge', 'date_upvoted']
