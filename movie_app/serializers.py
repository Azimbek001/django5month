
from .models import Director, Movie, Review
from rest_framework.serializers import *


class DirectorSerializer(ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'