from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from .models import Bicycle, Part, Brand_Choices
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.


#メインページ処理
def index_view(request):
    if request.user.is_authenticated:
        # ログインページ遷移
        login(request, User)
        user_id = request.User.id
        object = User.objects.get(id=user_id)
        return HttpResponseRedirect(render(request, 'list.html', {'object': object}))

    return render(request, 'index.html', {})

#新規登録処理
def singup_view(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, email, password)
            return render(request, 'signup.html', {})
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザーはすでに登録されています。'})
                
    return render(request, 'signup.html', {})

#ログイン処理
def login_view(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            user_id = request.User.id
            object = User.objects.get(id=user_id)
            return render(request, 'list.html', {'object': object})
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

#ログアウト処理
def logout_view(request):
    logout(request)
    return redirect('App:index')

#メインページ
def list_view(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if not request.user.is_authenticated:
        # ログインページ遷移
        return HttpResponseRedirect(reverse('App:index'))
    
    context = {
        "bicycles": Bicycle.objects.all(),
        }
    for bicycle in Bicycle.objects.all():
        print(bicycle.image)
    
    return render(request, 'list.html', context)

#自転車登録ページ
def bicycle_create_view(request):
    return render(request, 'bicycle_create.html', )

#自転車詳細ページ
def bicycle_detail_view(request, pk):

    context = {
        'parts': Part.objects.all(),
        'bicycle': Bicycle.objects.all(),
        }
    
    return render(request, 'bicycle_detail.html', context)

#パーツ登録ページ
def part_create_view(request):
    
    return render(request, 'part_create.html')