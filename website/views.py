from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from .models import Post
from .forms import CommentForm

def index(request):
    posts = Post.objects.all()

    return render(request, 'website/frontpage.html', {'posts': posts})

def post_details(request,slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_details', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'website/post_detail.html', {'post': post, 'form': form})