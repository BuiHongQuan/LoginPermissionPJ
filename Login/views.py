from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *


class IndexClass(View):
    def get(self, request):
        return HttpResponse("HELLU")


class LoginClass(View):
    def get(self, request):
        return render(request, 'login/login.html')

    def post(self, request):
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        my_user = authenticate(username=user_name, password=password)
        if my_user is None:
            return HttpResponse("Dang nhap that bai")
        # ham login truyen vao request va my_user da authenticated
        login(request, my_user)
        return render(request, 'Login/success.html')


class ViewUser(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return HttpResponse('Day la view user')


@decorators.login_required(login_url='/login/')
def view_product(request):
    return HttpResponse('Xem san pham')


class AddPost(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        f = PostForm()
        context = {'fm': f}
        return render(request, 'login/addpost.html', context)

    def post(self, request):
        f = PostForm(request.POST)

        if not f.is_valid():
            return HttpResponse('Sai du lieu')
        print(request.user.get_all_permissions())
        if request.user.has_perm('Login.addpost'):
            f.save()
        else:
            return HttpResponse("You don't have permission to add post")
        return HttpResponse('oke')
