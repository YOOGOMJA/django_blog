from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers

# Create your views here.

def home(req): 
    all_of_posts = Post.objects.all().order_by('-pub_date')

    # pagination
    paginator = Paginator(all_of_posts,5)
    page = req.GET.get('page')    
    posts = paginator.get_page(page)

    # hottest posts
    all_of_posts_with_views = Post.objects.all().order_by('-views' , '-pub_date')[:3]
    
    return render(req , './home.html' , { 'posts' : posts , 'hottest_posts' : all_of_posts_with_views })

def detail(req , post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.views += 1
    post.save()
    comments_list = Comment.objects.filter(post = post_id).order_by('-date')
    return render(req, 'detail.html', {'post':post, 'comments':comments_list})


# API
@csrf_exempt
def get_comment(req , post_id):
    post = get_object_or_404(Post , pk=post_id)
    comments_list = Comment.objects.filter(post = post_id).order_by('-date')
    return JsonResponse({
        'code' : 1 ,
        'message' : 'success',
        'data' : {
            'comments' : serializers.serialize('json' , comments_list)
        }
    }, json_dumps_params = {'ensure_ascii': True})

@csrf_exempt
def comment_create(req , post_id):
    comment = Comment()
    comment.writer = req.POST['writer']
    comment.content = req.POST['content']
    comment.post = get_object_or_404(Post , pk=post_id)
    comment.save()
    return JsonResponse({
        'code' : 1 ,
        'message' : 'success',
    }, json_dumps_params = {'ensure_ascii': True})

def comment_update(req , comment_id):
    return JsonResponse({
        'message' : 'success',
    }, json_dumps_params = {'ensure_ascii': True})

def comment_delete(req , comment_id):
    return JsonResponse({
        'message' : 'success',
    }, json_dumps_params = {'ensure_ascii': True})