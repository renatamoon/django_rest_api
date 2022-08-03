# STANDARD IMPORTS
from django.contrib import admin

# PROJECT IMPORTS
from .models import Course, Rating


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'url',
        'creation_date',
        'update_date',
        'active'
    )


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'course',
        'name',
        'email',
        'rating',
        'creation_date',
        'update_date',
        'active'
    )
