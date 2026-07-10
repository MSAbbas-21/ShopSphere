from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
from cart.models import Cart
from .models import Order, OrderItem
import razorpay
from django.conf import settings

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout(request):

    # Get all cart items of the logged-in user
    cart_items = Cart.objects.filter(user=request.user)

    # If cart is empty, stop here
    if not cart_items.exists():
        return Response(
            {"error": "Your cart is empty"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Calculate the total bill
    total_price = 0

    for item in cart_items:
        total_price += item.product.price * item.quantity

    # Create the order
    order = Order.objects.create(
        user=request.user,
        total_price=total_price
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout(request):

    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items.exists():
        return Response(
            {"error": "Your cart is empty"},
            status=status.HTTP_400_BAD_REQUEST
        )

    total_price = 0

    for item in cart_items:
        total_price += item.product.price * item.quantity

    order = Order.objects.create(
        user=request.user,
        total_price=total_price
    )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    cart_items.delete()

    return Response(
        {
            "message": "Order placed successfully",
            "order_id": order.id
        },
        status=status.HTTP_201_CREATED
    )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_orders(request):

    orders = Order.objects.filter(user=request.user)

    serializer = OrderSerializer(orders, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def all_orders(request):

    orders = Order.objects.all()

    serializer = OrderSerializer(orders, many=True)

    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_order_status(request, id):

    try:
        order = Order.objects.get(id=id)

    except Order.DoesNotExist:
        return Response(
            {"error": "Order not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    order.status = request.data.get("status")
    order.save()

    serializer = OrderSerializer(order)

    return Response(serializer.data)        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_payment(request):

    amount = int(request.data.get("amount")) * 100

    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    payment = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": 1
    })

    return Response(payment)
