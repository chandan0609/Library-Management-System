from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin','Admin'),
        ('user','User'),
    ]
    role = models.CharField(max_length=5, choices=ROLE_CHOICES)
# Add related_name to avoid conflicts with Django's User model
    groups = models.ManyToManyField(
        Group,
        related_name='libraryapp_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='libraryapp_user_permissions',
        blank=True
    )
class Category(models.Model):
    name = models.CharField(max_length=100)
def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    ISBN = models.CharField(max_length=13, unique=True)
    status = models.CharField(max_length=15, default='available')
class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)