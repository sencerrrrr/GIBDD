from django import forms
from .models import User, Car, ContactHistory, Region, CarBrand, CarModel

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname', 'name', 'fatherName', 'dateOfBirth', 'role']
        widgets = {
            'dateOfBirth': forms.DateInput(attrs={'type': 'date'}),
        }

class CarForm(forms.ModelForm):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), label='Регион')

    class Meta:
        model = Car
        fields = ['uniq_number', 'brand', 'model', 'Owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model'].queryset = CarModel.objects.none()

        if 'brand' in self.data:
            try:
                brand_id = int(self.data.get('brand'))
                self.fields['model'].queryset = CarModel.objects.filter(brand_id=brand_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input, ignore and fallback to empty queryset
        elif self.instance.pk:
            self.fields['model'].queryset = self.instance.brand.carmodel_set.order_by('name')

class ContactHistoryForm(forms.ModelForm):
    class Meta:
        model = ContactHistory
        fields = ['uniq_number', 'owner', 'buyer', 'car', 'contract']
