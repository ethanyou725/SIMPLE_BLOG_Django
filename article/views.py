from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from article.models import Article
from django.views.generic import ListView
from django.views.generic import View
from django.views.generic import FormView
from django.views.generic.edit import FormMixin
# Create your views here.

# test
def hello(request):
    return HttpResponse("<h1>Hello Django</h1>")


# def g(request, a):
#     return HttpResponse("article pages %s." % a)


# test
# def test(request):
#     context = {'current_time': datetime.now()}
#     return render(request, 'test.html', context)


# def home(request):
#     posts = Article.objects.all()
#     paginator = Paginator(posts, 2)
#     page = request.GET.get('page')
#     try:
#         post_list=paginator.page(page)
#     except PageNotAnInteger :
#         post_list=paginator.page(1)# If page is not an integer, deliver first page.
#     except  EmptyPage :
#         post_list = paginator.paginator(paginator.num_pages) # If page is out of range (e.g. 9999), deliver last page of results.
#     return render(request, 'index.html', {'post_list': post_list})


# def show_list(req):
#     title_list=Article.objects.values("title")[0:5]
#     category_list = Article.objects.values("category")
#     return render(req, 'sidebar.html',{'title_list': title_list, 'category_list': category_list})


# def detail(request, id):
#     item_list= Article.objects.values('category', 'date_time')
#     try:
#         post = Article.objects.get(id=str(id))
#         count = Article.objects.all().count()
#
#     except Article.DoesNotExist:
#         raise Http404
#     return render(request, 'single.html', {'post': post, 'count': count,'item_list':item_list})


# def archive(request):
#     try:
#         archive_list = Article.objects.all()
#     except Article.DoesNotExist:
#         raise Http404
#     return render(request, 'archive.html', {"archive_list": archive_list})


# def about_me(request):
#     return render(request, 'about_me.html')


# def category(request, category): #根据category查找
#     try:
#         post_list = Article.objects.filter(category__iexact=category)
#     except:
#         raise Http404
#     return render(request, 'index.html', {'post_list': post_list})


# def time(request, time): #根据date_time查找
#     try:
#         post_list = Article.objects.filter(date_time__iexact=time)
#     except:
#         raise Http404
#     return render(request, 'index.html', {'post_list': post_list})
#
#
# def tag(request, category):
#     try:
#         post_list = Article.objects.filter(category__iexact=category)
#     except:
#         raise Http404
#     return render(request, 'category.html', {'post_list': post_list})
#
#

class AboutView(View):
    template_name = "test.html"


class BaseView(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['item_list'] = Article.objects.values('category', 'date_time')
        return context


def search(request):
    item_list = Article.objects.values('category', 'date_time')
    keywords = request.GET.get("q")
    if keywords.strip() == "":
        return HttpResponseRedirect("/")
    else:
        post_list = Article.objects.filter(content__icontains=keywords.lower())
        if len(post_list) == 0:
            return render(request, 'index.html', {'post_list': post_list, 'none': True,'item_list':item_list})
        else:
            return render(request, 'index.html', {'post_list': post_list, 'none': False,'item_list':item_list})

#
# class SearchView(BaseView):
#     template_name = 'index.html'
#     context_object_name = 'post_list'
#
#     def get_queryset(self):
#         keyword=self.kwargs['q']
#         if keyword and keyword.strip() != "":
#             post_list = Article.objects.all()
#         else:
#             post_list = Article.object.filter(content__icontains=self.keyword.lower())
#         return post_list



'''Rss'''
from django.contrib.syndication.views import Feed


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):#按照时间降序
        return Article.objects.order_by('-date_time')

    def item_title(self, item): #rss标准写法,title,pubdate,description
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content


class IndexView(BaseView):
    template_name = 'index.html'
    context_object_name = 'post_list'
    paginate_by = 2


class AboutMeView(BaseView):
    template_name = 'about_me.html'


class ArchiveView(BaseView):
    template_name = 'archive.html'
    queryset = Article.objects.all()
    context_object_name = 'archive_list'


class SingleView(BaseView):
    template_name = 'single.html'
    context_object_name = 'post'

    def get_queryset(self):
        # post = get_object_or_404(Article, id=self.args[0])
        try:
            post = Article.objects.get(id=self.kwargs['id'])
        except:
            raise Http404
        return post


class CateView(BaseView):
    template_name = 'index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        post=Article.objects.filter(category__iexact=self.args[0])
        return post


# class DateView(BaseView):
#     template_name = 'single.html'
#     context_object_name = 'post_list'
#
#     def get_queryset(self):
#         post = Article.objects.filter(date_time=self.args[0])
#         return post
# class SearchView(DetailView):
#     template_name = 'index.html'
#     context_object_name = "post_list"
#     model = Article
#     keywords='keywords'
#
#     def get_object(self, queryset=None):
#         # cnum = int(self.kwargs.get(self.pk_url_kwarg, None))
#         keyword = self.kwargs.get(self.keywords, None)
#
#         queryset=Article.objects.filter(content__icontains=keyword)
#
#         try:
#             obj = queryset
#         except IndexError:
#             raise Http404
#         return obj






