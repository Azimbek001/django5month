"""
URL configuration for Afisha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.DirectorListApiView.as_view()),
    path('api/v1/directors/<int:id>/', views.DirectorDetailApiView.as_view()),
    path('api/v1/movies/', views.MovieListApiView.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieDetailApiView.as_view()),
    path('api/v1/reviews/', views.ReviewListApiView.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewDetailApiView.as_view()),
    path('api/v1/movies/reviews/', views.MoviesReviewAPIView.as_view()),
    path('api/v1/users/', include('users.urls'))
]
