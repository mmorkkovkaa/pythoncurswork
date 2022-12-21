from django import forms
from .models import HelpU

class AddForm(forms.ModelForm):

    class Meta:
        model = HelpU
        fields = ('name', 'phone', 'description',)

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.NumberInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
        }