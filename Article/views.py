from django.shortcuts import render,get_object_or_404,redirect
from .models import Article,Rating
from user.forms import ArticleForm,commentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def home_page(request):
    return render(request,'home_page.html')
def about(request):
    return render(request,'about.html')
def articles(request):
    articles = Article.objects.all()
    context = dict(
        articles = articles
    )
    return render(request,'articles.html',context)

def article(request,id):
    # article = Article.objects.get(id=id)
    article = get_object_or_404(Article,id=id)
    context = dict(
        article = article
    )
    return render(request,'article.html',context)
@login_required
def myarticles(request):
    articles = Article.objects.filter(author = request.user)
    context = dict(
        articles = articles
    )
    return render(request,'myarticles.html',context)
@login_required
def updateArticle(request,id):
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,instance=article)
    context = dict(
        form = form
    )
    if form.is_valid():
        newarticle = form.save(commit=False)
        newarticle.author = request.user
        newarticle.save()
        messages.success(request,'Makale Başarıyla Güncellendi.')
        return redirect('anasayfa')
    return render(request,'update.html',context)
@login_required
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)
    article.delete()
    messages.success(request,'Makale başarıyla silindi.')
    return redirect('anasayfa')


def comment(request,id):
    
    form = commentForm(request.POST or None)
    article = get_object_or_404(Article,id = id)
    context = dict(
        form = form
    )
    if form.is_valid():
        comment = form.save(commit=False)
        comment.title = article.title
        comment.save()
        messages.success(request,'Yorum Başarıyla Eklendi.')
        return redirect('anasayfa')

    return render(request,'comment.html',context)


def comments(request,id):
    article = get_object_or_404(Article,id = id)
    comment = Rating.objects.filter(title = article.title)
    context = dict(
        comment = comment
    )
    return render(request,'comments.html',context)

