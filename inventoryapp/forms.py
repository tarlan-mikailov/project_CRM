from django import forms
from inventoryapp import models

class ComodityForm(forms.ModelForm):
    class Meta:
        model = models.Commodity
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'price': forms.NumberInput(attrs={"class": "form-control"}),
            'amount': forms.NumberInput(attrs={"class": "form-control"}),
        }


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['discount'].required = False

    class Meta:
        model = models.Order
        fields = '__all__'

        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local', "class": "form-control"}),
            'id_commodity': forms.Select(attrs={"class": "form-select"}),
            'id_employee': forms.Select(attrs={"class": "form-select"}),
            'amount': forms.NumberInput(attrs={"class": "form-control", "placeholder": "amount"}),
            'discount': forms.NumberInput(attrs={"class": "form-control", "placeholder": "discount"}),
        }


orderFormSet = forms.modelformset_factory(
    models.Order, form=OrderForm, extra=1
)