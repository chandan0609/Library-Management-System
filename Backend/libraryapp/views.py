from rest_framework import viewsets
from django.shortcuts import render
from .models import User,Book, BorrowRecord,Category
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .utils import send_due_notification
from django.utils import timezone
from .serializers import UserSerializer,BookSerializer,BorrowRecordSerializer, CategorySerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsAuthenticated]
    
    def check_due_books(self):
        records = BorrowRecord.objects.filter(due_date__lte=timezone.now())
        for record in records:
            if not record.return_date:
                user_email = record.user.email
                book_title = record.book.title
                due_date = record.due_date.strftime('%Y-%m-%d')
                send_due_notification(user_email, book_title, due_date)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer