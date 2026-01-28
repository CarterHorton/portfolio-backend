from datetime import datetime, timezone
from django.db import models

# Create your models here.
class projectEntry(models.Model):
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    date_started = models.DateTimeField("date published")
    date_updated = models.DateTimeField("date updated")
    def __str__(self):
        return self.project_name

class journalEntry(models.Model):
    header = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    date_pub = models.DateTimeField("date published")
    project_entry = models.ForeignKey(projectEntry, on_delete=models.CASCADE)
    def __str__(self):
        return self.header
    def was_published_recently(self):
        return self.date_pub <= timezone.now() - datetime.timedelta(days=1)