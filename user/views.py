from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
       username = form.cleaned_data.get("username")  
       password = form.cleaned_data.get("password")


       newUser = User(username = username)
       newUser.set_password(password)
       newUser.save()
       login(request,newUser)
       messages.success(request,'Başarıyla Kayıt Olundu')
       return redirect("anasayfa")

    context = {
        "form":form
    }  
    return render(request,'register.html',context)
   
def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        if user is None:
            messages.info(request,'Kullanıcı Adı veya Parola Hatalı')
            return render(request,'login.html',context)
        messages.success(request,'Başarıyla Giriş Yaptınız.')
        login(request,user)
        return redirect('anasayfa')
    return render(request,'login.html',context)
@login_required
def logoutUser(request):
    logout(request)
    messages.success(request,'Başarıyla çıkış yaptınız.')
    return redirect('anasayfa')
@login_required
def addArticle(request):
    form = ArticleForm(request.POST or None)
    context = dict(
        form = form
    )
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,'Makale Başarıyla Eklendi')
        return redirect('anasayfa')
    return render(request,'addarticle.html',context)