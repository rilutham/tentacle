from django.db import models
from django.utils import timezone

class Activity(models.Model):
    activity_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    latest_hour = models.IntegerField(default=0)
    total_hour = models.BigIntegerField(default=0)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.activity_name

    def update_total_hour(self):
    	self.total_hour += self.latest_hour
    	return self.total_hour

    def get_last_update(self):
    	self.updated_at = timezone.now()
    	return self.updated_at