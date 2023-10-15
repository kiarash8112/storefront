from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/',views.ProductList.as_view()),
    path('products/<id>/',views.ProductDetails.as_view()),
    path('collection/',views.CollectionList.as_view()),
    path('collection/<int:pk>/',views.CollectionDetails.as_view()),
]