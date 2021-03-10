from django import forms


class StylishForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'wpcf7-form-control'})
            field.error_messages = {'required':'Ce champs est obligatoire', 'invalid':"Entrez une adresse email valide" }
           

class ContactForm(StylishForm):

    name = forms.CharField(max_length=30, label=False, widget= forms.TextInput
                           (attrs={'placeholder':'NOM'}))
    company = forms.CharField(max_length=30, label=False, widget= forms.TextInput
                           (attrs={'placeholder':'SOCIETE'}))
    email = forms.EmailField(max_length=254, label=False, widget= forms.EmailInput
                           (attrs={'placeholder':'EMAIL'}))
    message = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={'rows': 4,'placeholder':'VOTRE MESSAGE'}))
    
    