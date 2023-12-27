from django.urls import path,include
#from . import views
from .views import HomeView,ArticleDetailViews,AddpostView,AddcommentView
urlpatterns = [
    #path('',views.home,name='home')
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>', ArticleDetailViews.as_view(),name = 'article-detail'),
    path('add_post/',AddpostView.as_view(),name='add_post'),
    path('article/<int:pk>/comment/',AddcommentView.as_view(),name='add_comment')
]
