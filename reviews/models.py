from django.db import models
from products.models import Product
from profiles.models import UserProfile


class Reviews(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    subject = models.Charfield(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.IntegerField()
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
