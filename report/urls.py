from report import views
from django.urls import path


urlpatterns = [
    path('report/', views.ReportList.as_view(), name='report-list')
]
