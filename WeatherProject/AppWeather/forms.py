from django.forms import ModelForm , TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['city','is_favorite']
        widgets = {'city' : TextInput(attrs={'class':' input form-control form-control-lg','placeholder':"Search any City",'style': 'text-transform:capitalize;'})}

    # def __init__(self, *args, **kwargs):
    #     super(CityForm, self).__init__(*args, **kwargs)
    #     self.fields['is_favorite'].initial = False

    def clean_city(self):
        new_city=self.cleaned_data['city'].capitalize()
        return new_city