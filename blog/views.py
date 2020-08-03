from django.shortcuts import render,redirect
from .models import *
import markdown
from django.contrib import messages
from django.db.models import Q
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
import re

# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request,'index.html',locals())

# 文章详情页
def detail(request,pk):
    post = Post.objects.get(pk=pk)
    post.increase_views() #阅读量+1
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.sane_lists',
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)
    
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    return render(request,'detail.html',locals())


# 文章分类
def category(request,pk):
    category = Category.objects.get(pk=pk)
    post_list = Post.objects.filter(category=category)
    return render(request,'index.html',locals())

# 文章标签
def tag(request,pk):
    tags = Tag.objects.get(pk=pk)
    post_list = Post.objects.filter(tags=tags)
    return render(request,'index.html',locals()) 

# 文章归档
def archive(request, year, month):
    post_list = Post.objects.filter(create_time__year=year,create_time__month=month).order_by('-create_time')
    return render(request,'index.html',locals())

# 关于
def about(request):
    return render(request,'about.html',locals())

# 搜索功能
def search(request):
    q = request.GET.get('q')
    if not q:
        error_msg = '请输入搜索关键词'
        messages.add_message(request,messages.ERROR,error_msg,extra_tags='danger')
        return redirect('index')
    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request,'index.html',locals())