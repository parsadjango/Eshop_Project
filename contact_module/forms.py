from django import forms
from .models import Contact



class Contactusform(forms.Form):
    fullname = forms.CharField(label='نام و نام خانوادگی',
                               max_length=50,
                               error_messages={
                                   'required': 'نام و نام خانوادگی را لطفا وارد کنید',

                               }, widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    subject = forms.CharField(label='عنوان', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    message = forms.CharField(label='پیام', widget=forms.Textarea, )


class Contactmodels(forms.ModelForm):
    class Meta:
        model = Contact
        # if you want to costumize Forms
        fields = ['fullname', 'email', 'title', 'message']
        # all Forms
        # fields = '__all__'
        # expect this one !
        # exclude = ['response']
        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'id': 'message'
            })
        }

        labels = {
            'fullname': 'نام و نام خانوادگی شما',
            'email': 'ایمیل شما',
            'message': 'پیام شمای',
            'title': 'عنوان'
        }

        error_messages = {
            'fullname': {
                'required': 'نام و نام خانوادگی اجباری می باشد. لطفا وارد کنید'
            }
        }


class ProfileForm(forms.Form):
    user_image = forms.ImageField()