from django.urls import path
from .views import (
    add_to_wishlist,
    my_wishlist,
    remove_from_wishlist,
)

urlpatterns = [
    path("add/<int:id>/", add_to_wishlist),
    path("", my_wishlist),
    path("remove/<int:id>/", remove_from_wishlist),
]