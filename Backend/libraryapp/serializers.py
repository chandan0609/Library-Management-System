from rest_framework import serializers

from .models import User, Book, BorrowRecord, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['id','username','email','password','role']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = ['id','title','author','category','ISBN','status']

class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        field = ['id','user','book','borrow_date','due_date','return_date']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= ['id','name','books']
