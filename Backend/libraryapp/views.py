from rest_framework import viewsets
from django.shortcuts import render
from .models import User,Book, BorrowRecord,Category
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .utils import send_due_notification
from django.utils import timezone
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