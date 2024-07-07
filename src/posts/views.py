from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import BlogPost
from django.core.paginator import Paginator
from .forms import Contact


# Create your views here.


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"
    paginate_by = 6

class BlogHomeP(ListView):
    model = BlogPost
    context_object_name = "posts"
    template_name = "posts/blogpost_list.html"

class BlogHomeC(CreateView):
    form_class = Contact
    template_name = "posts/contacts.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


class BlogHomeA(ListView):
    model = BlogPost
    context_object_name = "posts"
    template_name = "posts/apropo.html"
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)


@method_decorator(login_required, name="dispatch")
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ['title', 'author', 'created_on', 'published', 'content', ]
    #fields = '__all__'

    success_url = reverse_lazy("posts:home")

@method_decorator(login_required, name="dispatch")
class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_editer.html"
    fields = ['title', 'content', 'published']


class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"

@method_decorator(login_required, name="dispatch")
class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = "post"
    success_url = reverse_lazy("posts:home")


#def Logins(request):
    #if request.methode == "POST":
        #username = request.POST["username"]
        #password = request.POST["password"]
        #password1 = request.POST["password1"]
        #firstname = request.POST["firstname"]
        #lastname = request.POST["lastname"]

       # if password == password1 :
           # user = User.objects.create_user(username=username, password=password)
            #user.first_name = firstname
            #user.last_name = lastname





