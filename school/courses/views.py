# STANDARD IMPORTS
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
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


"""API VERSION 2"""


# all of this code below replaces the code above
# the view set will implement the GET, POST, DELETE, PATCH
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=["get"])
    def ratings(self, request, pk=None):
        course = self.get_object()
        serializer = RatingSerializer(course.ratings.all(), many=True)
        return Response(serializer.data)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
