from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home_module/index-page.html'


# class HomeView(View):
#     @staticmethod
#     def get(request):
#
#         return render(request, 'home_module/index-page.html')


def site_header_partial(request):
    return render(request, 'shared/site_header_partial.html')


def site_footer_partial(request):
    return render(request, 'shared/site_footer_partial.html')
