from django.contrib.auth.models import User
from django.db import models
#分类
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    #标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
#文章
class Post(models.Model):
    #标题
    title = models.CharField(max_length=70)
    #正文
    body = models.TextField()
    #创建时间
    created_time = models.DateTimeField()
    #最后一次更新时间
    modified_time = models.DateTimeField()
    #摘要
    excerpt = models.CharField(max_length=200,blank=True)
    #分类
    category = models.ForeignKey(Category)
    #标签
    tags = models.ManyToManyField(Tag,blank=True)
    #作者
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']


