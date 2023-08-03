from django import forms

from . import models


class CalcForm(forms.ModelForm):
    class Meta:
        model = models.Sequence
        fields = ('sequence', 'absorbance260', 'dilution_factor', 'volume')
        widgets = {'sequence': forms.Textarea(attrs={'rows': 4,
                                                     'placeholder': '+T * +A * +G dA dT dC dT rG rC rA rC moeG * moeCm * moeT',
                                                     'class': 'form-control'}),
                   'absorbance260': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
                   'dilution_factor': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
                   'volume': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
                   }


class ContactForm(forms.Form):
    subject = forms.CharField(required=False,
                              max_length=200,
                              widget=forms.TextInput(attrs={'placeholder': 'Subject',
                                                            'class': 'form-control'}))
    name = forms.CharField(required=False,
                           max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Your Name',
                                                         'class': 'form-control'}))
    reply_to = forms.EmailField(required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Your Email',
                                                              'class': 'form-control'}))
    message = forms.CharField(required=True,
                              widget=forms.Textarea(attrs={'rows': 4,
                                                           'placeholder': 'Your message (Required)',
                                                           'class': 'form-control'
                                                           }))
