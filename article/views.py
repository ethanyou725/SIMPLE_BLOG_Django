from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

# test
def hello(request):
    return HttpResponse("<h1>Hello Django</h1>")


# def detail(request, my_args):
#     post = Article.objects.all()[int(my_args)]
#     str = "title = %s, category=%s, datetime=%s, content=%s." \
#           % (post.title, post.category, post.date_time, post.content)
#     return HttpResponse(str)
# test


def g(request, a):
    return HttpResponse("article pages %s." % a)


# test
def test(request):
    context = {'current_time': datetime.now()}
    return render(request, 'test.html', context)


def home(request):
    posts = Article.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        post_list=paginator.page(page)
    except PageNotAnInteger :
        post_list=paginator.page(1)# If page is not an integer, deliver first page.
    except  EmptyPage :
        post_list = paginator.paginator(paginator.num_pages) # If page is out of range (e.g. 9999), deliver last page of results.
    return render(request, 'index.html', {'post_list': post_list})


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
        count = Article.objects.all().count()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post, 'count': count})


def archive(request):
    try:
        archive_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archive.html', {"archive_list": archive_list})


def about_me(request):
    return render(request, 'about_me.html')


def tag(request, category):
    try:
        post_list = Article.objects.filter(category__iexact=category)
    except:
        raise Http404
    return render(request, 'category.html', {'post_list': post_list})


def search(request):
    keywords = request.GET.get("keywords")
    # qs=Article.objects.get(id='0')
    # l= keywords.split(" ")
    # for item in l:
    #     # if item is 'and' or item is 'not' or item is 'or':
    #     list.remove(item)
    #     qs=qs|Article.objects.get(Q(content__icontains=item))
    if keywords is "":
        return HttpResponseRedirect("/")
    else:
        post_list = Article.objects.filter(content__icontains=keywords.lower())
        if len(post_list) == 0:
            return render(request, 'index.html', {'post_list': post_list, 'none': True})
        else:
            return render(request, 'index.html', {'post_list': post_list, 'none': False})
        # return render(request, 'result.html', {'post_list': post_list})




'''Rss'''
from django.contrib.syndication.views import Feed

class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content
