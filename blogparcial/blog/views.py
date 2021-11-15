from django.shortcuts import render

from .models import Post
# Create your views here.
def frontpage(request):
    posts = Post.objects.all()

    return render(request, 'blog/frontpage.html', {'posts': posts})

def detalle(request, slug):
    post= Post.objects.get(slug=slug)

    return render(request, 'blog/detalle.html',  {'post': post})