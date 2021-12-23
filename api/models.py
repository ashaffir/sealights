from django.db import models

from users.models import User
from reports.models import Report


class Note(models.Model):
    """A note object that can be used for private and publically shared notes from users"""

    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)
    content = models.CharField(max_length=500)

    # TODO: Files should uploaded to an S3 storage
    file = models.FileField(upload_to="files/%Y/%m/%d", blank=True, null=True)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self) -> str:
        return f"{self.user}-{self.content}"
