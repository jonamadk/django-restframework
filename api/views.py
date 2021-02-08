from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
from .models import Article
from .serializer import ArticleSerializer
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from  rest_framework.views import APIView


# Create your views here.
class ArticleList(APIView):

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many =True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_404_CREATED)
        
class ArticleDetail(APIView):

    def get_object(self,pk):
        try:
            return Article.objects.get(id=pk)
        except Article.DoesNotExist:
            return HttpResponse(status=404)

    def get(self,request, pk):

        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)
        return Response(serializer.error , status =status.HTTP_400_CREATED)

    def delete(self, request, pk,format=None):
        article = self.get_object(pk)
        article.delete()
        return HttpResponse(status = 204)



