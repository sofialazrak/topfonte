from django import forms
from .models import Order
from django.core.exceptions import ValidationError 


class StylishForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input-text'})
            field.error_messages = {'required':'Ce champs est obligatoire', 'invalid': 'Ce champs est non valide'}
    

class OrderCreateForm(StylishForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'company', 'email', 'phone',
         'address', 'city', 'postcode', 'country']
        widgets = {
            'first_name' : forms.TextInput(attrs={'placeholder': 'PRENOM *', 'class': 'input-text'}),
            'last_name' : forms.TextInput(attrs={'placeholder': 'NOM *', 'class': 'input-text'}),
            'company' : forms.TextInput(attrs={'placeholder': 'SOCIETE *', 'class': 'input-text'}),
            'email' : forms.TextInput(attrs={'placeholder': 'EMAIL *', 'class': 'input-text', }),
            'phone' : forms.TextInput(attrs={'placeholder': 'TELEPHONE/GSM *', 'class': 'input-text',}),
            'address' : forms.TextInput(attrs={'placeholder': 'ADRESSE *', 'class': 'input-text'}),
            'city' : forms.TextInput(attrs={'placeholder': 'VILLE *', 'class': 'input-text'}),
            'postcode' : forms.TextInput(attrs={'placeholder': 'CODE POSTAL *', 'class': 'input-text'}),
            'country' : forms.TextInput(attrs={'placeholder': 'PAYS *', 'class': 'input-text'}),
        }
        
        