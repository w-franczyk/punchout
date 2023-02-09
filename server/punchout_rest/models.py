from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id}. {self.name}"

class Category(models.Model):
    name = models.CharField(max_length=255)
    colour = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.id}. {self.name}, {self.colour}"

class Task(models.Model):
    title = models.CharField(max_length=1234)
    details = models.CharField(max_length=1234)
    categoryId = models.ForeignKey(Category, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.id}. {self.title}, {self.categoryId}"

class TaskTag(models.Model):
    taskId = models.ForeignKey(Task, on_delete=models.CASCADE)
    tagId = models.ForeignKey(Tag, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.id}. {self.taskId} to {self.tagId}"
