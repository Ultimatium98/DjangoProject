from blog import models
from django.http import JsonResponse
from django.db.models import Q
from django.utils import timezone


#Return a JSON with all posts published
def posts(request):
    response = []
    posts = models.Post.objects.filter().order_by('-datetime')
    for post in posts:
        response.append({
            'datetime': post.datetime,
            'title': post.title,
            'content': post.content,
            'author': f"{post.user.first_name} {post.user.last_name}",
            'Hash': post.hash,
            'TxId': post.txId,
        })
    return JsonResponse(response, safe=False)

#Return a JSON with a list of posts published in the last hour
def recent_posts(request):
    now=timezone.now()
    response = []
    posts = models.Post.objects.filter(datetime__gt = now.replace(hour=now.hour-1)).order_by('-datetime')
    for post in posts:
        response.append({
            'datetime': post.datetime,
            'title': post.title,
            'content': post.content,
            'author': f"{post.user.first_name} {post.user.last_name} ({post.user.username})",
            'Hash': post.hash,
            'TxId': post.txId,
        })
    return JsonResponse(response, safe=False)

#This function counts how many times the word [string] appears in all posts
def count_str(request, string):
    sum = 0
    posts = models.Post.objects.filter(Q(title__contains=string) | Q(content__contains=string))
    for post in posts:
        sum += post.content.lower().count(string)
        sum+= post.title.lower().count(string)
    return JsonResponse({f'recurrences': sum}, safe=False)
