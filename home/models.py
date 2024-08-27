from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='custom_user'
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set_permissions', 
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='custom_user_permissions'
    )
    
    def __str__(self) -> str:
        return f'{self.username}'
    

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    star = models.IntegerField()
    image = models.ImageField(upload_to='recipe-images/')
    created_at = models.DateField(auto_now_add=True)
    prep = models.IntegerField()
    cook = models.IntegerField()
    yields = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    

class RecipeText(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='text')
    text = models.TextField()


    def __str__(self) -> str:
        return f'{self.text[:50]}'
    


class Ingredients(models.Model):
    name = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self) -> str:
        return self.name
    

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name
    


class Contact(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name
    

class CommentRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.message[:50]
    

    