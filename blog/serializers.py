# posts/serializers.py
from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'content', 'created_at', 'updated_at',)
        model = models.Post