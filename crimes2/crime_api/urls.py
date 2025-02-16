from django.urls import path
from .views import reports_by_crime_code, CrimeReportListCreateView, CrimeReportDetailView, UpvoteListCreateView

urlpatterns = [
    path('crime-reports/', CrimeReportListCreateView.as_view(), name='crime-list'),
    path('crime-reports/<int:pk>/', CrimeReportDetailView.as_view(), name='crime-detail'),
    path('upvotes/', UpvoteListCreateView.as_view(), name='upvote-list'),
    path('crime-reports/by-crime-code/', reports_by_crime_code, name='crime-reports-by-code'),
]
