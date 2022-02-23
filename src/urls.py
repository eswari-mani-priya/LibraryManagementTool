"""src app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import LibraryList, BooksDetailView, BooksList, LibraryBooksList, UsersList, LibraryActivityList,\
    LibraryBooksByUser, LibraryActivityDetail, LibraryBooksByLibrary
from django.urls import path

urlpatterns = [
    path('libraries/', LibraryList.as_view(), name="library_list"),
    path('books/', BooksList.as_view(), name='books_list'),
    path('books/<int:pk>/', BooksDetailView.as_view(), name="books_detail_view"),
    path('library_books/', LibraryBooksList.as_view(), name='library_books_list'),
    path('users/', UsersList.as_view(), name='users_list'),
    path('activities/', LibraryActivityList.as_view(), name='library_activity_list'),
    path('activities/<int:pk>/', LibraryActivityDetail.as_view(), name='activity_detail_view'),
    path('user_checkout_books/<int:pk>/', LibraryBooksByUser.as_view(), name='user_checkout_books'),
    path('library_checkout_books/<int:pk>/', LibraryBooksByLibrary.as_view(), name='library_checkout_books'),

]