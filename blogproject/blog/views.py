import markdown
from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, request
from comments.forms import CommentForm
from blog.models import Post,Category

#首页
def index(request):
    post_list = Post.objects.all()
    return render(request,'blog/index.html',context={'post_list':post_list})

#文章详情页
def detail(request,pk):
    try:
        post = Post.objects.get(id=pk)
    except:
        return render(request,'blog/detail.html',status=404)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form  = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post':post,
        'form':form,
        'comment_list': comment_list
    }
    return render(request,'blog/detail.html',context=context)

#归档
def archives(request,year,month):
    post_list = Post.objects.filter(Q(created_time__year=year) & Q(created_time__month=month))
    return render(request,'blog/index.html',context={'post_list':post_list})

def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request,'blog/index.html',context={'post_list':post_list})


