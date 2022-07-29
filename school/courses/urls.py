# STANDARD IMPORTS
from django.urls import path

# PROJECT IMPORTS
from .views import (
    CourseAPIView,
    CoursesAPIView,
    RatingAPIView,
    RatingsAPIView
)


# url patterns is used to say that the route will use a view:
urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>', CourseAPIView.as_view(), name='course'),
    path('courses/<int:course_pk>/ratings', RatingsAPIView.as_view(), name='course_ratings'),
    path('courses/<int:course_pk>/ratings/<int:rating_pk>', RatingAPIView.as_view(), name='course_rating'),

    path('ratings/', RatingAPIView.as_view(), name='ratings'),
    path('ratings/<int:rating_pk>', RatingAPIView.as_view(), name='rating')
]
