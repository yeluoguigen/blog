from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Post
from .forms import CommentForm

def post_comment(request,post_pk):
    post = get_object_or_404(Post,pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            #实例化
            comment = form.save(commit=False)
            #把两个表关联起来
            comment.post = post
            #保存在数据库
            comment.save()
            #返回到文章详情页
            return redirect(post)
        else:
            #数据不合法，重新渲染详情页
            comment_list = post.comment_set.all()
            context = {
                'post':post,
                'form':form,
                'comment_list':comment_list
            }
            return render(request,'blog/detail.html',context=context)
    else:
        #没有表单数据，重定向到文章详情页
        return redirect(post)
