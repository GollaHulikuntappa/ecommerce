from django import forms
from shop.customer import Customer


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"

