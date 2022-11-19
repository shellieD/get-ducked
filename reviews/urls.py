from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_reviews, name='all_reviews'),
    path('', views.AddReview.as_view(), name='add_review'),
]
