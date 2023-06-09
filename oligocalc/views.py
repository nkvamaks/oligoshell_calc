from django.shortcuts import render

from . import forms
from . import utils


def calc_view(request):
    form = forms.CalcForm(request.POST or None)
    sequence = ''
    length = 0
    epsilon260 = 0
    absorbance260 = 0
    dilution_factor = 0
    concentration_molar = 0
    concentration_mass = 0
    volume = 0
    odu260 = 0
    quantity = 0
    mass_monoisotopic = 0
    mass_monoisotopic_dmt_on = 0
    mass_average = 0
    mass_average_dmt_on = 0
    esi_series = []
    seq_wo_phosph_tup = ()
    mass_fragments_array = []

    if form.is_valid():
        sequence = form.cleaned_data['sequence']
        volume = form.cleaned_data['volume']
        absorbance260 = form.cleaned_data['absorbance260']
        dilution_factor = form.cleaned_data['dilution_factor']
        length = utils.get_length(sequence)
        epsilon260 = utils.get_extinction(sequence)
        if not utils.contain_degenerate_nucleotide(sequence):
            mass_monoisotopic = utils.get_mass_monoisotopic(sequence)
            mass_monoisotopic_dmt_on = round(mass_monoisotopic + utils.mass_mono['DMT'] - utils.mass_mono['H'], 4)
        mass_average = utils.get_mass_avg(sequence)
        mass_average_dmt_on = round(mass_average + utils.mass_avg['DMT'] - utils.mass_avg['H'], 2)

        for z in range(1, length):
            esi_series_avg_dmt_off = round((mass_average - z * utils.mass_avg['H']) / z, 2)
            esi_series_avg_dmt_on = round((mass_average_dmt_on - z * utils.mass_avg['H']) / z, 2)
            if not utils.contain_degenerate_nucleotide(sequence):
                esi_series_mono_dmt_off = round((mass_monoisotopic - z * utils.mass_mono['H']) / z, 4)
                esi_series_mono_dmt_on = round((mass_monoisotopic_dmt_on - z * utils.mass_mono['H']) / z, 4)
            else:
                esi_series_mono_dmt_off = None
                esi_series_mono_dmt_on = None
            esi_series.append((z, esi_series_avg_dmt_off, esi_series_avg_dmt_on, esi_series_mono_dmt_off, esi_series_mono_dmt_on))

        if absorbance260 and dilution_factor:
            concentration_molar = round(absorbance260 * dilution_factor / epsilon260 * 1000000, 2)
            concentration_mass = round(concentration_molar * mass_average / 1000, 2)

        if absorbance260 and dilution_factor and volume:
            odu260 = round(absorbance260 * dilution_factor * volume, 2)

        if concentration_molar and volume:
            quantity = round(concentration_molar * volume, 1)

        if not utils.contain_degenerate_nucleotide(sequence):
            seq_wo_phosph_tup = utils.sequence_split(utils.sequence_explicit(sequence))[::2]
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

    return render(request, 'oligocalc/calculator.html', {
        'form': form,
        'sequence': sequence,
        'length': length,
        'charge': range(1, length),
        'epsilon260': epsilon260,
        'absorbance260': absorbance260,
        'dilution_factor': dilution_factor,
        'concentration_molar': concentration_molar,
        'concentration_mass': concentration_mass,
        'volume': volume,
        'odu260': odu260,
        'quantity': quantity,
        'mass_monoisotopic': mass_monoisotopic,
        'mass_average': mass_average,
        'mass_monoisotopic_dmt_on': mass_monoisotopic_dmt_on,
        'mass_average_dmt_on': mass_average_dmt_on,
        'esi_series': esi_series,
        'seq_wo_phosph_tup': seq_wo_phosph_tup,
        'mass_fragments_array': mass_fragments_array,

    })

def about(request):
    return render(request, 'oligocalc/about.html')
