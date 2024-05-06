from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductCategoryViewSet, ProductImageViewSet, ProductReviewViewSet, ProductVarientViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'product_categories', ProductCategoryViewSet)
router.register(r'product_images', ProductImageViewSet)
router.register(r'product_reviews', ProductReviewViewSet)
router.register(r'product_variants', ProductVarientViewSet)

urlpatterns = [

    path('', include(router.urls)),
]
