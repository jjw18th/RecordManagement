from django.urls import path
from . import views
urlpatterns=[path('new-book/',views.NewBook),path('add/',views.addBook),path('view-books/',views.viewBooks),path('delete-book/',views.deleteBook),path('edit/',views.edit),path('edit-book',views.editBook),path('search-book/',views.searchBook),path('search/',views.search),path('login/',views.userlogin),path('logout/',views.userlogout),]
