from django import forms
from clientapp import models


class ClientForm(forms.ModelForm):
    image = forms.ImageField(max_length=255, required=False, widget=forms.FileInput(attrs={"class": "form-control", "type": "file", "accept": "image/png, image/jpeg", "multiple": ""}))

    class Meta:
        model = models.Client
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'comment': forms.Textarea(attrs={"cols": 30, "rows": 3, "class": "form-control"}),
            'birthday': forms.DateTimeInput(attrs={'type': 'date', "class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'phone': forms.TextInput(attrs={"class": "form-control", "phone": "", "autocomplete": "off"}),# "pattern": "380\s[0-9]{2}\s[0-9]{3}-[0-9]{2}-[0-9]{2}"}),
        }


class ClientPhotoForm(forms.ModelForm):
    
    class Meta:
        model = models.ClientPhoto
        fields = '__all__'