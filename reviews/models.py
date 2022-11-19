from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from profiles.models import UserProfile
from django.core.validators import MaxValueValidator, MinValueValidator

STATUS = ((0, "Draft"), (1, "Added"))


class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    title = models.CharField(
        default='Title',
        max_length=100,
        blank=True,
        null=False
    )
    review = models.TextField(
        default='Write your review here',
        max_length=500,
        blank=True,
        null=False
    )
    rating = models.IntegerField(
        default=3,
        validators=[MaxValueValidator(5), MinValueValidator(1)],
        null=False
    )
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
