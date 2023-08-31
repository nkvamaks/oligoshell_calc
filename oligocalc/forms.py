from django import forms

from . import models
from . import validators


class CalcForm(forms.ModelForm):
    CHOICES = [('dna', 'DNA'), ('mix', 'Therapeutic')]
    input_style = forms.ChoiceField(widget=forms.RadioSelect,
                                    choices=CHOICES,
                                    initial='dna')

    def clean(self):
        super().clean()
        if self.cleaned_data['input_style'] == 'dna':
            seq_regex_validated = validators.validate_seq_dna_regex(self.cleaned_data['sequence'])
            seq_input_validated = validators.validate_seq_dna(seq_regex_validated)
            seq_modifications_validated = validators.validate_seq_mix(seq_input_validated)
        elif self.cleaned_data['input_style'] == 'mix':
            validators.validate_seq_mix(self.cleaned_data['sequence'])
        else:
            raise forms.ValidationError('Something went wrong...')

    class Meta:
        model = models.Sequence
        fields = ('sequence', 'absorbance260', 'dilution_factor', 'volume')
        widgets = {'sequence': forms.Textarea(attrs={'rows': 4,
                                                     'placeholder': 'DNA style:    [FAM]AC*TGKCGATTA[+Cm]GCC*G[BHQ1]\n\nTherapeutic style:    +T * +A * +G dA dT dC dT rG rC rA rC moeCm * moeT * GALNAC3-ALN',
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
