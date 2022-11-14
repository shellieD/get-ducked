from django.shortcuts import render


def custom_403_error(request, exception):
    """ 403 error view """
    data = {}
    return render(request, 'errors/403.html', data)


def custom_404_error(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def custom_500_error(request, exception):
    """ 500 error view """
    data = {}
    return render(request, 'errors/500.html', data)