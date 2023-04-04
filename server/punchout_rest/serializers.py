from rest_framework import serializers
from .models import Tag, Category, Task, TaskTag, Board

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', "name", 'type']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', "name", 'colour', 'boardId']
