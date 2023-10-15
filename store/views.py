from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Product,Collection
from .serializer import ProductSerializer,CollectionSerializer


class ProductList(APIView):
    def get(self,request):
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(queryset,many = True)
        return Response(serializer.data)
    def put(self,request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save( )
        return Response(serializer.data,status=status.HTTP_201_CREATED)

 
class ProductDetails(APIView):
        def get(self,request):
            product =  get_object_or_404(Product,pk=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        def put(self,request):
            product =  get_object_or_404(Product,pk=id)
            serializer = ProductSerializer(product,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        def delete(self,request):
            product =  get_object_or_404(Product,pk=id)
            if product.orderitem_set.count() > 0:
                 return Response( status=status.HTTP_405_METHOD_NOT_ALLOWED)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
class CollectionList(APIView):
    def get(self,request):
        queryset = Collection.objects.annotate(products_count=Count('featured_product')).all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class CollectionDetails(APIView):
   
    def get(self,request):
        collection = get_object_or_404(
        Collection.objects.annotate(
        products_count=Count('featured_product')), pk=id)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    def put(self,request):
        collection = get_object_or_404(
        Collection.objects.annotate(
        products_count=Count('featured_product')), pk=id)
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request):
        collection = get_object_or_404(
        Collection.objects.annotate(
        products_count=Count('featured_product')), pk=id)
        if collection.featured_product.count() > 0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
