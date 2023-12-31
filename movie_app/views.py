from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.serializers import DirectorSerializer,MovieSerializer,ReviewSerializer, ReviewValidateSerializer
from movie_app.models import Director, Movie, Review
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
#
# @api_view(['GET', 'POST'])
# def director_list(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         data = DirectorSerializer(directors,many=True)
#         return Response(data.data)
#     elif request.method == 'POST':
#         serializer = DirectorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def get_director(request, id):
#     director = get_object_or_404(Director, id=id)
#     if request.method == 'GET':
#         serializer = DirectorSerializer(director)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = DirectorSerializer(director, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=200)
#
#
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         data = MovieSerializer(movies, many=True)
#         return Response(data.data)
#     elif request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

class DirectorListApiView(generics.CreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'

class MovieListApiView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'


class ReviewListApiView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'






#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def get_movie(request, id):
#     movie = get_object_or_404(Movie, id=id)
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=200)
#
#
# @api_view(['GET', 'POST'])
# def review_list(request):
#     if request.method == 'GET':
#         review = Review.objects.all()
#         data = ReviewSerializer(review, many=True)
#         return Response(data.data)
#     elif request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def get_review(request, id):
#     review = get_object_or_404(Review, id=id)
#     if request.method == 'GET':
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ReviewSerializer(review, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=200)
#

class MoviesReviewAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination

