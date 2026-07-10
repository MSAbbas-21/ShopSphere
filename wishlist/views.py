from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Wishlist
from .serializers import WishlistSerializer
from products.models import Product


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_wishlist(request, id):

    try:
        product = Product.objects.get(id=id)

    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    serializer = WishlistSerializer(wishlist_item)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_wishlist(request):

    wishlist = Wishlist.objects.filter(user=request.user)

    serializer = WishlistSerializer(wishlist, many=True)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_wishlist(request, id):

    try:
        wishlist = Wishlist.objects.get(
            user=request.user,
            product_id=id
        )

    except Wishlist.DoesNotExist:
        return Response(
            {"error": "Item not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    wishlist.delete()

    return Response(
        {"message": "Removed successfully"},
        status=status.HTTP_200_OK
    )