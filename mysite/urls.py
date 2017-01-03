
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic.base import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

from article import views
# from article.views import RSSFeed

# urlpatterns = [
#     url(r'^hostadmin/', admin.site.urls),
#     # url(r'^article/page(?P<a>\d+)/', views.g),
#     # url(r'^post(?P<id>\d+)/$', views.detail, name='d'),
#     # url(r'aboutme/$',views.about_me, name='about_me'),
#     # url(r'category/(?P<category>.+)/$', views.category, name='category'),
#     # url(r'search/$', views.search, name='search'),
#     # url(r'date/(\w+)/$', views.DateView.as_view(), name='title'),
#     url(r'^$', views.IndexView.as_view(), name='home'),
#     url(r'^post/(?P<id>\d+)/(?P<f>.+)/$', views.SingleView.as_view(), name='single'),
#     url(r'archive/$',views.ArchiveView.as_view(), name='archive'),
#     url(r'aboutme/$',views.AboutMeView.as_view(), name='about_me'),
#     url(r'search/$',views.SearchView.as_view(),name='search'),
#     url(r'^feed/$', RSSFeed(), name="RSS"),
#     url(r'test/$',views.AboutView.as_view()),
#     url(r'category/(\w+)/$', views.CateView.as_view(), name='category'),
#     url(r'ajax/$', views.ajax, name='ajax'),
# ]
urlpatterns = [
    url(r'^hostadmin/', admin.site.urls),
    url(r'^index/$',TemplateView.as_view(template_name ='test2.html')),
    url(r'^', include('article.urls')),

]

urlpatterns = format_suffix_patterns(urlpatterns)
