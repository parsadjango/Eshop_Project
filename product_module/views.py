from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib import sessions


# from django.db.models import Avg , Min , Max

# Create your views here.


class ProductlistView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = "products"

    def get_queryset(self):
        base_query = super(ProductlistView, self).get_queryset()
        data = base_query.filter(is_active=True)
        return data


# def product_list(request):
#     product = Product.objects.all()
#     number_of_products = product.count()
#     return render(request, "product_module/product_list.html", {
#         "product": product,
#         "number_of_products": number_of_products,
#
#     })

class ProductDetailsView(DetailView):
    template_name = 'product_module/product_details.html'
    model = Product
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        loaded_product = self.object
        request = self.request
        fav_product_id = request.session.get('product_fav')
        context['is_favorite'] = fav_product_id == str(loaded_product.id)
        return context



class AddToFavView(View):
    def post(self, request):
        product_id = request.POST['product_id']
        product = Product.objects.get(pk=product_id)
        request.session['product_fav'] = product_id
        return redirect(product.get_absolute_url())

    #
    # def get_context_data(self, **kwargs):
    #     context = super(ProductDetailsView, self).get_context_data()
    #     slug = kwargs['slug']
    #     product = get_object_or_404(Product, slug=slug)
    #     context['product'] = product
    #     return context
# def product_details(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     return render(request, "product_module/product_details.html", {
#         "product": product
#     })
