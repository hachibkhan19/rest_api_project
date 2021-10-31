from django.urls import path
from . import api
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.Registration.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('article_api/', api.ArticleApiView.as_view(), name='article_api'),
    path('article_details/<int:id>/', api.ArticleApiDetails.as_view(), name='article_details'),
    path('create', views.CreateArticle.as_view(), name='create'),
    
]
