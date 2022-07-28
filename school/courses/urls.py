# STANDARD IMPORTS
from django.urls import path

# PROJECT IMPORTS
from .views import CourseAPIView, RatingAPIView


# url patterns is used to say that the route will use a view:
urlpatterns = [
    path('courses/', CourseAPIView.as_view(), name='courses'),
    path('ratings/', RatingAPIView.as_view(), name='ratings')
]
