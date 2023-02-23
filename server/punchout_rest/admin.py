from django.contrib import admin
from .models import Tag, Category, Task, TaskTag, Board

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(TaskTag)
admin.site.register(Board)
