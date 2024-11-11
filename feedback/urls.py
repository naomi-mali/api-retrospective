from django.urls import path
from feedback import views


urlpatterns = [
    path('feedback/', views.FeedbackList.as_view()),
]