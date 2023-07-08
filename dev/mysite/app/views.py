from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Bicycle
from .forms import BicycleForm
from .models import Brand_Choices

# Create your views here.


#メインページ処理
def template_view(request):
    if request.user.is_authenticated:
        # ログインページ遷移
        return HttpResponseRedirect(reverse('App:mainpage'))

    return render(request, 'index.html')

#新規登録処理
def singup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('form')
    else:
        form = SignupForm()
        
    param = {
        "form": form,
    }

    return render(request, 'signup.html', param)

#ログイン処理
def login_view(request):
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('username')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ログインページ遷移
                return HttpResponseRedirect(reverse('App:mainpage'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'login.html')

#ログアウト処理
def logout_view(request):
    logout(request)
    return redirect('App:list')

#ページ
def mainpage_view(request):
    if not request.user.is_authenticated:
        # ホームページ遷移
        return HttpResponseRedirect(reverse('App:list'))
    
    context = {
        "bicycles": Bicycle.objects.all(),
        }
    for bicycle in Bicycle.objects.all():
        print(bicycle.image)
    
    return render(request, 'mainpage.html', context)

#自転車登録ページ
def bicycle_create_view(request):
    context = None
    if request.method == 'POST':
        form = BicycleForm(request.POST, request.FILES)
        for field in form:
            print("Field Error:", field.name,  field.errors)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            model = form.cleaned_data['model']
            year = form.cleaned_data['year']
            image = form.cleaned_data['image']
            bicycle = Bicycle(brand=brand, model=model, year=year, image=image)
            bicycle.save()
            return redirect('App:mainpage')
    else:
        form = BicycleForm()
        choices = Brand_Choices
        context = {
            'form' : form,
            'choices' : choices
        }
    
    return render(request, 'bicycle_create.html', context)

#自転車詳細ページ
def bicycle_detail_view(request):
    
    return render(request, 'bicycle_detail.html')

#パーツ登録ページ
def part_create_view(request):
    
    return render(request, 'part_create.html')