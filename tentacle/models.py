from django.db import models
from django.utils import timezone

class Activity(models.Model):
    activity_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    latest_hour = models.IntegerField(default=0)
    total_hour = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_activity = models.ForeignKey('self', default=0)

    def __str__(self):
        return self.activity_name

    def update_total_hour(self):
    	self.total_hour += self.latest_hour
    	return self.total_hour

class Note(models.Model):
    note = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    activity = models.ForeignKey(Activity)
