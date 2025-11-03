from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'books',views.BookViewSet)
router.register(r'borrow-records',views.BorrowRecordViewSet)
router.register(r'categories',views.CategoryViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]