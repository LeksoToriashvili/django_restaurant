from django.urls import include, path
from rest_framework import routers

from rest import views

router = routers.DefaultRouter()
router.register(r'register', views.RegisterViewSet, basename='register')
router.register(r'restaurants', views.RestaurantViewSet, basename='restaurant')
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'subcategories', views.SubCategoryViewSet, basename='subcategory')
router.register(r'dishes', views.DishViewSet, basename='dish')


urlpatterns = [
    path('', include(router.urls)),
]
