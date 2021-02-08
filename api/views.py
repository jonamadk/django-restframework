from django.db.models.query import QuerySet
from django.shortcuts import render

from .models import Article
from .serializer import ArticleSerializer

from rest_framework import generics
from rest_framework.authentication import SessionAuthentication,TokenAuthentication , BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ArticleList(generics.ListCreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes =[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

  
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]

   


