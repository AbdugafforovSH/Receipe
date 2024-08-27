from django.contrib import admin
from .models import User, Recipe, RecipeText, Ingredients, Comment, CommentRecipe

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active']
    search_fields = ['username', 'email']
    list_filter = ['is_active', 'is_staff']
    ordering = ['username']

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'star', 'created_at', 'prep', 'cook', 'yields']
    search_fields = ['name']
    list_filter = ['created_at']
    ordering = ['created_at']

admin.site.register([ RecipeText,Ingredients, Comment, CommentRecipe])

