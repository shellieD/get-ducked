from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.all_reviews,
        name='all_reviews'
    ),
    path(
        'add_review/',
        views.AddReview.as_view(),
        name='add_review'
    ),
    path(
        'moderate_reviews/',
        views.ModerateReviews.as_view(),
        name='moderate_reviews'
    ),
    path(
        'reviews/<slug:slug>/approve_reviews',
        views.ModerateApproveReview.as_view(),
        name='approve_reviews'
    ),
    path(
        'reviews/<slug:slug>/admin_delete_review/',
        views.ModerateDeleteReview.as_view(),
        name='moderate_delete_review'
    ),
    path(
        'reviews/admin_update_review/<slug:slug>',
        views.ModerateUpdateReview.as_view(),
        name='moderate_update_review'
    ),
]
