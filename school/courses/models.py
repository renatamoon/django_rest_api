# STANDARD IMPORTS
from django.db import models


class Base(models.Model):
    creation_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title


class Rating(Base):
    course = models.ForeignKey(Course, related_name='ratings', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    rating = models.DecimalField(max_digits=2, decimal_places=1)  # allowing rates to be 4.8

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        unique_together = ['email', 'course']  # each person who rated the course can only rate the course once

    def __str(self):
        return f'{self.name} rated the course {self.course} with the final rating of {self.rating}'
