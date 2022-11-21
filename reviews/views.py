from django.shortcuts import render, redirect, reverse
from .forms import ReviewForm
from django.contrib import messages
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Review
from .forms import ReviewForm, ApproveForm


def all_reviews(request):
    """View to show a list reviews posted by all users"""
    reviews = Review.objects.filter(status=1)
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/all_reviews.html', context)


class AddReview(View):
    """ A view to add a review """

    def get(self, request):
        template = 'reviews/add_review.html'
        context = {'form': ReviewForm()}
        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        title = form.instance.title

        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
            messages.success(request, "Thank you for your feedback. \
                Your review has been submitted.")
            return redirect('home')
        else:
            messages.error(request,
                           'Error: The form is not valid, '
                           'please check and try again')
            context = {'form': form}
            return render(request, template, context)


class ModerateDeleteReview(DeleteView):
    """View to delete review"""
    model = Review
    template_name = 'reviews/delete_review.html'
    success_url = reverse_lazy('moderate_reviews')


class ModerateApproveReview(UpdateView):
    """View to toggle status of reviews from draft to approved"""
    model = Review
    template_name = 'reviews/approve_review.html'
    form_class = ApproveForm
    success_url = reverse_lazy('moderate_reviews')


class ModerateReviews(generic.ListView):
    """View to display draft reviews awaiting approval by admin"""
    template_name = 'reviews/moderate_reviews.html'
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        return Review.objects.filter(
            status=0
        ).order_by('-date_created')


class ModerateUpdateReview(UpdateView):
    """View to update a review"""
    model = Review
    template_name = 'reviews/update_review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('moderate_reviews')
