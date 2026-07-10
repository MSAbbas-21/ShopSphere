from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Cart
from .serializers import CartSerializer
from products.models import Product
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_list(request):

    cart_items = Cart.objects.filter(user=request.user)

    serializer = CartSerializer(cart_items, many=True)

    return Response(serializer.data)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):

    product_id = request.data.get('product')
    quantity = request.data.get('quantity', 1)

    try:
        product = Product.objects.get(id=product_id)

    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={"quantity": quantity}
    )

    if not created:
        cart_item.quantity += int(quantity)
        cart_item.save()

    serializer = CartSerializer(cart_item)

    return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_list(request):

    cart_items = Cart.objects.filter(user=request.user)

    serializer = CartSerializer(cart_items, many=True)

    return Response(serializer.data)        

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_cart(request, id):

    try:
        cart_item = Cart.objects.get(id=id, user=request.user)

    except Cart.DoesNotExist:
        return Response(
            {"error": "Cart item not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    quantity = request.data.get("quantity")

    cart_item.quantity = quantity
    cart_item.save()

    serializer = CartSerializer(cart_item)

    return Response(serializer.data)    

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_cart(request, id):

    try:
        cart_item = Cart.objects.get(id=id, user=request.user)

    except Cart.DoesNotExist:
        return Response(
            {"error": "Cart item not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    cart_item.delete()

    return Response(
        {"message": "Item removed from cart"},
        status=status.HTTP_200_OK
    )    