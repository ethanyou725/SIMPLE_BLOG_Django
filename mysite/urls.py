
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic.base import TemplateView

# from article.views import RSSFeed

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    # url(r'^index/$',TemplateView.as_view(template_name ='test2.html')),
    url(r'^', include('article.urls')),
    url(r'^react/', TemplateView.as_view(template_name ='react.html')),
    url(r'^', TemplateView.as_view(template_name ='index.html')),
    url(r'^hostadmin/', admin.site.urls),
    url('^schema/$', schema_view),
]


# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls')),
# ]
