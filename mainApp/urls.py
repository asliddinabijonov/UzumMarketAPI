from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryAPIView.as_view()),
    path('categories/<int:category_id>/', CategoryDetailsAPIView.as_view()),

    path('subCategories/', SubCategoryAPIView.as_view()),
    path('subCategories/<int:subCategory_id>/', SubCategoryDetailsAPIView.as_view()),

    path('products/', ProductAPIView.as_view()),
]
