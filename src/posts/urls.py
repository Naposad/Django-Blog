from .views import BlogHome, BlogPostCreate, BlogPostUpdate, BlogPostDetail, BlogPostDelete, BlogHomeP, BlogHomeA, BlogHomeC
from django.urls import path

app_name = "posts"
urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('list', BlogHomeP.as_view(), name="home-list"),
    path('<str:slug>', BlogPostDetail.as_view(), name="detail"),
    path('create/', BlogPostCreate.as_view(), name="create"),
    path('edit/<str:slug>', BlogPostUpdate.as_view(), name="edit"),
    path('delete/<str:slug>', BlogPostDelete.as_view(), name="delete"),
    path('apropo/', BlogHomeA.as_view(), name="apropo"),
    path('contact/', BlogHomeC.as_view(), name="contact"),

]
