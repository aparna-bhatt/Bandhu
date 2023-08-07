from typing import Any
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from rest_framework.renderers import JSONRenderer

from .models import HomePage

from products.models import Product, ProductDetail
# Create your views here.


class ProductsViewSet(TemplateView):
    template_name = 'products.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        query_set = Product.objects.all()
        return render(request, 'products.html', {
            "data": query_set,
            "content": HomePage.objects.all().first()
        })


class ProductViewSet(TemplateView):
    template_name = 'product.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        id=self.kwargs.get('id')
        query_set = get_object_or_404(Product,id=id)
        details = ProductDetail.objects.filter(product=id)
        json_data = [{'detail': detail.detail} for detail in details]
        print(json_data )
        return render(request, 'product.html', {
            "data": query_set,
            "content": HomePage.objects.all().first(),
            "details":json_data
        })

