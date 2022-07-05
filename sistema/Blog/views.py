from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from Blog.models import BlogModel
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm



class BlogList(ListView):

    model = BlogModel
    template_name = "PaginasBlog/blog_list.html"


class BlogDetail(DetailView):

    model = BlogModel
    template_name = "PaginasBlog/blog_details.html"


class BlogCreate(CreateView):

    model = BlogModel
    #template_name = "PaginasBlog/blog.html"
    success_url = reverse_lazy("blog_list") #Esto lo saqué y dejé el de arriba
    fields = ["titulo", "sub_titulo", "cuerpo"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class BlogUpdate(UserPassesTestMixin, UpdateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["Tema", "Subtema", "Opinion"]

    def test_func(self):
        exist = BlogModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False
        


class BlogDelete(UserPassesTestMixin, DeleteView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")

    def test_func(self):
        exist = BlogModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False


class BlogLogin(LoginView):
    template_name = 'PaginasBlog/blog_login.html'
    next_page = reverse_lazy("blog_list")


class BlogLogout(LogoutView):
    template_name = 'PaginasBlog/blog_logout.html'
# Create your views here.
