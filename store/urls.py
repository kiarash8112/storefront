from django.urls import path
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register(prefix="products", viewset=views.ProductViewSet)
router.register(prefix="collections", viewset=views.CollectionViewSet)
router.register(prefix="carts", viewset=views.CartViewSet)

products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')

products_router.register('reviews', views.ReviewViewSet,
                         basename='product-reviews')
# URLConf
urlpatterns = router.urls + products_router.urls
