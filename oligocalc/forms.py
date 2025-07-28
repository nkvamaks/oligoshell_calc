from django import forms
# from django.conf import settings
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from allauth.account.forms import SignupForm, LoginForm
#from django_recaptcha.fields import ReCaptchaField
#from django_recaptcha.widgets import ReCaptchaV2Checkbox

from . import models
from . import validators


class CalcForm(forms.ModelForm):
    STYLE_CHOICES = [('dna', 'DNA'), ('rna', 'RNA'), ('mix', 'Therapeutic')]
    PARAM_CHOICES = [('Default', 'Default'), ('qPCR', 'qPCR')]

    btnradio = forms.ChoiceField(widget=forms.RadioSelect,
                                 choices=STYLE_CHOICES,
                                 initial='dna')
    param_set = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select form-select-sm'}),
                                  choices=PARAM_CHOICES,
                                  initial='qPCR')

    def clean(self):
        if self.cleaned_data['btnradio'] == 'dna':
            seq_regex_validated = validators.validate_seq_dna_regex(self.cleaned_data['sequence'])
            seq_input_validated = validators.validate_seq_dna(seq_regex_validated)
            seq_modifications_validated = validators.validate_seq_mix(seq_input_validated)
        elif self.cleaned_data['btnradio'] == 'mix':
            validators.validate_seq_mix(self.cleaned_data['sequence'])
        elif self.cleaned_data['btnradio'] == 'rna':
            seq_regex_validated = validators.validate_seq_rna_regex(self.cleaned_data['sequence'])
            seq_input_validated = validators.validate_seq_rna(seq_regex_validated)
            seq_modifications_validated = validators.validate_seq_mix(seq_input_validated)
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
        widgets = {'sequence': forms.Textarea(attrs={'rows': 6,
                                                     'placeholder': 'Examples:\nDNA:  [VIC]CAAGAGGAAGAGAGAGACC[MGB-ECLIPSE]\nRNA: GUGCGAAGGGACGGUGCGGAGAGGAGAGCAC[GALNAC3-ALN]\nTherapeutic:  +A * +G * +A * dT * dT * dC * dA * dG * dT * dG * dT * dG * dG * +T * +G * dG\nTherapeutic (PMO):  morA # morC # morG # morT # morG # morC # morA',
                                                     'class': 'form-control'}),
                   'target': forms.Select(attrs={'class': 'form-select form-select-sm'}),
                   'absorbance260': forms.NumberInput(attrs={'placeholder': '0.135',
                                                             'class': 'form-control form-control-sm'}),
                   'volume': forms.NumberInput(attrs={'placeholder': '1.23',
                                                      'class': 'form-control form-control-sm'}),
                   'mv_conc': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
                   'dv_conc': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
                   'dntp_conc': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
                   'dna_conc': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
                   }


class ContactForm(forms.Form):
    subject = forms.CharField(required=False,
                              max_length=200,
                              widget=forms.TextInput(attrs={'placeholder': 'Describe your issue briefly',
                                                            'class': 'form-control'}))
    name = forms.CharField(required=False,
                           max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'John Doe',
                                                         'class': 'form-control'}))
    reply_to = forms.EmailField(required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'john.doe@example.com',
                                                              'class': 'form-control'}))
    message = forms.CharField(required=True,
                              widget=forms.Textarea(attrs={'rows': 4,
                                                           'placeholder': 'Enter your message here...',
                                                           'class': 'form-control'
                                                           }))
    #recaptcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


class TaqManFindForm(forms.ModelForm):
    def clean_fasta(self):
        return validators.validate_fasta(self.cleaned_data['fasta'])

    def clean_primer1(self):
        return validators.validate_primer1(self.cleaned_data['primer1'])

    def clean_primer2(self):
        return validators.validate_primer2(self.cleaned_data['primer2'])

    def clean_probe(self):
        return validators.validate_probe(self.cleaned_data['probe'])

    def clean_amp_size(self):
        return validators.validate_amp_size(self.cleaned_data['amp_size'])

    class Meta:
        model = models.TaqManFind
        fields = '__all__'
        widgets = {'fasta': forms.Textarea(attrs={'rows': 7,
                                                  'placeholder': '>NM_001101.3 Homo sapiens actin beta (ACTB), mRNA\nACCGCCGAGACCGCGTCCGCCCCGCGAGCACAGAGCCTCGCCTTTGCCGATCCGCCGCCCGTCCACACCC\nGCCGCCAGCTCACCATGGATGATGATATCGCCGCGCTCGTCGTCGACAACGGCTCCGGCATGTGCAAGGC\nCGGCTTCGCGGGCGACGATGCCCCCCGGGCCGTCTTCCCCTCCATCGTGGGGCGCCCCAGGCACCAGGGC',
                                                  'class': 'form-control',
                                                  'id': 'output',
                                                  'style': 'font-family: monospace,monospace;'}),
                   'primer1': forms.NumberInput(attrs={'placeholder': '5432.1',
                                                       'class': 'form-control'}),
                   'primer2': forms.NumberInput(attrs={'placeholder': '6789.0',
                                                       'class': 'form-control'}),
                   'probe': forms.NumberInput(attrs={'placeholder': '7654.3',
                                                     'class': 'form-control'}),
                   'probe_dye': forms.Select(attrs={'class': 'form-select'}),
                   'amp_size': forms.NumberInput(attrs={'placeholder': '120',
                                                        'class': 'form-control'}),
                   }


class DeleteAccountForm(forms.Form):
    confirm_deletion = forms.BooleanField(required=True,
                                          label="I confirm my account deactivation",
                                          widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=150, label='First Name', required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John'}))
    last_name = forms.CharField(max_length=150, label='Last Name', required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doe'}))
    #recaptcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = '__all__'

    def save(self, request):
        user = super(SignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

    def signup(self, request, user):
        """ This function is required otherwise you will get an ImproperlyConfigured exception """
        pass


class CustomLoginForm(LoginForm):
    """
    A custom LoginForm that adds 'form-control' classes to fields,
    changes labels/attributes, or overrides certain methods if needed.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'john.doe@example.com',
        })
        self.fields['login'].label = "Email"
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '············',
        })
        self.fields['password'].label = "Password"

    def login(self, *args, **kwargs):
        return super().login(*args, **kwargs)


class SirnaScoreForm(forms.ModelForm):
    def clean_fasta(self):
        return validators.validate_fasta_RNA(self.cleaned_data['fasta'])

    class Meta:
        model = models.SirnaScore
        fields = '__all__'

        widgets = {'fasta': forms.Textarea(attrs={'rows': 5,
                                                  'placeholder': '>NM_001101.3 Homo sapiens actin beta (ACTB), mRNA\nACCGCCGAGACCGCGTCCGCCCCGCGAGCACAGAGCCTCGCCTTTGCCGATCCGCCGCCCGTCCACACCC\nGCCGCCAGCTCACCATGGATGATGATATCGCCGCGCTCGTCGTCGACAACGGCTCCGGCATGTGCAAGGC\nCGGCTTCGCGGGCGACGATGCCCCCCGGGCCGTCTTCCCCTCCATCGTGGGGCGCCCCAGGCACCAGGGC',
                                                  'class': 'form-control',
                                                  'id': 'output',
                                                  'style': 'font-family: monospace,monospace;'}),
                   }
