# from django.contrib import admin
# from .models import Task

# # Register your models here.
# admin.site.register(Task)

from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'created_at')
