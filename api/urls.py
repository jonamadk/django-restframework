

from django.urls import path
from api.views import article_list, article_detail

urlpatterns = [
    path('articles/', article_list),
    path('article/<int:pk>/', article_detail)

]