from django.contrib import admin
from .models import Tag, Category, Task, TaskTag

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(TaskTag)
