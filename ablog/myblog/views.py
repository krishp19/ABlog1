from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView
from .models import Post,Comment
from .forms import PostForm
# Create your views here.
#def home(request):
 #   return render(request,'home.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailViews(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddpostView(CreateView):
    model=Post
   # form_class=PostForm
    template_name = 'add.html'
    fields = '__all__'

class AddcommentView(CreateView):
    model= Comment
    template_name = 'comment.html'
    fields = '__all__'
