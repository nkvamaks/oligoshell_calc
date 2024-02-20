import math
from . import utils

R = 1.987  # universal gas constant in Cal/degrees C*Mol
T0 = 273.15

# DNA/DNA parameters set
# Dict contains pairs of dH and dS
# NN pairs are in 5'-NN-3' direction
# H. T. Allawi, J. Santalucia (1997), Biochemistry 36 (34): 10581-10594
# DOI: 10.1021/bi962590c
DNA_DNA_all97 = {
    'c0NaCl': 1,
    'init': {'dH': 0, 'dS': 0}, 'init_A/T': {'dH': 2.3, 'dS': 4.1}, 'init_G/C': {'dH': 0.1, 'dS': -2.8},
    'sym': {'dH': 0, 'dS': -1.4},
    'AA': {'dH': -7.9, 'dS': -22.2}, 'TT': {'dH': -7.9, 'dS': -22.2},
    'AT': {'dH': -7.2, 'dS': -20.4},
    'TA': {'dH': -7.2, 'dS': -21.3},
    'CA': {'dH': -8.5, 'dS': -22.7}, 'TG': {'dH': -8.5, 'dS': -22.7},
    'GT': {'dH': -8.4, 'dS': -22.4}, 'AC': {'dH': -8.4, 'dS': -22.4},
    'CT': {'dH': -7.8, 'dS': -21.0}, 'AG': {'dH': -7.8, 'dS': -21.0},
    'GA': {'dH': -8.2, 'dS': -22.2}, 'TC': {'dH': -8.2, 'dS': -22.2},
    'CG': {'dH': -10.6, 'dS': -27.2},
    'GC': {'dH': -9.8, 'dS': -24.4},
    'GG': {'dH': -8.0, 'dS': -19.9}, 'CC': {'dH': -8.0, 'dS': -19.9}
}


def fr_GC(sequence):
    """
    Takes a cleared sequence in 'DNA' style format and returns fraction of GC content
    """
    return (sequence.count('G') + sequence.count('C')) / len(sequence)


def self_complement(sequence):
    """
    Takes a cleared sequence in 'DNA' style format and returns True if sequence is self-complementary
    otherwise returns False
    """
    if sequence == utils.rev_compl(sequence):
        return True
    else:
        return False


def calc_dH_dS(sequence, nn_set):
    """
    Takes a cleared sequence in 'DNA' style format and returns calculated dH and dS values according to
    thermodynamic nearest neighbours parameters set
    """
    delta_h = 0
    delta_s = 0

    # Initiation values
    delta_h += nn_set['init']['dH']
    delta_s += nn_set['init']['dS']

    # Values for G/C or A/T terminal basepairs
    ends = sequence[0] + sequence[-1]
    a_t = ends.count('A') + ends.count('T')
    g_c = ends.count('G') + ends.count('C')
    delta_h += nn_set['init_A/T']['dH'] * a_t
    delta_s += nn_set['init_A/T']['dS'] * a_t
    delta_h += nn_set['init_G/C']['dH'] * g_c
    delta_s += nn_set['init_G/C']['dS'] * g_c

    # If sequence is self-complementary, apply symmetry
    if self_complement(sequence):
        delta_h += nn_set['sym']['dH']
        delta_s += nn_set['sym']['dS']

    # NN calculations
    for nt_index in range(len(sequence) - 1):
        nt_pair = sequence[nt_index:nt_index + 2]
        delta_h += nn_set[nt_pair]['dH']
        delta_s += nn_set[nt_pair]['dS']

    return delta_h, delta_s


def calc_tm_perfect_match(delta_h, delta_s, na_conc, self_compl):
    """
    Takes dH, dS and nucleic acid concentration and returns calculated melting temperature in Kelvin
    """
    factor = 1 if self_compl is True else 4

    # Melting temperature
    return (delta_h * 1000) / (delta_s + R * math.log(na_conc / (factor * 1e6)))  # in Kelvin


def calc_tm_salt_corr_owc08_eq16(Tm1, dv_conc, fr_GC, Nbp):
    """
    Takes Tm1 and concentration of divalent salt and returns calculated
    corrected melting temperature in Kelvin according to
    Owczarzy et al., Biochemistry 2008, 47 (19), 5336–5353
    doi.org/10.1021/bi702363u
    equation 16
    """
    return 1 / ((1 / Tm1) + 3.92e-5 - 9.11e-6 * math.log(dv_conc * 1e-3) + fr_GC * (6.26e-5 + 1.42e-5 * math.log(dv_conc * 1e-3)) + (-4.82e-4 + 5.25e-4 * math.log(dv_conc * 1e-3) + 8.31e-5 * (math.log(dv_conc * 1e-3)) ** 2) / (2 * (Nbp - 1)))


def calc_tm_salt_corr_owc08_eq16_18_20(Tm1, mv_conc, dv_conc, fr_GC, Nbp):
    """
    Takes Tm1 and concentrations of mono- and divalent salts and returns calculated
    corrected melting temperature in Kelvin according to
    Owczarzy et al., Biochemistry 2008, 47 (19), 5336–5353
    doi.org/10.1021/bi702363u
    equation 16 with parameters 18-20
    """
    param_a = 3.92e-5 * (0.843 - 0.352 * math.sqrt(mv_conc * 1e-3) * math.log(mv_conc * 1e-3))
    param_d = 1.42e-5 * (1.279 - 4.03e-3 * math.log(mv_conc * 1e-3) - 8.03e-3 * (math.log(mv_conc * 1e-3)) ** 2)
    param_g = 8.31e-5 * (0.486 - 0.258 * math.log(mv_conc * 1e-3) + 5.25e-3 * (math.log(mv_conc * 1e-3)) ** 3)
    return 1 / ((1 / Tm1) + param_a - 9.11e-6 * math.log(dv_conc * 1e-3) + fr_GC * (6.26e-5 + param_d * math.log(dv_conc * 1e-3)) + (-4.82e-4 + 5.25e-4 * math.log(dv_conc * 1e-3) + param_g * (math.log(dv_conc * 1e-3)) ** 2) / (2 * (Nbp - 1)))


