from django.http import Http404
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from article.models import Article
import json
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import ArticleDetailSerializer,ArticleListSerializer
from rest_framework import viewsets
from rest_framework import permissions
# Create your views here.

# test
def hello(request):
    return HttpResponse("<h1>Hello Django</h1>")



#
# @csrf_exempt
# def ajax(request):
#     parameter = request.POST['content']
#     a=Article.objects.values('title').filter(title__icontains=parameter)
#     res_dict={'parameter':parameter,'result':"    ||    ".join(list(map(lambda x:x['title'],list(a))))}
#     return JsonResponse(res_dict)





# '''restful'''
# from rest_framework.renderers import  JSONRenderer
# from rest_framework.parsers import JSONParser


# @api_view(['GET', 'POST'])
# def article_list(request, format=None):
#     if request.method =='GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles,many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data,status=201)
#         else:
#             return JSONResponse(serializer.errors, status=400)


# @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, id ,format=None):
#     """
#     Retrieve, update or delete a code Article.
#     """
#     try:
#         article = Article.objects.get(id=id)
#     except Article.DoesNotExist:
#         # raise Http404
#         return render(request,'error.html')

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(json.dumps(serializer.data))

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)





# 

# class ArticleList(APIView):
     
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
#     def get(self, request, format=None):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def perform_create(self,serilizer):
#         serilizer.save(author=self.request.user)

'''
class ArticleDetail(APIView):
   
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

# from django.contrib.auth.models import User
# from .serializers import UserSerializer

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

'''
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class =ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

'''

from rest_framework.decorators import detail_route

class ArticleDetailViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Article.objects.values("id", "title", "category", "date_time", "content")
    # queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


    @detail_route()
    def detail(self,req,*args,**kwargs):
        article = self.get_object()
        return Response(article)


class ArticleListViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = Article.objects.values("id","title","category","date_time")
    # queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


    