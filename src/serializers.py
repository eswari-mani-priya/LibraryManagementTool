# src/serializers.py

from rest_framework import serializers
from .models import Libraries, Books, LibraryActivities, LibraryBooks, LibraryUsers


# class ChoicesField(serializers.Field):
#     def __init__(self, choices, **kwargs):
#         self._choices = choices
#         super(ChoicesField, self).__init__(**kwargs)
#
#     def to_representation(self, obj):
#         return self._choices[obj]
#
#     def to_internal_value(self, data):
#         return getattr(self._choices, data)


class LibrariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libraries
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class LibraryUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryUsers
        fields = '__all__'


class LibraryBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryBooks
        fields = '__all__'


class LibraryActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryActivities
        fields = '__all__'









