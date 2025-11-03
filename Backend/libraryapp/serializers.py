from rest_framework import serializers

from .models import User, Book, BorrowRecord, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password','role']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','author','category','ISBN','status']

class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['id','user','book','borrow_date','due_date','return_date']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= ['id','name','books']
