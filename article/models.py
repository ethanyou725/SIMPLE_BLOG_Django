from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Article(models.Model):
    '''
    article model
    '''
    title = models.CharField(max_length=100)  # 题目
    category = models.CharField(max_length=50)  # 标签
    date_time = models.DateTimeField(auto_now_add=True)  # 日期
    content = models.TextField()  # 内容
    # author = models.ForeignKey('auth.User',related_name='articles',on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # path=reverse('single', kwargs={'id':self.id})
        return '/article/%i/' % self.id

    class Meta:  # 按id降序
        '''order by id'''
        ordering = ['id']


