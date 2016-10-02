"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from article import views
from article.views import RSSFeed

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$',views.hello),
    # url(r'^(?P<my_args>\d+)/$',views.detail),
    #^(?P<my_args>\d+)/$  (?P<num>[0-9]+)

    url(r'^article/page(?P<a>\d+)/', views.g),
    url(r'^test/$', views.test),
    url(r'^$',views.home, name='home'),
    url(r'^post(?P<id>\d+)/$', views.detail, name='d'),
    url(r'archive/$',views.archive, name='archive'),
    url(r'aboutme/$',views.about_me, name='about_me'),
    url(r'category/(?P<category>.+)/$', views.tag, name='category'),
    url(r'search/$', views.search, name='search'),
    url(r'^feed/$', RSSFeed(), name="RSS"),
]
