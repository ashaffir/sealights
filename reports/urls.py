from django.urls import path

from . import views

app_name = "reports"

urlpatterns = [
    path("report/", views.AddReportAPIView.as_view(), name="report"),
]
