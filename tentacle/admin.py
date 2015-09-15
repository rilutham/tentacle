from django.contrib import admin
from .models import Activity, Note

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_name','description','total_hour','latest_hour','created_at','updated_at')

class NoteAdmin(admin.ModelAdmin):
	list_display = ('activity_id', 'note','status','created_at')

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Note, NoteAdmin)