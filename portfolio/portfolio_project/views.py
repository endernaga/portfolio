from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from cart.form import CartAddProductForm
from portfolio_project.forms import CommentsForm, RegisterUserForm, AuthenticationUserForm
from portfolio_project.models import *


class MainPage(ListView):
    model = Products
    template_name = 'portfolio_project/shop.html'
    context_object_name = 'products'
    paginate_by = 15


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        context['rubricks'] = Rubricks.objects.all()
        context['tags'] = Tags.objects.all()
        return context


class PageByCategories(ListView):
    model = Products
    template_name = 'portfolio_project/shop.html'
    paginate_by = 15
    context_object_name = 'products'


    def get_queryset(self):
        return Products.objects.filter(rubrick__slug=self.kwargs['slug'])


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PageByCategories, self).get_context_data(**kwargs)
        context['title'] = 'Товари по категоріям'
        context['tags'] = Tags.objects.all()
        context['rubricks'] = Rubricks.objects.all()
        return context


class PageByTags(ListView):
    model = Products
    template_name = 'portfolio_project/shop.html'
    paginate_by = 15
    context_object_name = 'products'


    def get_queryset(self):
        return Products.objects.filter(tag__slug=self.kwargs['slug'])


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PageByTags, self).get_context_data(**kwargs)
        context['title'] = 'Товари по категоріям'
        context['tags'] = Tags.objects.all()
        context['rubricks'] = Rubricks.objects.all()
        return context



class DetailPage(DetailView):
    model = Products
    template_name = 'portfolio_project/detail.html'
    context_object_name = 'products'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DetailPage, self).get_context_data(**kwargs)
        CartAddProductForm.QUANTITY = Products.objects.get(id=kwargs['object'].pk).avaibility
        print(CartAddProductForm.QUANTITY)
        context['tags'] = Tags.objects.all()
        context['comments_field'] = CommentsForm
        context['rubricks'] = Rubricks.objects.all()
        context['cart_form'] = CartAddProductForm
        return context

    def post(self, request, slug):
        name = request.POST.get('name')
        text = request.POST.get('text')
        post_id = Products.objects.get(slug=slug).pk
        Comment(name=name, text=text, post_id=post_id).save()
        return redirect('detail', slug=slug)


def pageNotFound(request, exceptions):
    return HttpResponseNotFound(request, template_name='404.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('main')
    template_name = 'portfolio_project/Register.html'


    def get_context_data(self, **kwargs):
        context = super(RegisterUser, self).get_context_data(**kwargs)
        context['auth'] = 'Регістрація'
        context['title'] = 'Регістрація'
        context['action'] = 'Зареєструватись'
        return context


class LoginUser(LoginView):
    form_class = AuthenticationUserForm
    template_name = 'portfolio_project/Register.html'


    def get_context_data(self, **kwargs):
        context = super(LoginUser, self).get_context_data(**kwargs)
        context['auth'] = 'Авторизація'
        context['title'] = 'Авторизація'
        context['action'] = 'Авторизуватись'
        return context


    def get_success_url(self):
        return reverse('main')


def UserLoggedIn(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username


def userLogout(request):
    username = UserLoggedIn(request)
    if username:
        logout(request)
        return redirect('auth')


def logoutRequest(request):
    context = {'title': 'Вихід', 'name': 'Вихід з акаунту'}
    return render(request, 'portfolio_project/logout.html', context=context)