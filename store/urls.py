from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/',views.product_list ),
    path('products/<id>/',views.product_detail),
    path('collection/',views.collection_list),
    path('collections/<int:id>/',views.collection_detail),
]