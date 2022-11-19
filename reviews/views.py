from django.shortcuts import render, redirect, reverse
from .forms import ReviewForm
from django.contrib import messages
from django.views import generic, View

from .models import Review
from .forms import ReviewForm


def all_reviews(request):
    """View to show a list reviews posted by all users"""
    reviews = Review.objects.all()
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
