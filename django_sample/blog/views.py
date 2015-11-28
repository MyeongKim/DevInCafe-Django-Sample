from django.shortcuts import render, redirect

from blog.forms import PostForm
from blog.models import Post


def index(request):
    title = 'DevInCafe | Blog'

    post_list = Post.objects.filter(removed=False)

    context = {
        'WEB_TITLE': title,
        'e_post_list': enumerate(post_list),
    }
    return render(request, 'blog/pages/index.html', context)


def post_create(request):
    title = 'DevInCafe | NEW'
    context = {
        'WEB_TITLE': title,
    }

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')

    else:
        form = PostForm()

    context.update({'form': form})

    return render(request, 'blog/pages/add_post.html', context)