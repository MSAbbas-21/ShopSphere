from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


from django.core.paginator import Paginator

@api_view(['GET'])
def product_list(request):

    products = Product.objects.all()

    category = request.GET.get("category")

    if category:
        products = products.filter(category_id=category)

    paginator = Paginator(products, 10)

    page = request.GET.get("page")

    page_obj = paginator.get_page(page)

    serializer = ProductSerializer(page_obj, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, id):

    try:
        product = Product.objects.get(id=id)

    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProductSerializer(product)

    return Response(serializer.data)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_product(request):

    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_product(request, id):

    try:
        product = Product.objects.get(id=id)

    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProductSerializer(product, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product(request, id):

    try:
        product = Product.objects.get(id=id)

    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    product.delete()

    return Response(
        {"message": "Product deleted successfully"},
        status=status.HTTP_200_OK
    )     
@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def category_detail(request, id):

    try:
        category = Category.objects.get(id=id)

    except Category.DoesNotExist:
        return Response(
            {"error": "Category not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = CategorySerializer(category)

    return Response(serializer.data)
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_category(request):

    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_category(request, id):

    try:
        category = Category.objects.get(id=id)

    except Category.DoesNotExist:
        return Response(
            {"error": "Category not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = CategorySerializer(category, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_category(request, id):

    try:
        category = Category.objects.get(id=id)

    except Category.DoesNotExist:
        return Response(
            {"error": "Category not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    category.delete()

    return Response(
        {"message": "Category deleted successfully"},
        status=status.HTTP_200_OK
    )  
@api_view(['GET'])
def search_products(request):

    query = request.GET.get("q")

    products = Product.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query)
    )

    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)        
