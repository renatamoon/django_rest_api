# STANDARD IMPORTS
from rest_framework import generics, viewsets, mixins, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

# PROJECT IMPORTS
from .models import Course, Rating
from .serializers import CourseSerializer, RatingSerializer
from .permissions import IsSuperUser


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
    permission_classes = (
        IsSuperUser,  # if this class solves the problem of permission,
        # it won't use the second class (DjangoModelPermissions)
        permissions.DjangoModelPermissions,  # if the permission was not solved as above, then it wil use this one
    )
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=["get"])
    def ratings(self, request, pk=None):
        self.pagination_class.page_size = 1  # one per page
        ratings = Rating.objects.filter(course_id=pk)
        page = self.paginate_queryset(ratings)

        # if the pagination exists, then the page is sent to serializer, if not, it shows everything
        if page is not None:
            serializer = RatingSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # course = self.get_object()
        serializer = RatingSerializer(ratings.all(), many=True)
        return Response(serializer.data)


"""
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    """


# this rating view set is the same thing as Rating View Set above. If you don't want to list or update something, just
# do not instantiate below
class RatingViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
