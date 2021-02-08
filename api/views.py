from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Article
from .serializer import ArticleSerializer

from rest_framework import generics

# Create your views here.
class ArticleList(generics.ListCreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
        
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



