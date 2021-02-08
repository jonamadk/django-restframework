

from django.urls import path
from api.views import ArticleDetail, ArticleList

urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('article/<int:pk>/', ArticleDetail.as_view()),

]