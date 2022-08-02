# STANDARD IMPORTS
from rest_framework import serializers
from django.db.models import Avg

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
            'rating',
            'creation_date',
            'active'
        )

        def validate_rating(self, value):  # a pattern of the serializer model is that you need to put
            # [validate_ + field you wanna validate]
            if value in range(1, 6):
                return value
            raise serializers.ValidationError('The rating needs to be an integer between 1 and 5')


class CourseSerializer(serializers.ModelSerializer):
    # NESTED RELATIONSHIP
    # many=True - means that a course can have many ratings,
    # and read_only=True this data is only to read - allowed to method GET
    # ratings = RatingSerializer(many=True, read_only=True)

    # HYPER LINKED RELATED FIELD
    """ratings = serializers.HyperlinkedIdentityField(
        many=True,
        read_only=True,
        view_name='rating-detail'
        # serializer - through the views we do access to the routers
        # and we need to set the view_name like this, once it's to see the detail
        # this hyperlink it's seen when you open the router get ... besides seeing all the ratings, it's
        # shown a hyperlink that you redirect to a page with all the ratings
    ) """

    # PRIMARY KEY RELATED FIELD
    """using PrimaryKeyRelatedField it will generate an link but only with the primary key (id) of the rating"""
    ratings = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    average_ratings = serializers.SerializerMethodField()

    class Meta:
        model = Course

        fields = (
            'id',
            'title',
            'url',
            'creation_date',
            'active',
            'ratings',
            'average_ratings'
        )

        def get_average_ratings(self, obj):
            average = obj.ratings.aggregate(Avg('ratings')).get('rating__avg')

            if average is None:
                return 0
            return round(average * 2) / 2

# email and password is a sensitive field, then you can hide it to be shown.
