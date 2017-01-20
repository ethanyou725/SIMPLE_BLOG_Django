from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     url(r'^articles/$',views.ArticleList.as_view()),
#     url(r'^articles/(?P<pk>[0-9]+)/$',views.ArticleDetail.as_view()),
#     # url(r'^users/$', views.UserList.as_view()),
#     # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

# ]


article_list = views.ArticleListViewSet.as_view({
    'get':"list"
})
article_detail = views.ArticleDetailViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    # 'patch': 'partial_update',
    # 'delete': 'destroy'
})

router = DefaultRouter()
router.register(r'articles', views.ArticleDetailViewSet)


urlpatterns = [
    url(r'^articles/$',article_list,name = 'articles'),
    url(r'^articles/(?P<pk>[0-9]+)/$',article_detail,name='detail'),
    # url(r'^users/$', views.UserList.as_view()),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    #  url(r'^', include(router.urls)),
]


urlpatterns = format_suffix_patterns(urlpatterns)