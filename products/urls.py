from django.urls import path
from .views import (
    product_list,
    product_detail,
    create_product,
    update_product,
    delete_product,
)

urlpatterns = [
    path('', product_list),
    path('create/', create_product),
    path('<int:id>/', product_detail),
    path('update/<int:id>/', update_product),
    path('delete/<int:id>/', delete_product),
]