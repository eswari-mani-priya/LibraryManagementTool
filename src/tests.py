from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from datetime import datetime
from .views import BooksList, LibraryBooksList, LibraryBooksByUser
from .models import Libraries, Books, LibraryBooks, LibraryActivities, LibraryUsers
import json

# Create your tests here.


class TestingBooksList(APITestCase):

    def test_create_book(self):
        factory = APIRequestFactory()
        view = BooksList.as_view()
        data = {'title': 'Test_Title',
                'author_name': 'Test_Author',
                'isbn_num': '1111',
                'genre': 'Test_Genre',
                'description': 'Test_Description'}
        request = factory.post('/books/', json.dumps(data), content_type='application/json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_bookslist(self):
        factory = APIRequestFactory()
        view = BooksList.as_view()
        request = factory.get('/books/')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestLibraryBooksList(APITestCase):
    def test_create_library_book(self):
        factory = APIRequestFactory()
        view = LibraryBooksList.as_view()
        library_obj = Libraries.objects.create(name='Test_Lib', city='Test_City', state='Test_State', postal_code=1111)
        book_obj = Books.objects.create(title='Test_Title',author_name='Test_Author',isbn_num='1111',genre='Test_Genre',description='Test_Description')
        data = {'library_id': library_obj.library_id, 'book_id': book_obj.book_id}
        request = factory.post('/library_books/', json.dumps(data), content_type='application/json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_library_bookslist(self):
        factory = APIRequestFactory()
        view = LibraryBooksList.as_view()
        request = factory.get('/library_books/')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestLibraryBooksByUser(APITestCase):
    def test_get_library_books_by_user(self):
        factory = APIRequestFactory()
        user_obj = LibraryUsers.objects.create(name='Test_User')
        library_obj = Libraries.objects.create(name='Test_Lib', city='Test_City', state='Test_State', postal_code=1111)
        book_obj = Books.objects.create(title='Test_Title', author_name='Test_Author', isbn_num='1111',
                                        genre='Test_Genre', description='Test_Description')
        library_book_obj = LibraryBooks.objects.create(library_id=library_obj, book_id=book_obj)
        cur_date_time = datetime.now()
        library_activity_obj = LibraryActivities.objects.create(activity_type='CHECK_OUT',
                                                                user_id=user_obj,
                                                                library_book_id=library_book_obj,
                                                                checked_out_at=cur_date_time)
        view = LibraryBooksByUser.as_view()
        request = factory.get('/user_outbooks/1')
        response = view(request, pk='1')
        # response.render()
        result = {'activity_type': 'CHECK_OUT',
                  'user_name': "Test_User",
                  'library_activity_id': 1,
                  'checked_out_at': str(cur_date_time.strftime("%m/%d/%Y, %H:%M:%S")),
                  'library_book_id': 1,
                  'library_id': 1,
                  'library_name': "Test_Lib",
                  'book_id': 1,
                  'book_name': "Test_Title"}
        print(json.dumps(result))
        print(response.content.decode("UTF-8"))
        self.assertEqual(response.content.decode("UTF-8"), json.dumps(result))
