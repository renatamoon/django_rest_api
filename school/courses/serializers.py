# STANDARD IMPORTS
from rest_framework import serializers

# PROJECT IMPORTS
from .models import Course, Rating


class RatingSerializer(serializers.ModelSerializer):
    # create extra class configs
    class Meta:
        extra_kwargs = {
            # this field here sets that the email won't be showed when you see the api, only when an user registrate
            'email': {
                'write_only': True
            }
        }

        model = Rating

        # fields you want to show when the user access the api - all of this are existing fields of the main model
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'creation_date',
            'active'
        )


class CourseSerializer(serializers.ModelSerializer):

    class Meta:

        model = Course

        fields = (
            'id',
            'title',
            'url',
            'creation_date',
            'active'
        )

# email and password is a sensitive field, then you can hide it to be shown.
