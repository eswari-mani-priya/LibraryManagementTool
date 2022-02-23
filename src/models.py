# models.py
from django.db import models, connection
from model_utils import Choices
from enumchoicefield import ChoiceEnum, EnumChoiceField

# Create your models here.

class Libraries(models.Model):
    id = models.AutoField(name='library_id', primary_key=True, auto_created=True)
    name = models.CharField(max_length=150, null=False)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    postal_code = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name


class Books(models.Model):
    id = models.AutoField(name='book_id', primary_key=True, auto_created=True)
    title = models.CharField(max_length=200, null=False)
    author_name = models.CharField(max_length=200, null=False)
    isbn_num = models.CharField(max_length=100, null=False)
    genre = models.CharField(max_length=100, null=False)
    description = models.TextField()

    def __str__(self):
        return self.title


class LibraryUsers(models.Model):
    id = models.AutoField(name='user_id', primary_key=True, auto_created=True)
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name


class LibraryActivities(models.Model):
    ActivityTypes = Choices(
        ("CHECK_IN", "CHECK_IN"),
        ("CHECK_OUT", "CHECK_OUT"),
    )
    id = models.AutoField(name="library_activity_id", primary_key=True)
    activity_type = models.CharField(max_length=10, choices=ActivityTypes, default=ActivityTypes.CHECK_IN)
    user_id = models.ForeignKey('LibraryUsers', on_delete=models.CASCADE)
    library_book_id = models.ForeignKey('LibraryBooks', related_name='library_book', on_delete=models.CASCADE)
    checked_out_at = models.DateTimeField(null=True)
    checked_in_at = models.DateTimeField(null=True)


class LibraryBooks(models.Model):
    id = models.AutoField(name='library_book_id', primary_key=True)
    library_id = models.ForeignKey('Libraries', on_delete=models.CASCADE)
    book_id = models.ForeignKey('Books', on_delete=models.CASCADE)
    last_library_activity_id = models.ForeignKey(LibraryActivities, related_name="last_activity",
                                                 on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.library_id.name + ' ' + self.book_id.title



