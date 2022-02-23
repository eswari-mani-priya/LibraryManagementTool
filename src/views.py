from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.views import View
import json
from .models import Libraries, Books, LibraryBooks, LibraryActivities, LibraryUsers
from .serializers import LibrariesSerializer, BooksSerializer, LibraryBooksSerializer, \
    LibraryActivitiesSerializer, LibraryUsersSerializer

# Create your views here.


class LibraryList(generics.ListCreateAPIView):
    queryset = Libraries.objects.all()
    serializer_class = LibrariesSerializer


class BooksList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BooksSerializer

    def get_object(self):
        pk = int(self.kwargs['pk'])
        return get_object_or_404(Books.objects.all(), book_id=pk)


class LibraryBooksList(generics.ListCreateAPIView):
    queryset = LibraryBooks.objects.all()
    serializer_class = LibraryBooksSerializer


class UsersList(generics.ListCreateAPIView):
    queryset = LibraryUsers.objects.all()
    serializer_class = LibraryUsersSerializer


class LibraryActivityList(generics.ListCreateAPIView):
    queryset = LibraryActivities.objects.all()
    serializer_class = LibraryActivitiesSerializer

    def create(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        print("data:", data)
        serializer = LibraryActivitiesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("serializer saved!")
            library_activity_obj = LibraryActivities.objects.get(library_book_id=data['library_book_id'])
            library_activity_obj.save()
            library_book_obj = LibraryBooks.objects.get(library_book_id=data['library_book_id'])
            library_book_obj.last_library_activity_id = library_activity_obj
            library_book_obj.save()
            print("Library book got saved!!")
            return JsonResponse(serializer.data, status=201)


class LibraryActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LibraryActivitiesSerializer

    def get_object(self):
        pk = int(self.kwargs['pk'])
        return get_object_or_404(LibraryActivities.objects.all(), library_activity_id=pk)


class LibraryBooksByUser(View):

    def get(self, request, pk):
        library_activity_obj = LibraryActivities.objects.filter(Q(user_id=pk) & Q(activity_type='CHECK_OUT'))
        data = {}
        for each in library_activity_obj:
            data['activity_type'] = 'CHECK_OUT'
            data['user_name'] = each.user_id.name
            data['library_activity_id'] = each.library_activity_id
            data['checked_out_at'] = each.checked_out_at.strftime("%m/%d/%Y, %H:%M:%S")
            data['library_book_id'] = each.library_book_id.library_book_id
            data['library_id'] = each.library_book_id.library_id.library_id
            data['library_name'] = each.library_book_id.library_id.name
            data['book_id'] = each.library_book_id.book_id.book_id
            data['book_name'] = each.library_book_id.book_id.title
        return JsonResponse(data, status=200)


class LibraryBooksByLibrary(View):

    def get(self, request, pk):
        library_activity_obj = LibraryActivities.objects.filter(Q(library_book_id__library_id__library_id=pk) & Q(activity_type='CHECK_OUT'))
        data = {}
        for each in library_activity_obj:
            data['activity_type'] = 'CHECK_OUT'
            data['user_name'] = each.user_id.name
            data['library_activity_id'] = each.library_activity_id
            data['checked_out_at'] = each.checked_out_at.strftime("%m/%d/%Y, %H:%M:%S")
            data['library_book_id'] = each.library_book_id.library_book_id
            data['library_id'] = each.library_book_id.library_id.library_id
            data['library_name'] = each.library_book_id.library_id.name
            data['book_id'] = each.library_book_id.book_id.book_id
            data['book_name'] = each.library_book_id.book_id.title
        return JsonResponse(data, status=200)





