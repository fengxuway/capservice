from django.db import models


class CapData(models.Model):
    title = models.CharField(max_length=200)
    file_path = models.FileField(upload_to="static/files", default="")
