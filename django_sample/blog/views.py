from django.shortcuts import render


def index(request):
    title = 'DevInCafe Sample | Blog'
    context = {
        'WEB_TITLE' : title
    }
    return render(request, 'blog/pages/index.html', context)