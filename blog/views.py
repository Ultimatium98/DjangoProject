from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import *
from django.contrib.auth.models import User

word = 'hack'
string = f"Can't publish a Post that contains the word {word}"


# Clicking on a post will render to a page that contains information about that post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def newPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            if word in post.title.lower() or word in post.content.lower():
                return render(request, 'blog/post_new.html', {'error': string})
            post.save()
            post.writeOnChain()
            return redirect('post_detail', pk=post.pk)
    else:
        posts = Post.objects.filter().order_by('-datetime')
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form, 'posts': posts})


# This funciotn returns the number of posts that each User has published
def analytics(request):
    list = []
    for user in User.objects.all():
        count = Post.objects.filter(user=user.id).count()
        list.append({'user': user.username, 'posts': count})
    return render(request, 'blog/user_analytics.html', {'list': list})


# This function return some informations about users
def user_detail(request, id):
    user = get_object_or_404(User, id=id)
    posts = Post.objects.filter(user=id)
    count = posts.count()
    return render(request, 'blog/user_detail.html', {'user': user, 'posts': posts, 'count': count})


def get_ip_address(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    except:
        ip = ''
    return ip


# this functions check if ip address has changed and return a message and the list of all posts
# published
def home(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter().order_by('-datetime')
        old_ip = request.user.userprofile.ip
        ip = get_ip_address(request)
        user = User.objects.get(username=request.user)
        if ip == old_ip:
            status = 'ok'
        else:
            status = 'different'
            user.userprofile.ip = ip
            user.userprofile.save()
    else:
        status = ''
    return render(request, 'blog/home.html', {'status': status, 'posts': posts})
# Create your views here.
