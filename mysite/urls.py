
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic.base import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

from article import views
# from article.views import RSSFeed
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    # url(r'^index/$',TemplateView.as_view(template_name ='test2.html')),
    url(r'^', include('article.urls')),
    url(r'^hostadmin/', admin.site.urls),
    url('^schema/$', schema_view),
]


# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls')),
# ]
