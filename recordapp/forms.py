from django import forms
from django.core.exceptions import ValidationError

from recordapp.models import Record


time_choice = (
    ('9 AM', '9 AM'),
    ('10 AM', '10 AM'),
    ('11 AM', '11 AM'),
)


class RecordForm(forms.ModelForm):
    # time_slot = forms.ChoiceField(choices=time_choice,
    #                               widget=forms.Select(attrs={"class": "form-select", 'id': 'reservation_slot'}))

    class Meta:
        model = Record
        fields = '__all__'

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', "class": "form-control", 'id': 'reservation_date'}),
            'id_client': forms.Select(attrs={"class": "form-select"}),
            'id_staff': forms.Select(attrs={"class": "form-select"}),
            'id_service': forms.Select(attrs={"class": "form-select"}),
            'price': forms.NumberInput(attrs={"class": "form-control"}),
            # 'time_slot': forms.Select(attrs={"class": "form-control", 'id': 'reservation_slot'})
        }

    # def clean(self):
    #     super().clean()
    #     dates_from_bd = self.instance.objects.filter(date=self.data.get('date'))
    #     if dates_from_bd:
    #         for obj in dates_from_bd:
    #             if obj['time'] < self.data.get('time') < obj['time'] + obj['duration']:
    #                 raise ValidationError
