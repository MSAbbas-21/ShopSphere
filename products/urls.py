from django.urls import path
from .views import (
    product_list,
    product_detail,
    create_product,
    update_product,
    delete_product,
    category_list,
    category_detail,
    create_category,
    update_category,
    delete_category,
)

urlpatterns = [

    # Product APIs
    path('', product_list),
    path('create/', create_product),
    path('<int:id>/', product_detail),
    path('update/<int:id>/', update_product),
    path('delete/<int:id>/', delete_product),

    # Category APIs
    path('categories/', category_list),
    path('categories/create/', create_category),
    path('categories/<int:id>/', category_detail),
    path('categories/update/<int:id>/', update_category),
    path('categories/delete/<int:id>/', delete_category),

]