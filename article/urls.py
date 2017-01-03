from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^articles/$',views.article_list),
    url(r'^articles/(?P<id>[0-9]+)/$',views.article_detail)
]