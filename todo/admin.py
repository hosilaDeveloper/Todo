from django.contrib import admin
from todo.models import Todo
# Register your models here.


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_done')
    list_display_links = ('id', 'title')
    list_filter = ('is_done',)
    search_fields = ('id', 'title')
