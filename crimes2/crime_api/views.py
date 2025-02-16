from rest_framework import generics
from .models import CrimeReport, Upvote
from .serializers import CrimeReportSerializer, UpvoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Count

# List all crime reports or create a new one
class CrimeReportListCreateView(generics.ListCreateAPIView):
    queryset = CrimeReport.objects.all()
    serializer_class = CrimeReportSerializer

# Retrieve, update, or delete a crime report
class CrimeReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CrimeReport.objects.all()
    serializer_class = CrimeReportSerializer

# Upvote handling
class UpvoteListCreateView(generics.ListCreateAPIView):
    queryset = Upvote.objects.all()
    serializer_class = UpvoteSerializer

@api_view(['GET'])
def reports_by_crime_code(request):
    reports = CrimeReport.objects.values('crm_cd').annotate(total=Count('crm_cd')).order_by('-total')
    return Response(reports)

@api_view(['GET'])
def upvote_list(request):
    upvotes = Upvote.objects.all()  # Query all upvotes
    serializer = UpvoteSerializer(upvotes, many=True)  # Serialize the data
    return Response(serializer.data)  # Return JSON response

