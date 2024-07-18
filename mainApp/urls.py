from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryAPIView.as_view()),
    path('categories/<int:category_id>/details/', CategoryDetailsAPIView.as_view()),

    path('subCategories/', SubCategoryAPIView.as_view()),
    path('subCategories/<int:subCategory_id>/details/', SubCategoryDetailsAPIView.as_view()),

    path('products/', ProductAPIView.as_view()),
    path('product/<int:product_id>/details/', ProductDetailsAPIView.as_view())
]
