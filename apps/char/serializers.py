from rest_framework import serializers
from .models import Character

class CharacterListSerializer(serializers.ModelSerializer):
    class Meta:

        model = Character
        fields = [
          'id',
          'name',
          'slug',
          'image',
          'age',
          'anime',
        ]


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:

        model = Character
        fields = [
          'id',
          'name',
          'slug',
          'description',
          'image',
          'role',
          'age',
          'anime',
        ]
