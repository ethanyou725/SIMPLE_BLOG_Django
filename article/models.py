from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)  # 题目
    category = models.CharField(max_length=50)  # 标签
    date_time = models.DateTimeField(auto_now_add=True)  # 日期
    content = models.TextField()  # 内容

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        path=reverse('d',kwargs={'id':self.id})
        return '127.0.0.1:8000%s' % path

    class Meta:  # 按id降序
        ordering = ['id']


# class Author(models.Model):
#     name = models.CharField(max_length=50)
#     age = models.IntegerField()
#
#     def __str__(self):
#         return self.name
#
#
# class Blog(models.Model):
#     title = models.CharField(max_length=50)
#     content = models.TextField
#     counter = models.IntegerField(default=0)  # 访问数量
#     pubDate = models.DateField(auto_now_add=True)
#     author = models.ForeignKey(Author)
#
#     def __str__(self):
#         return self.title
