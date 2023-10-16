from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Product,Collection
from .serializer import ProductSerializer,CollectionSerializer


class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializer


 
class ProductDetails(RetrieveUpdateDestroyAPIView):
        queryset =Product.objects.all()
        serializer_class = ProductSerializer
         
        def delete(self,request,pk):
            product =  get_object_or_404(Product,pk=pk)
            if product.orderitem_set.count() > 0:
                 return Response( status=status.HTTP_405_METHOD_NOT_ALLOWED)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
class CollectionList(ListCreateAPIView): 
    queryset = Collection.objects.annotate(products_count=Count('featured_product')).all()
    serializer_class = CollectionSerializer

class CollectionDetails(RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.annotate(products_count=Count('featured_product')).all()
    serializer_class = CollectionSerializer
    def delete(self,request,pk):
        collection = get_object_or_404(
        Collection.objects.annotate(
        products_count=Count('featured_product')), pk=id)
        if collection.featured_product.count() > 0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
