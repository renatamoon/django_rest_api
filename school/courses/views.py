# STANDARD IMPORTS
from rest_framework import generics

# PROJECT IMPORTS
from .models import Course, Rating
from .serializers import CourseSerializer, RatingSerializer


class CourseAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RatingAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
