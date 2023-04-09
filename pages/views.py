from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def login_success(request):
    if request.user.is_approved is True:
        # TODO: This needs to be replaced with a redirect to the user dashboard once created
        return redirect('pages:home')
    else:
        return redirect('pages:home')


def homepage_view(request):
    return render(request, 'pages/home.html', {})
