
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic.base import TemplateView
from rest_framework.schemas import get_schema_view

from article.views import RSSFeed


urlpatterns = [
    # url(r'^index/$',TemplateView.as_view(template_name ='test2.html')),
    url(r'^', include('article.urls')),
    url(r'^react/', TemplateView.as_view(template_name ='react.html')),
    url(r'^schema/$', get_schema_view(title='Pastebin API')),
    url(r'^feed/$', RSSFeed(), name = "RSS"),
    url(r'^hostadmin/', admin.site.urls),
    url(r'^', TemplateView.as_view(template_name ='index.html')),
    
]


# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls')),
# ]
