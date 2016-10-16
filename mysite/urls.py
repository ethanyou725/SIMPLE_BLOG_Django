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
    # url(r'^article/page(?P<a>\d+)/', views.g),
    url(r'^$', views.IndexView.as_view(), name='home'),
    # url(r'^post(?P<id>\d+)/$', views.detail, name='d'),
    url(r'^post/(?P<id>\d+)/$', views.SingleView.as_view(), name='single'),
    url(r'archive/$',views.ArchiveView.as_view(), name='archive'),
    # url(r'aboutme/$',views.about_me, name='about_me'),
    url(r'aboutme/$',views.AboutMeView.as_view(), name='about_me'),
    # url(r'category/(?P<category>.+)/$', views.category, name='category'),
    # url(r'search/$', views.search, name='search'),
    url(r'search/$',views.SearchView.as_view(),name='search'),
    url(r'^feed/$', RSSFeed(), name="RSS"),
    url(r'test/$',views.AboutView.as_view()),
    url(r'category/(\w+)/$', views.CateView.as_view(), name='category'),
    # url(r'date/(\w+)/$', views.DateView.as_view(), name='title'),
]
