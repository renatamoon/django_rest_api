# STANDARD IMPORTS
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# PROJECT IMPORTS
from .models import Course, Rating
from .serializers import CourseSerializer, RatingSerializer


class CourseAPIView(APIView):
    """
    Course API from RM
    """
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RatingAPIView(APIView):
    """
    Rating API from RM
    """
    def get(self, request):
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
