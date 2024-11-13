# report/urls.py
from django.urls import path
from . import views
from .views import ReportList

urlpatterns = [
    path('report/', ReportList.as_view(), name='report-list'),

]
