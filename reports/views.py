from rest_framework import exceptions, serializers, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from reports.models import Report

from users.models import User
from .serializers import ReportSerializer


class AddReportAPIView(GenericAPIView):
    """add report (dev)"""

    serializer_class = ReportSerializer

    def post(self, request):
        try:
            user = User.objects.get(id=int(request.data["user"]))
        except Exception as e:
            return Response(e.args, status=status.HTTP_400_BAD_REQUEST)

        report = Report.objects.create(user=user)
        serializer = self.serializer_class(report)
        return Response({"report": serializer.data}, status=status.HTTP_201_CREATED)
