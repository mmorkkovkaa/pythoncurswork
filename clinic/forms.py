from django import forms
from .models import Help

class AddForm(forms.ModelForm):

    class Meta:
        model = Help
        fields = ('name', 'email')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
        }