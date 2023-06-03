# serializers.py
from rest_framework.serializers import ModelSerializer
from base.models import Tag, Task

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TaskSerializer(ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

