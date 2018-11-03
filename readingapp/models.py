from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=80)
    tag = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Topic(models.Model):
    name = models.CharField(max_length=80)
    estimation = models.IntegerField()
    pct_completed = models.IntegerField(default=0)
    details = models.TextField(default=None, blank=True, null=True)
    embed_link = models.CharField(max_length=255, default=None, blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


