from django.db import models
from users.models import User


class Report(models.Model):
    """report model for dev"""

    report_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
