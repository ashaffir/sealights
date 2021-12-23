import logging
from rest_framework import serializers
from django.core import exceptions
from decouple import config
from .models import Note, Report
from users.models import User
from api import models

logger = logging.getLogger(__file__)


class NotePostSerializer(serializers.Serializer):
    """Serializing the note"""

    content = serializers.CharField()
    file = serializers.FileField(allow_null=True, allow_empty_file=True, required=False)
    public = serializers.BooleanField()
    user_id = serializers.CharField()
    report_id = serializers.CharField()

    def validate(self, attrs):

        # Check if file attached to note
        try:
            file = attrs["file"]
        except:
            return super().validate(attrs)

        # Checking the size of the uploaded file
        if attrs["file"].size > int(config("MAX_UPLOAD_SIZE")):
            raise exceptions.ValidationError("File is too big")

        # Checking file type
        forbidden_file_types = config("FORBIDDNE_FILES").split(",")
        if attrs["file"].name.split(".")[-1] in forbidden_file_types:
            raise exceptions.ValidationError("File type not allowed")

        return super().validate(attrs)


class NoteReadSerializer(serializers.ModelSerializer):
    """Serializing note for read"""

    report_id = serializers.CharField()

    class Meta:
        model = Note
        exclude = ("user",)
