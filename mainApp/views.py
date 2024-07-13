from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *


class CategoryAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='title',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Search by Title',
            )
        ]
    )
    def get(self, request):
        categories = Category.objects.all()

        title_search = request.query_params.get('title')

        if title_search is not None:
            categories = categories.filter(title=title_search)

        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoryDetailsAPIView(APIView):

    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class SubCategoryAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='category',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Filter by Catigory id'
            ),
            openapi.Parameter(
                name='title',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Search by title'
            )
        ]
    )
    def get(self, request):
        subCategories = SubCategory.objects.all()
        categoty_filter = request.query_params.get('category', None)
        title_search = request.query_params.get('title')

        if categoty_filter is not None:
            subCategories = subCategories.filter(categoty__id=categoty_filter)

        if title_search is not None:
            subCategories = subCategories.filter(title=title_search)

        serializer = SubCategorySerializer(subCategories, many=True)
        return Response(serializer.data)


class SubCategoryDetailsAPIView(APIView):
    def get(self, request, subCategory_id):
        subCategory = get_object_or_404(SubCategory, id=subCategory_id)
        serializer = SubCategorySerializer(subCategory)
        return Response(serializer.data)


class ProductAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='category',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description='Filter by Category ID'
            ),
            openapi.Parameter(
                name='subCategory',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description='Filter by SubCategory ID'
            ),
            openapi.Parameter(
                name='name',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Search by Product name'
            ),
            openapi.Parameter(
                name='brend',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Search by brand'
            ),
            openapi.Parameter(
                name='min_price',
                in_=openapi.IN_QUERY,
                type=openapi.FORMAT_FLOAT,
                description='Filter by min price'
            ),
            openapi.Parameter(
                name='max_price',
                in_=openapi.IN_QUERY,
                type=openapi.FORMAT_FLOAT,
                description='Filter by max price'
            ),
            openapi.Parameter(
                name='order_by',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Order by price_min, price_max, discount, ordered, rating, created_at_first,' +
                            ' created_at_last ',
                enum=['price_min', 'price_max', 'discount', 'ordered', 'r   ating', 'created_at_first',
                      'created_at_last', ]
            ),
        ]
    )
    def get(self, request):
        products = Product.objects.all()

        subCategory_filter = request.query_params.get('subCategory', None)
        if subCategory_filter is not None:
            products = products.filter(subCategory_id=subCategory_filter)

        category_filter = request.query_params.get('category', None)
        if category_filter is not None:
            products = products.filter(subCategory__category_id=category_filter)

        name_search = request.query_params.get('name', None)
        if name_search is not None:
            products = products.filter(name__icontains=name_search)

        brand_search = request.query_params.get('brand', None)
        if brand_search is not None:
            products = products.filter(name__icontains=brand_search)

        min_price = request.query_params.get('min_price', None)
        if min_price is not None:
            products = products.filter(price__gte=min_price)

        max_price = request.query_params.get('max_price', None)
        if max_price is not None:
            products = products.filter(price__lte=max_price)

        order_by = request.query_params.get('order_by', None)
        if order_by is not None:
            if order_by == 'price_min':
                products = products.order_by('price')
            elif order_by == 'price_max':
                products = products.order_by('-price')
            elif order_by == 'discount':
                products = products.order_by('-discount')
            elif order_by == 'ordered':
                products = products.order_by('-ordered')
            elif order_by == 'rating':
                products = products.order_by('-rating')
            elif order_by == 'created_at_first':
                products = products.order_by('created_at')
            elif order_by == 'created_at_last':
                products = products.order_by('-created_at')

        serializer = ProdoctSerializer(products, many=True)
        return Response(serializer.data)
