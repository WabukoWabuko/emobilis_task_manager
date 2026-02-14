from django.contrib import admin

from .models import Task
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # This is to make the Admin dashboard more informative
    list_display = ('id', 'title', 'completed', 'created_at')
    list_filter = ('completed',)
    search_fields = ('title',)
