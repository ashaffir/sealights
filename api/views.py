import logging
from re import T
from django.core import exceptions
from django.db.models.query_utils import Q

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from api.models import Note, Report

from .serializers import NotePostSerializer, NoteReadSerializer
from api import serializers

logger = logging.getLogger(__file__)


class NotePostAPIView(GenericAPIView):
    """API endpoint for adding a user note"""

    serializer_class = NotePostSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = User.objects.get(id=request.data["user_id"])
        except:
            return Response(
                {"error": "Failed to get user"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            report = Report.objects.get(report_id=request.data["report_id"])
        except:
            return Response(
                {"error": "Failed to get report"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            file = serializer.validated_data["file"]
        except:
            file = None
        try:
            note = Note(
                user=user,
                report=report,
                content=serializer.validated_data["content"],
                public=serializer.validated_data["public"],
                file=file,
            )

            note.save()

        except Exception as e:
            logger.error(f"Failed creating a note. Error: {e}")
            return Response({"error": e.args}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"ok": "Note saved"}, status=status.HTTP_201_CREATED)


class NoteReadAPIView(GenericAPIView):
    """read notes
    arguments:
    report_id[int]
    user_id[int]
    """

    serializer_class = NoteReadSerializer

    def get(self, request):

        try:
            report = Report.objects.get(report_id=request.GET["report_id"])
            user = User.objects.get(id=request.GET["user_id"])
        except exceptions.ObjectDoesNotExist as e:
            return Response({"error": e.args}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve notes for the report that either public or the user wrote them
        notes = Note.objects.filter(Q(report=report) & (Q(public=True) | Q(user=user)))

        serializer = self.serializer_class(notes, many=True)
        return Response({"notes": serializer.data}, status=status.HTTP_200_OK)
