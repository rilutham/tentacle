from django.contrib import admin
from .models import Activity

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_name','description','total_hour','latest_hour','created_at','updated_at')

admin.site.register(Activity, ActivityAdmin)