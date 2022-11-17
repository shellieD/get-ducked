from django.shortcuts import render, redirect, reverse
from .forms import ReviewForm
from django.contrib import messages

from .models import Review
from .forms import ReviewForm


def review(request):
    """ A view to return the reviews page """

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        title = request.POST['title']
        review = request.POST['review']
        rating = request.POST['rating']

        if form.is_valid():
            cust_review = form.save()
            messages.success(request, 'Thank you for your feedback. \
                  Your review has been submitted.')
            return redirect(reverse('reviews'))
        else:
            messages.error(
                request,
                'Oops, something went wrong. \
                    Please check your form is valid.'
            )
    else:
        form = ReviewForm()

    template = 'reviews/reviews.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
