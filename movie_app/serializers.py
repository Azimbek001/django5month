from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.serializers import *
from movie_app.models import *


class DirectorSerializer(ModelSerializer):
    class Meta:
        model = Director
        fields = ["id", "name", "movie_count"]


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "director", "rating"]


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewValidateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(max_value=100)
    text = serializers.CharField(max_length=220)
    stars = serializers.IntegerField(min_value=1, max_value=5)
