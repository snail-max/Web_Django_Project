from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# def index(request):
#     return render(request,'blog/index.html',context={
#         'title':'傻鸟的博客',
#         'welcome':'欢迎来到博客园首页'
#     })
#     return HttpResponse('欢迎访问我的博客首页')

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})
