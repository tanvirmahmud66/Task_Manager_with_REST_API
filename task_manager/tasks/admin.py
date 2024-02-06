from django.contrib import admin
from .models import Tasks, Photos
# Register your models here.

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('id','user','title','priority','complete','due_date','created_at','updated_at')

class PhotosModelAdmin(admin.ModelAdmin):
    list_display = ('task','image')

admin.site.register(Tasks,TaskModelAdmin)
admin.site.register(Photos,PhotosModelAdmin)
