from django.shortcuts import render

from blog.models import Post


def index(request):
    title = 'DevInCafe Sample | Blog'

    post_list = Post.objects.all()

    context = {
        'WEB_TITLE' : title,
        'post_list' : post_list,
    }
    return render(request, 'blog/pages/index.html', context)