from django.urls import path
from . import views 
from .views import login_view, register_view


urlpatterns = [
    
    path('', views.Home.as_view(), name='home'),
    path('about', views.About.as_view(), name='about'),
    path('blog-post', views.BlogPost.as_view(), name='blog-post'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('elements', views.Element.as_view(), name='elements'),
    path('receipe-post', views.RecipePost.as_view(), name='recipe-post'),
    path('login', login_view, name='login'),
    path('register', register_view, name='register'),
    path('recipe-detail/<int:recipe_id>', views.RecipeDetail.as_view(), name='recipe-detail'),
]
