from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from . models import Article
from . forms import RegistrationForm, ArticleForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'base.html', context)

class Registration(View):
    def get(self, request):
        form = RegistrationForm
        context = {
            'form': form
        }
        return render(request, 'register.html', context)
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            instance  = form.save(commit=False)
            instance.save()
            return redirect('login')
    
class Login(View):
    template_name = "login.html"
    
    def get(self, request): 
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('index')
    

class CreateArticle(View):
    def get(self, request):
        form = ArticleForm
        context = {
            'form': form
        }
        return render(request, 'create.html', context)
    
    def post(self, request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('index')
        
        
