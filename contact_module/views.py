from django.shortcuts import render, redirect, reverse
from .forms import Contactusform, Contactmodels, ProfileForm
from .models import Contact, Profile_User
from django.views.generic.edit import FormView
from django.views import View
from django.views.generic import ListView


# Create your views here.

class ContactUsView(FormView):
    template_name = 'contact_module/contact_components.html'
    form_class = Contactmodels
    success_url = '/contact-us/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def store_profile(file):
    with open('temp/image.jpg', 'wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class ProfileUserView(View):

    def get(self, request):
        form = ProfileForm()
        return render(request, 'contact_module/profile_components.html', {'form': form})

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            pf = Profile_User(image=request.FILES['user_image'])
            pf.save()
            return redirect('profile-create-page')

        return render(request, 'contact_module/profile_components.html')


class ProfilesView(ListView):
    model = Profile_User
    template_name = "contact_module/profile_list_component.html"
    context_object_name = "profiles"









# def get(self, request):
#     contact_form = Contactmodels()
#     return render(request, 'contact_module/contact_components.html',
#                   {
#
#                       'contact_form': contact_form
#
#                   })
#
# def post(self, request):
#     # contact_form = Contactusform(request.POST)
#     contact_form = Contactmodels(request.POST)
#     if contact_form.is_valid():
#         # contact = Contact(
#         #     title=contact_form.cleaned_data.get("title"),
#         #     fullname=contact_form.cleaned_data.get("fullname"),
#         #     email=contact_form.cleaned_data.get("email"),
#         #     message=contact_form.cleaned_data.get("message"),
#         # )
#         contact_form.save()
#         return redirect('index-page')

# def contactus(request):
#     if request.method == 'POST':
#         # contact_form = Contactusform(request.POST)
#         contact_form = Contactmodels(request.POST)
#         if contact_form.is_valid():
#             # contact = Contact(
#             #     title=contact_form.cleaned_data.get("title"),
#             #     fullname=contact_form.cleaned_data.get("fullname"),
#             #     email=contact_form.cleaned_data.get("email"),
#             #     message=contact_form.cleaned_data.get("message"),
#             # )
#             contact_form.save()
#             return redirect('index-page')
#     else:
#
#         # contact_form = Contactmodels()
#         # return render(request, 'contact_module/contact_components.html',
#         #               {
#         #
#         #                   'contact_form': contact_form
#         #
#         #               })
