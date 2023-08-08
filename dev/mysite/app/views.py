from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from .models import Bicycle, Part, Brand_Choices, Partname_Choices
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.


#メインページ
def index_view(request):
    if request.user.is_authenticated:
        # ログインページ遷移
        user_id = request.user.id
        object = User.objects.get(id=user_id)
        login(request, object)
        return redirect('App:list')

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
            return render(request, 'index.html', {})
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザーはすでに登録されています。'})
                
    return render(request, 'signup.html', {})

#ログイン処理
def login_view(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('バリデーション成功')
            login(request, user)
            return HttpResponseRedirect(reverse('App:list'))
        else:
            print('バリデーション失敗')
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

#ログアウト処理
def logout_view(request):
    logout(request)
    return redirect('App:index')

#自転車一覧
def list_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('App:index'))
    
    context = {
        "bicycles": Bicycle.objects.all(),
        }
    print(context)
        
    return render(request, 'list.html', context)

#自転車登録ページ
def bicycle_create_view(request):
    user_id = request.user.id
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        image = request.FILES.get('image')
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        size = request.POST.get('size')
        year = request.POST.get('year')
        bicycle = Bicycle(user=user, image=image, brand=brand, model=model, size=size, year=year)
        print(image)
        bicycle.save()
        return redirect('App:list')
        
    return render(request, 'bicycle_create.html', {'choices': Brand_Choices})

#自転車詳細ページ
def bicycle_detail_view(request, bicycle_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('App:index'))

    bicycle = get_object_or_404(Bicycle, id=bicycle_id)
    parts = Part.objects.filter(bicycle=bicycle)
    partname_dict = dict(Partname_Choices)
    partname_choices = Partname_Choices

    context = {
        'bicycle': bicycle,
        'parts': parts,
        'partname_dict': partname_dict,
        'partname_choices': partname_choices,
    }
    
    return render(request, 'bicycle_detail.html', context)

#自転車削除ページ
def bicycle_delete_view(request, bicycle_id):
    bicycle = get_object_or_404(Bicycle, id=bicycle_id)
    
    if request.method == 'POST':
        bicycle.delete()
        return redirect('App:list')
    
    return render(request, 'bicycle_delete.html', {'bicycle': bicycle})

#パーツ登録ページ
def part_create_view(request, bicycle_id):
    context = {
        'bicycle_id': bicycle_id,
        'choices': Partname_Choices
    }
    if request.method == 'POST':
        bicycle = get_object_or_404(Bicycle, id=bicycle_id)
        partname = request.POST.get('partname')
        last_inspection_date = request.POST.get('last_inspection_date')
        parts = Part(bicycle=bicycle, partname=partname, last_inspection_date=last_inspection_date)
        parts.save()
        return redirect('App:bicycle_detail', bicycle_id = bicycle_id)
        
    return render(request, 'part_create.html', context)

#パーツ削除ページ
def part_delete_view(request, part_id):
    part = get_object_or_404(Part, id=part_id)
    partname_dict = dict(Partname_Choices)
    context = {
        'part': part,
        'partname_dict': partname_dict
    }
    
    if request.method == 'POST':
        part.delete()
        return redirect('App:bicycle_detail', bicycle_id = part.bicycle.id)
    
    return render(request, 'part_delete.html', context)
