
from django.contrib import admin
from django.urls import path, include
from . import views
#应用的名称
app_name = 'blog'

urlpatterns = [
   path('article-list/', views.article_list, name='article_list'),
   path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
   path('article-create/', views.article_create, name='article_create'),
   path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
   path('article-update/<int:id>/', views.article_update, name='article_update'),
]