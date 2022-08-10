from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from brm.forms import NewBookForm,SearchForm
from brm import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='http://localhost:8000/brm/login/')
def NewBook(request):
    form=NewBookForm()
    res=render(request,'brm/new_book.html',{'form':form})
    return res
def index(request):
     res=render(request,'brm/index.html')
     return res

@login_required(login_url='http://localhost:8000/brm/login/')
def addBook(request):
    msg=""
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.title=form.data['title']
        book.author=form.data['author']
        book.price=form.data['price']
        book.publisher=form.data['publisher']
        book.save()
    else:
        msg="Record cannot be saved in database"
    msg=msg+ "<br><a href='http://localhost:8000/brm/view-books'>View Books</a>"
    return HttpResponse(msg)
@login_required(login_url='http://localhost:8000/brm/login/')
def viewBooks(request):
    book=models.Book.objects.all()
    res=render(request,'brm/view_books.html',{'books':book})
    return res
@login_required(login_url='http://localhost:8000/brm/login/')
def deleteBook(request):
    bookid=request.GET['book-id']
    book=models.Book.objects.filter(id=bookid)
    book.delete();
    return HttpResponseRedirect('http://localhost:8000/brm/view-books')
@login_required(login_url='http://localhost:8000/brm/login/')
def editBook(request):
    book=models.Book.objects.get(id=request.GET['book-id']);
    fields={'title':book.title,'author':book.author,'price':book.price,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'brm/edit_book.html',{'form':form,'book':book})
    return res
@login_required(login_url='http://localhost:8000/brm/login/')
def edit(request):
    if request.method=="POST":
        form=NewBookForm(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.author=form.data['author']
        book.price=form.data['price']
        book.publisher=form.data['publisher']
        book.save()
    return HttpResponseRedirect("http://localhost:8000/brm/view-books")
@login_required(login_url='http://localhost:8000/brm/login/')
def searchBook(request):
    form=SearchForm()
    res=render(request,'brm/search_book.html',{'form':form})
    return res
@login_required(login_url='http://localhost:8000/brm/login/')
def search(request):
    form=SearchForm(request.POST)
    title=form.data['title']
    books=models.Book.objects.filter(title=title)
    res=render(request,'brm/search_book.html',{'books':books,'form':form})
    return res
def userlogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session.username=username
            return(HttpResponseRedirect('http://localhost:8000/brm/view-books'))
        else:
            data['error':"Username or Password is incorrect"]
            res=render[request,'brm/login.html',data]
            return res
    else:
         res=render(request,'brm/login.html',data)
         return res
@login_required(login_url='http://localhost:8000/brm/login/')
def userlogout(request):
    logout(request)
    del request.session.username
    return HttpResponseRedirect('http://localhost:8000/brm/login/')
