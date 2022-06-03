from django.shortcuts import render
from blog.models import Post


# Create your views here.
def landing(request):
    if Post.objects.count() >= 3:
        return render(request, 'single_pages/landing.html', {
            'recent_post': Post.objects.order_by('-pk')[:3],
        })
    else:
        return render(request, 'single_pages/landing.html', {
            'recent_post': Post.objects.order_by('-pk')[:Post.objects.count()],
        })


def about_me(request):
    return render(request, 'single_pages/about_me.html')
