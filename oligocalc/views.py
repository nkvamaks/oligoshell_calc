from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import forms
from . import utils
from . import tm


def calc_view(request):
    if request.method == "POST":
        form = forms.CalcForm(request.POST)
        sequence = ''
        concentration_molar = 0
        concentration_mass = 0
        odu260 = 0
        quantity = 0
        mass_monoisotopic = 0
        esi_series = []
        mass_fragments_array = []
        melting_t = -1

        if form.is_valid():
            btnradio = form.cleaned_data['btnradio']
            if btnradio == 'dna':
                sequence = utils.dna2mix(form.cleaned_data['sequence'])
            elif btnradio == 'mix':
                sequence = form.cleaned_data['sequence']

            sequence_dna = utils.mix2dna_wo_mod_phosph(utils.wo_phosph(sequence))
            sequence_dna_rev_compl = utils.rev_compl(sequence_dna)
            seq_wo_phosph_tup = utils.sequence_split(utils.wo_phosph(sequence))
            length = utils.get_length(sequence)
            volume = form.cleaned_data['volume']
            absorbance260 = form.cleaned_data['absorbance260']
            mv_conc = form.cleaned_data['mv_conc']
            dv_conc = form.cleaned_data['dv_conc']
            dntp_conc = form.cleaned_data['dntp_conc']
            dna_conc = form.cleaned_data['dna_conc']  # dna_conc - uM
            target = form.cleaned_data['target']
            epsilon260 = utils.get_extinction(sequence)
            gc_content = utils.gc_content(seq_wo_phosph_tup)
            brutto_formula = utils.get_formula(sequence)

            mass_average = utils.get_mass_avg(sequence)
            nmol_OD260 = round((1 / epsilon260) * 1e6, 2)
            ug_OD260 = round((1 / epsilon260) * mass_average * 1e3, 2)

            if not utils.contain_degenerate_nucleotide(sequence):
                mass_monoisotopic = utils.get_mass_monoisotopic(sequence)

            for z in range(1, length):
                esi_series_avg_dmt_off = round((mass_average - z * utils.mass_avg['H']) / z, 2)
                if not utils.contain_degenerate_nucleotide(sequence):
                    esi_series_mono_dmt_off = round((mass_monoisotopic - z * utils.mass_mono['H']) / z, 4)
                else:
                    esi_series_mono_dmt_off = None
                esi_series.append((z, esi_series_avg_dmt_off, esi_series_mono_dmt_off))

            if absorbance260:
                concentration_molar = round(absorbance260 / epsilon260 * 1000000, 2)
                concentration_mass = round(concentration_molar * mass_average / 1000, 2)

            if absorbance260 and volume:
                odu260 = round(absorbance260 * volume, 2)

            if concentration_molar and volume:
                quantity = round(concentration_molar * volume, 1)

            if not utils.contain_degenerate_nucleotide(sequence):
                a_esi, a_B_esi, b_esi, c_esi, d_esi, w_esi, x_esi, y_esi, z_esi = map(utils.get_ms_fragments_esi_series, utils.get_ms_fragments(sequence))

                for charge in range(1, length):
                    mass_fragments_array.append(
                        [
                            (d_esi[seq_ind][charge-1],
                             c_esi[seq_ind][charge-1],
                             b_esi[seq_ind][charge-1],
                             a_esi[seq_ind][charge-1],
                             a_B_esi[seq_ind][charge-1],
                             seq_wo_phosph_tup[seq_ind-1],
                             w_esi[seq_ind][charge-1],
                             x_esi[seq_ind][charge-1],
                             y_esi[seq_ind][charge-1],
                             z_esi[seq_ind][charge-1]) for seq_ind in range(1, length+1)
                        ]
                    )

            dna_mon = list(nt in utils.dna_nucleotides for nt in seq_wo_phosph_tup)
            if dna_mon and all(dna_mon):
                melting_t = tm.calc_tm(seq=sequence,
                                       target=target,
                                       dna_conc=dna_conc,
                                       mv_conc=mv_conc,
                                       dv_conc=dv_conc,
                                       dntp_conc=dntp_conc
                                       )

            return render(request, 'oligocalc/calculator.html', {
                'form': form,
                'mv_conc': mv_conc,
                'dv_conc': dv_conc,
                'dntp_conc': dntp_conc,
                'dna_conc': dna_conc,
                'sequence': sequence,
                'seq_wo_phosph_tup': seq_wo_phosph_tup,
                'sequence_dna': sequence_dna,
                'sequence_dna_rev_compl': sequence_dna_rev_compl,
                'volume': volume,
                'odu260': odu260,
                'epsilon260': epsilon260,
                'absorbance260': absorbance260,
                'length': length,
                'charge': range(1, length),
                'concentration_molar': concentration_molar,
                'concentration_mass': concentration_mass,
                'quantity': quantity,
                'mass_monoisotopic': mass_monoisotopic,
                'mass_average': mass_average,
                'esi_series': esi_series,
                'mass_fragments_array': mass_fragments_array,
                'melting_t': melting_t,
                'gc_content': int(gc_content * 100),
                'brutto_formula': brutto_formula,
                'nmol_OD260': nmol_OD260,
                'ug_OD260': ug_OD260,
                })

    else:
        form = forms.CalcForm()
    return render(request, 'oligocalc/calculator.html', {'form': form})


def about(request):
    with open(r'README.md', 'r') as fh:
        return render(request, 'oligocalc/about.html', {'about_osh_calc': ''.join(line for line in fh)})


def contact(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            reply_to = form.cleaned_data['reply_to']

            body = 'From:\t{}\nEmail:\t{}\nMessage:\t\t\n\n{}\n'.format(name, reply_to, message)

            email = EmailMessage(
                subject=subject,
                body=body,
                from_email='OligoShell App',
                to=[settings.EMAIL_HOST_USER, ],
                reply_to=[reply_to, ],
            )
            email.send()
            return HttpResponseRedirect(reverse('oligocalc:success'))

    else:
        form = forms.ContactForm()
    return render(request, 'oligocalc/contact.html', {"form": form})


def success(request):
    return render(request, 'oligocalc/successfully_sent.html')


def modifications(request):
    return render(request, 'oligocalc/modifications.html')