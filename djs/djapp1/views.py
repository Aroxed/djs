from django.shortcuts import render


def index(request):
    return render(request, 'djapp1_index.html', {})
