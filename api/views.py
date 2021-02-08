from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
from rest_framework.parsers import JSONParser
from .models import Article
from .serializer import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.views import APIView

# Create your views here.
class ArticleList(generics.GenericAPIView, 
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return  self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)
        
        
class ArticleDetail(generics.GenericAPIView,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    ):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self,request, pk, *args, **kwargs):

        return self.retrieve(request, *args, **kwargs)
        
    def put(self, request, pk, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        
        return self.destroy(request, *args, **kwargs)



