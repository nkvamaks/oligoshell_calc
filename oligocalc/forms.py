from django import forms

from . import models


class CalcForm(forms.ModelForm):
    class Meta:
        model = models.Sequence
        fields = ('sequence', 'absorbance260', 'dilution_factor', 'volume')
        widgets = {'sequence': forms.Textarea(attrs={'rows': 3,
                                                     'placeholder': '+T * +A * +G dA dT dC dT rG rC rA rC moeG * moeCm * moeT',
                                                     'class': 'form-control'}),
                   'absorbance260': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
                   'dilution_factor': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
                   'volume': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
                   }
