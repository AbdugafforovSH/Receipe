from django.shortcuts import render, redirect
from django.views import View 
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import User, Recipe, CommentRecipe
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginRequiredMixin, View):
    def get(self, request):
        recipes = Recipe.objects.all()
        return render(request, 'index.html', context={'recipes': recipes})
    

class About(View):
    def get(self, request):
        return render(request, 'about.html')
    
class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')
class BlogPost(View):
    def get(self, request):
        return render(request, 'blog-post.html')
class Element(View):
    def get(self, request):
        return render(request, 'elements.html')
class RecipePost(View):
    def get(self, request):
        return render(request, 'receipe-post.html')
    
class RecipeDetail(View):
    def get(self, request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        return render(request, 'receipe-post.html', context={'recipe': recipe})

    def post(self, request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        user = request.user
        message = request.POST.get('message')
        print(message, user, recipe, 's')
        # if message:
        CommentRecipe.objects.create(user=user, recipe=recipe, message=message)
        return redirect('recipe-detail',recipe_id=recipe_id)
        # else:
            # return render(request, 'receipe-post.html', context={'recipe': recipe, 'error': 'Message cannot be empty'})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            return render(request, 'login.html', {'error': 'Login yoki parol noto\'g\'ri'})

    return render(request, 'login.html')

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        email = request.POST.get('email')

        print(username, password, email, password1)
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Bunday foydalanuvchi mavjud'})
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Bunday elektron pochta mavjud'})
        
        if password!= password1:
            return render(request, 'register.html', {'error': 'Parollar mos kelishi kerak'})

        
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        return redirect('login')
    
    return render(request, 'register.html')