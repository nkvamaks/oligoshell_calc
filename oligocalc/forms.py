from django import forms
from . import models
from . import validators


class CalcForm(forms.ModelForm):
    STYLE_CHOICES = [('dna', 'DNA'), ('mix', 'Therapeutic')]
    PARAM_CHOICES = [('Default', 'Default'), ('qPCR', 'qPCR')]

    btnradio = forms.ChoiceField(widget=forms.RadioSelect,
                                 choices=STYLE_CHOICES,
                                 initial='dna')
    param_set = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select form-select-sm'}),
                                  choices=PARAM_CHOICES,
                                  initial='Default')

    def clean(self):
        if self.cleaned_data['btnradio'] == 'dna':
            seq_regex_validated = validators.validate_seq_dna_regex(self.cleaned_data['sequence'])
            seq_input_validated = validators.validate_seq_dna(seq_regex_validated)
            seq_modifications_validated = validators.validate_seq_mix(seq_input_validated)
        elif self.cleaned_data['btnradio'] == 'mix':
            validators.validate_seq_mix(self.cleaned_data['sequence'])
        else:
            raise forms.ValidationError('Something went wrong...')

        validators.validate_dna_conc(self.cleaned_data['dna_conc'])
        validators.validate_mv_conc(self.cleaned_data['mv_conc'])
        validators.validate_dv_conc(self.cleaned_data['dv_conc'])
        validators.validate_dntp_conc(self.cleaned_data['dntp_conc'], self.cleaned_data['dv_conc'])

    class Meta:
        model = models.Oligo
        fields = ('sequence', 'target', 'absorbance260', 'volume',
                  'mv_conc', 'dv_conc', 'dntp_conc', 'dna_conc',)
        widgets = {'sequence': forms.Textarea(attrs={'rows': 5,
                                                     'placeholder': 'DNA style:  [VIC]CAAGAGGAAGAGAGAGACC[MGB-ECLIPSE]\n\nTherapeutic style:  +A * +G * +A * dT * dT * dC * dA * dG * dT * dG * dT * dG * dG * +T * +G * dG',
                                                     'class': 'form-control'}),
                   'target': forms.Select(attrs={'class': 'form-select form-select-sm'}),
                   'absorbance260': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
                   'volume': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
                   'mv_conc': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
                   'dv_conc': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
                   'dntp_conc': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
                   'dna_conc': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
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


