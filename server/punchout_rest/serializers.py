from rest_framework import serializers
from .models import Tag, Category, Task, TaskTag, Board

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', "name", 'type']
