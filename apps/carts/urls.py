from django.urls import path
from apps.carts.views import CartListAPIView, CartCreateAPIView, CartDeleteAPView

urlpatterns = [
    path('list', CartListAPIView.as_view(), name='cart-list'),
    path('create', CartCreateAPIView.as_view(), name='cart-create'),
    path('delete/<int:id>', CartDeleteAPView.as_view(), name='cart-delete')
]