from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('id', 'title', 'content', 'user', 'created_at', 'updated_at', )