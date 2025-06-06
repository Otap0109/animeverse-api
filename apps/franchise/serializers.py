from rest_framework import serializers
from .models import Franchise

class FranchiseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Franchise
        fields = [
            'id',
            'title',
            'slug',
            'image',
            'release_date',
            'rating',
            'genre',
        ]


class FranchiseSerializer(serializers.ModelSerializer):
    chars = serializers.StringRelatedField(many=True, source='characters')

    class Meta:
        model = Franchise
        fields = [
            'id',
            'title',
            'slug',
            'image',
            'description',
            'release_date',
            'rating',
            'genre',
            'chars',
        ]