def calc_effective_dv_owc08_eq17(dv_conc, dntp_conc):
    """
    Calculates effective concentration of Mg2+ ions in the presence of dNTPs.
    """
    Ka = 30000
    b = Ka * (dntp_conc - dv_conc) * 1e-3 + 1
    discr = b ** 2 + 4 * Ka * dv_conc * 1e-3
    return ((-b + math.sqrt(discr)) / (2 * Ka)) * 1e3


def calc_tm_salt_corr_owc04_eq22(Tm1, mv_conc, fr_GC, c0NaCl):
    """
    Takes Tm1 and concentration of monovalent salts and returns calculated
    corrected melting temperature in Kelvin according to
    Owczarzy et al., Biochemistry 2004, 43, 3537-3554
    doi 10.1021/bi034621r
    equation 22
    """
    return 1 / ((1 / Tm1) + (4.29 * fr_GC - 3.95) * 1e-5 * math.log(mv_conc / (c0NaCl * 1e3)) + 9.4 * 1e-6 * ((math.log(mv_conc / 1e3)) ** 2 - (math.log(c0NaCl)) ** 2))


def calc_tm_salt_corr(Tm1, mv_conc, dv_conc, dntp_conc, fr_GC, c0NaCl, Nbp):
    """
    Takes Tm1 and concentrations of mono-, divalent salts and dNTP, and returns calculated
    corrected melting temperature in Kelvin depending on salt composition
    Owczarzy et al., Biochemistry 2008, 47 (19), 5336–5353
    doi.org/10.1021/bi702363u
    """
    # Calculate effective concentration of Mg2+ if both Mg2+ and dNTPs are present, owc08_eq17
    if dv_conc and dntp_conc:
        dv_conc = calc_effective_dv_owc08_eq17(dv_conc=dv_conc, dntp_conc=dntp_conc)

    # Calculate ratio Mg^0.5/Na to decide about salt correction method
    ratio_dv_mv = math.sqrt(dv_conc * 1e-3) / (mv_conc * 1e-3)
    if ratio_dv_mv < 0.22:
        # Calculate according to owc04_eq22 (Na correction)
        melting_t_salt_corr_K = calc_tm_salt_corr_owc04_eq22(Tm1=Tm1, mv_conc=mv_conc, fr_GC=fr_GC, c0NaCl=c0NaCl)
    elif 0.22 <= ratio_dv_mv < 0.6:
        # Calculate according to owc08_eq16 with parameters 18-20 (Na/Mg correction)
        melting_t_salt_corr_K = calc_tm_salt_corr_owc08_eq16_18_20(Tm1=Tm1, mv_conc=mv_conc, dv_conc=dv_conc, fr_GC=fr_GC, Nbp=Nbp)
    else:
        # calculate accordind to owc08_eq16 (Mg correction)
        melting_t_salt_corr_K = calc_tm_salt_corr_owc08_eq16(Tm1=Tm1, dv_conc=dv_conc, fr_GC=fr_GC, Nbp=Nbp)
    return melting_t_salt_corr_K


def calc_tm(seq, target, dna_conc, mv_conc, dv_conc, dntp_conc):
    """
    Incoming values:
    seq: in 'Therapeutic format'
    target: nature of target NA (DNA, RNA, mRNA etc.)
    dna_conc: concentration of nucleic acid strand, uM
    mv_conc: concentration of mono-valent cations, mM
    dv_conc: concentration of di-valent cations, mM
    dntp_conc: concentration of dNTPs, mM
    """
    # Set initial values
    Nbp = utils.get_length(seq)
    nn_set = DNA_DNA_all97
    if target == 'dna':
        nn_set = DNA_DNA_all97

    # Convert 'Therapeutic' sequence to 'DNA' style. Remove modifications that cannot be used for
    # Tm calculations. Replace U to T.
    seq_dna = utils.mix2dna_wo_mod_degen_phosph(seq).replace('U', 'T')

    # Calculate dH and dS values
    delta_h, delta_s = calc_dH_dS(sequence=seq_dna, nn_set=nn_set)

    # Do not calculate Tm if sequence length is too short
    if len(seq_dna) < 6:
        return -1
    else:
        # Calculate melting temperature, in Kelvin
        melting_t_K = calc_tm_perfect_match(delta_h=delta_h,
                                            delta_s=delta_s,
                                            na_conc=dna_conc,
                                            self_compl=self_complement(seq_dna)
                                            )


        melting_t_salt_corr_K = calc_tm_salt_corr(Tm1=melting_t_K,
                                                  mv_conc=mv_conc,
                                                  dv_conc=dv_conc,
                                                  dntp_conc=dntp_conc,
                                                  fr_GC=fr_GC(seq_dna),
                                                  c0NaCl=nn_set['c0NaCl'],
                                                  Nbp=Nbp
                                                  )

        return round(melting_t_salt_corr_K - T0, 1)
