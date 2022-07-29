# STANDARD IMPORTS
from rest_framework import generics

# PROJECT IMPORTS
from .models import Course, Rating
from .serializers import CourseSerializer, RatingSerializer


# GET METHOD
class CoursesAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# class RatingAPIView(generics.ListCreateAPIView):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer


# RetrieveUpdateDestroyAPIView - this method does GET, UPDATE, POST AND DELETE
class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RatingsAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class RatingAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
