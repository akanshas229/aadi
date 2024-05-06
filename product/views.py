from .serializers import ProductSerializer, ProductCategorySerializer, ProductImageSerializer,ProductReviewSerializer, ProductVariantSerializer, VendorProfileSerializer
from .models import ProductReview, Product, ProductCategory, ProductImage, ProductVariant
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]


class ProductVarientViewSet(viewsets.ModelViewSet):
    queryset = ProductVariant.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Product, ProductCategory, ProductImage, ProductReview, ProductVariant
# from .serializers import (
#     ProductSerializer, ProductCategorySerializer,
#     ProductImageSerializer, ProductReviewSerializer,
#     ProductVariantSerializer
# )

# class ProductListCreateAPIView(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProductDetailAPIView(APIView):
#     def get_object(self, pk):
#         try:
#             return Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, pk):
#         product = self.get_object(pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         product = self.get_object(pk)
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         product = self.get_object(pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ProductCategoryListCreateAPIView(APIView):
#     def get(self, request):
#         categories = ProductCategory.objects.all()
#         serializer = ProductCategorySerializer(categories, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProductCategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class ProductImageListCreateAPIView(APIView):
#     def get(self, request):
#         images = ProductImage.objects.all()
#         serializer = ProductImageSerializer(images, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProductImageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProductReviewListCreateAPIView(APIView):
#     def get(self, request):
#         reviews = ProductReview.objects.all()
#         serializer = ProductReviewSerializer(reviews, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProductReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProductVariantListCreateAPIView(APIView):
#     def get(self, request):
#         variants = ProductVariant.objects.all()
#         serializer = ProductVariantSerializer(variants, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProductVariantSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    