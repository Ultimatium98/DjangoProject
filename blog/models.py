from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User
from blog.utils import sendTransaction
import hashlib


class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    hash = models.CharField(max_length=32, default=None, null=True)
    txId = models.CharField(max_length=66, default=None, null=True)

    def writeOnChain(self):
        self.hash = hashlib.sha256(self.content.encode('utf-8')).hexdigest()
        self.txId = sendTransaction(self.hash)
        self.save()

    def __str__(self):
        return self.title


def post_list(request):
    posts = Post.objects.filter().order_by('-datetime')
    return render(request, 'blog/home.html', {'posts': posts})