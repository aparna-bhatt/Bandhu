from django.urls import path
from django.conf import settings
from .views import ProductsViewSet, ProductViewSet

urlpatterns = [
    path('', ProductsViewSet.as_view()),
    path('<int:id>', ProductViewSet.as_view())
]
