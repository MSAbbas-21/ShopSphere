from django.urls import path
from .views import (
    add_to_cart,
    cart_list,
    update_cart,
    delete_cart,
)

urlpatterns = [
    path('add/', add_to_cart),
    path('', cart_list),
    path('update/<int:id>/', update_cart),
    path('delete/<int:id>/', delete_cart),
]