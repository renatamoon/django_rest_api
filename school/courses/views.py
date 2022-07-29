# STANDARD IMPORTS
from rest_framework import generics
from rest_framework.generics import get_object_or_404

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

    def get_queryset(self):
        # get all the ratings filtered by a course, if not, only all ratings.
        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
        return self.queryset.all


class RatingAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_object(self):
        if self.kwargs.get('course_pk'):
            response = get_object_or_404(
                self.get_queryset(),
                course_id=self.kwargs.get('course_id'),
                pk=self.kwargs.get('ratings_pk'))
            return response

        response = get_object_or_404(
            # this function will get the object or it will raise an error
            self.get_queryset(),
            pk=self.kwargs.get('ratings_pk')
        )
        return response
