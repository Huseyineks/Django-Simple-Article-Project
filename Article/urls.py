from django.contrib import admin
from django.urls import path
from Article import views
app_name = 'Article'
urlpatterns = [
   
    path('', views.articles,name='articles'),
    path('article/<int:id>', views.article,name='article'),
    path('myarticles/', views.myarticles,name='myarticles'),
    path('update/<int:id>', views.updateArticle,name='update'),
    path('delete/<int:id>', views.deleteArticle,name='delete'),
    path('comment/<int:id>', views.comment,name='comment'),
    path('comments/<int:id>', views.comments,name='comments'),
]