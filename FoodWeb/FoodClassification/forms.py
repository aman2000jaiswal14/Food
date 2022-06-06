from django import forms


class ImageForms(forms.Form):
    img = forms.ImageField()