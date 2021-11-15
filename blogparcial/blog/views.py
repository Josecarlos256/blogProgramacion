#from typing_extensions import Required
from django import forms
from django.shortcuts import redirect, render

from .forms import CommentForm
from .models import Post
# Create your views here.
def frontpage(request):
    posts = Post.objects.all()

    return render(request, 'blog/frontpage.html', {'posts': posts})

def detalle(request, slug):
    post= Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('detalle', slug=post.slug)
    
    else:
        form = CommentForm()

    return render(request, 'blog/detalle.html',  {'post': post, 'form':form})