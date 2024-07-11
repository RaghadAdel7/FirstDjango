from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import User, Post, Comment, Category


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def blogs(request):
    blog_posts = Post.objects.all()
    context = {'blog_posts': blog_posts}
    return render(request, 'blogs.html', context)

def blogdetails(request, post_id, date_published=None):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post_id=post_id)
    context = {'post': post, 'comments': comments}
    category = post.category
    date_published: post.date_published
    return render(request, 'blogdetails.html', context)

def comments(request):
    all_comments = Comment.objects.all()
    context = {'all_comments': all_comments}
    return render(request, 'comments.html', context)

def categories(request):
    categories_list = Category.objects.all()
    context = {'categories_list': categories_list}
    return render(request, 'categories.html', context)
