from django.shortcuts import render


def index(request):
    return render(request, 'djapp2_index.html', {})
