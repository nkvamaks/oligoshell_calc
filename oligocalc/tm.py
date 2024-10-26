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

# DNA/DNA parameters set
# NN pairs are in 5'-NN-3' direction
# J. SantaLucia, Jr. and D. Hicks. The thermodynamics of DNA structural motifs
# Annu Rev Biophys Biomol Struct 2004Vol. 33 P 415-440. DOI: 10.1146/annurev.biophys.32.110601.141800
DNA_DNA_san04 = {
    'c0NaCl': 1,
    'init': {'dH': 0.2, 'dS': -5.7}, 'init_A/T': {'dH': 2.2, 'dS': 6.9}, 'init_G/C': {'dH': 0, 'dS': 0},
    'sym': {'dH': 0, 'dS': -1.4},
    'AA': {'dH': -7.6, 'dS': -21.3}, 'TT': {'dH': -7.6, 'dS': -21.3},
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

# DNA/DNA parameters set
# NN pairs are in 5'-NN-3' direction
# N. Sugimoto, S. Nakano, M. Yoneyama and K. Honda. Improved thermodynamic parameters and helix initiation
# factor to predict stability of DNA duplexes
# Nucleic Acids Res 1996 Vol. 24 Issue 22 P 4501-4505. DOI: 10.1093/nar/24.22.4501
DNA_DNA_sug96 = {
    'c0NaCl': 1,
    'init': {'dH': 0.6, 'dS': -9.0}, 'init_A/T': {'dH': 0, 'dS': 0}, 'init_G/C': {'dH': 0, 'dS': 0},
    'sym': {'dH': 0, 'dS': -1.4},
    'AA': {'dH': -8.0, 'dS': -21.9}, 'TT': {'dH': -8.0, 'dS': -21.9},
    'AT': {'dH': -5.6, 'dS': -15.2},
    'TA': {'dH': -6.6, 'dS': -18.4},
    'CA': {'dH': -8.2, 'dS': -21.0}, 'TG': {'dH': -8.2, 'dS': -21.0},
    'GT': {'dH': -9.4, 'dS': -25.5}, 'AC': {'dH': -9.4, 'dS': -25.5},
    'CT': {'dH': -6.6, 'dS': -16.4}, 'AG': {'dH': -6.6, 'dS': -16.4},
    'GA': {'dH': -8.8, 'dS': -23.5}, 'TC': {'dH': -8.8, 'dS': -23.5},
    'CG': {'dH': -11.8, 'dS': -29.0},
    'GC': {'dH': -10.5, 'dS': -26.4},
    'GG': {'dH': -10.9, 'dS': -28.4}, 'CC': {'dH': -10.9, 'dS': -28.4}
}

# DNA/DNA parameters set
# NN pairs are in 5'-NN-3' direction.
# K. J. Breslauer, R. Frank, H. Blöcker and L. A. Marky. Predicting DNA duplex stability from the base sequence.
# Proceedings of the National Academy of Sciences 1986 Vol. 83 Issue 11 Pages 3746-3750. DOI: 10.1073/pnas.83.11.3746
DNA_DNA_bre86 = {
    'c0NaCl': 1,
    'init': {'dH': 0.0, 'dS': 0.0}, 'init_A/T': {'dH': 0, 'dS': 0}, 'init_G/C': {'dH': 0, 'dS': 0},
    'sym': {'dH': 0, 'dS': -1.3},
    'AA': {'dH': -9.1, 'dS': -24.0}, 'TT': {'dH': -9.1, 'dS': -24.0},
    'AT': {'dH': -8.6, 'dS': -23.9},
    'TA': {'dH': -6.0, 'dS': -16.9},
    'CA': {'dH': -5.8, 'dS': -12.9}, 'TG': {'dH': -5.8, 'dS': -12.9},
    'GT': {'dH': -6.5, 'dS': -17.3}, 'AC': {'dH': -6.5, 'dS': -17.3},
    'CT': {'dH': -7.8, 'dS': -20.8}, 'AG': {'dH': -7.8, 'dS': -20.8},
    'GA': {'dH': -5.6, 'dS': -13.5}, 'TC': {'dH': -5.6, 'dS': -13.5},
    'CG': {'dH': -11.9, 'dS': -27.8},
    'GC': {'dH': -11.1, 'dS': -26.7},
    'GG': {'dH': -11.0, 'dS': -26.6}, 'CC': {'dH': -11.0, 'dS': -26.6}
}

# RNA/RNA parameters set
# NN pairs are in 5'-NN-3' direction
# S M Freier, R Kierzek, J A Jaeger, N Sugimoto, M H Caruthers, T Neilson, and D H Turner.
# Improved free-energy parameters for predictions of RNA duplex stability.
# Proc Natl Acad Sci U S A. 1986 Dec; 83(24): 9373–9377. doi: 10.1073/pnas.83.24.9373
RNA_RNA_fre86 = {
    'c0NaCl': 1,
    'init': {'dH': 0, 'dS': -10.8}, 'init_A/T': {'dH': 0, 'dS': 0}, 'init_G/C': {'dH': 0, 'dS': 0},
    'sym': {'dH': 0, 'dS': -1.4},
    'AA': {'dH': -6.6, 'dS': -18.4}, 'UU': {'dH': -6.6, 'dS': -18.4},
    'AU': {'dH': -5.7, 'dS': -15.5},
    'UA': {'dH': -8.1, 'dS': -22.6},
    'CA': {'dH': -10.5, 'dS': -27.8}, 'UG': {'dH': -10.5, 'dS': -27.8},
    'GU': {'dH': -10.2, 'dS': -26.2}, 'AC': {'dH': -10.2, 'dS': -26.2},
    'CU': {'dH': -7.6, 'dS': -19.2}, 'AG': {'dH': -7.6, 'dS': -19.2},
    'GA': {'dH': -13.3, 'dS': -35.5}, 'UC': {'dH': -13.3, 'dS': -35.5},
    'CG': {'dH': -8.0, 'dS': -19.4},
    'GC': {'dH': -14.2, 'dS': -34.9},
    'GG': {'dH': -12.2, 'dS': -29.7}, 'CC': {'dH': -12.2, 'dS': -29.7}
}

# DNA/DNA parameters set
# NN pairs are in 5'-NN-3' direction
# Primer Express 3.0
DNA_DNA_pe3 = {
    #
    'init': {'dH': 0, 'dS': 0}, 'init_A/T': {'dH': 2.3, 'dS': 4.1}, 'init_G/C': {'dH': 0.1, 'dS': -2.8},
    'sym': {'dH': 0, 'dS': 0},
    'AA': {'dH': -7.9, 'dS': -22.2}, 'AC': {'dH': -8.4, 'dS': -22.4}, 'AG': {'dH': -7.8, 'dS': -21.0}, 'AT': {'dH': -7.2, 'dS': -20.4},
    'CA': {'dH': -8.5, 'dS': -22.7}, 'CC': {'dH': -8.0, 'dS': -19.9}, 'CG': {'dH': -10.6, 'dS': -27.2}, 'CT': {'dH': -7.8, 'dS': -21.0},
    'GA': {'dH': -8.2, 'dS': -22.2}, 'GC': {'dH': -9.8, 'dS': -24.4}, 'GG': {'dH': -8.0, 'dS': -19.9}, 'GT': {'dH': -8.4, 'dS': -22.4},
    'TA': {'dH': -7.2, 'dS': -21.3}, 'TC': {'dH': -8.2, 'dS': -22.2}, 'TG': {'dH': -8.5, 'dS': -22.7}, 'TT': {'dH': -7.9, 'dS': -22.2}
    }
DNA_DNA_pcr_pe3 = {
    # Parameters for Na=40mM and Mg=5mM, 'standard PCR' conditions
    'init': {'dH': 0, 'dS': 0}, 'init_A/T': {'dH': -1.05865748, 'dS': -7.0977}, 'init_G/C': {'dH': -5.431818926, 'dS': -19.002},
    'sym': {'dH': 0, 'dS': 0},
    'AA': {'dH': -7.848149736, 'dS': -22.251}, 'AC': {'dH': -8.454769827, 'dS': -22.652}, 'AG': {'dH': -6.389315578, 'dS': -17.274}, 'AT': {'dH': -8.184491174, 'dS': -22.988},
    'CA': {'dH': -7.530587908, 'dS': -20.343}, 'CC': {'dH': -7.8583913, 'dS': -20.071}, 'CG': {'dH': -8.083611101, 'dS': -20.68}, 'CT': {'dH': -6.389315578, 'dS': -17.274},
    'GA': {'dH': -8.715696056, 'dS': -23.959}, 'GC': {'dH': -8.954301519, 'dS': -22.041}, 'GG': {'dH': -7.8583913, 'dS': -20.071}, 'GT': {'dH': -8.454769827, 'dS': -22.652},
    'TA': {'dH': -7.231831033, 'dS': -21.767}, 'TC': {'dH': -8.715696056, 'dS': -23.959}, 'TG': {'dH': -7.530587908, 'dS': -20.343}, 'TT': {'dH': -7.848149736, 'dS': -22.251}
    }
# dS increment for MGB-modified oligos
mgb_delta_s_pcr_pe3 = {
    # Parameters for Na=40mM and Mg=5mM, 'standard PCR' conditions
    'AA': 3.407506222, 'AC': 1.441885745, 'AG': 0.664524726, 'AT': 3.060091908,
    'CA': 0.607476337, 'CC': 0.90513791, 'CG': -1.104146165, 'CT': 2.25315143,
    'GA': 2.542327963, 'GC': 1.819880026, 'GG': 1.288047464, 'GT': 2.004729958,
    'TA': 2.462867141, 'TC': 2.870499201, 'TG': -8.4998E-5, 'TT': 3.3130226
}
# Na and Mg temperature correction tables for oligos labeled with MGB
Ttable = [[-22.9, -22.9, -13.7, -4.9, -0.6, -0.1],
          [-17.3, -17.3, -11.7, -4.9, -0.3, 0.3],
          [-11.7, -11.7, -9.7, -4.9, 0.0, 0.7],
          [-3.2, -3.2, -3.2, -2.4, 0.3, 1.1],
          [1.1, 1.1, 1.1, 1.1, 1.3, 1.5],
          [4.7, 4.5, 4.3, 4.1, 4.1, 4.1],
          [9.6, 9.03, 8.56, 8.1, 7.83, 7.56]]
Tna = [0.0, 0.02, 0.04, 0.11, 0.21, 0.41, 1.0]
Tnalog = [0.0, -1.69897, -1.39794, -0.958607, -0.677781, -0.387216, 0.0]
Tmg = [0.0, 4e-5, 2e-4, 0.001, 0.005, 0.025]
Tmglog = [0.0, -4.39794, -3.69897, -3.0, -2.30103, -1.60206]


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
    if not sequence:
        return 0, 0
    else:
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


def rev_calc_tm_salt_corr_owc08_eq16(Tm2, dv_conc, fr_GC, Nbp):
    """
    Takes Tm2 (Mg corrected) and concentration of divalent salts and returns Tm1 (1M NaCl)
    melting temperature in Kelvin according to
    Owczarzy et al., Biochemistry 2008, 47 (19), 5336–5353
    doi.org/10.1021/bi702363u
    equation 16
    """
    return 1 / ((1 / Tm2) - 3.92e-5 + 9.11e-6 * math.log(dv_conc * 1e-3) - fr_GC * (6.26e-5 + 1.42e-5 * math.log(dv_conc * 1e-3)) - (-4.82e-4 + 5.25e-4 * math.log(dv_conc * 1e-3) + 8.31e-5 * (math.log(dv_conc * 1e-3)) ** 2) / (2 * (Nbp - 1)))


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


def rev_calc_tm_salt_corr_owc08_eq16_18_20(Tm2, mv_conc, dv_conc, fr_GC, Nbp):
    """
    Takes Tm2 (Na-Mg corrected) and concentrations of mono- and divalent salts and returns calculated Tm1 (1M NaCl)
    corrected melting temperature in Kelvin according to
    Owczarzy et al., Biochemistry 2008, 47 (19), 5336–5353
    doi.org/10.1021/bi702363u
    equation 16 with parameters 18-20
    """
    param_a = 3.92e-5 * (0.843 - 0.352 * math.sqrt(mv_conc * 1e-3) * math.log(mv_conc * 1e-3))
    param_d = 1.42e-5 * (1.279 - 4.03e-3 * math.log(mv_conc * 1e-3) - 8.03e-3 * (math.log(mv_conc * 1e-3)) ** 2)
    param_g = 8.31e-5 * (0.486 - 0.258 * math.log(mv_conc * 1e-3) + 5.25e-3 * (math.log(mv_conc * 1e-3)) ** 3)
    return 1 / ((1 / Tm2) - param_a + 9.11e-6 * math.log(dv_conc * 1e-3) - fr_GC * (6.26e-5 + param_d * math.log(dv_conc * 1e-3)) - (-4.82e-4 + 5.25e-4 * math.log(dv_conc * 1e-3) + param_g * (math.log(dv_conc * 1e-3)) ** 2) / (2 * (Nbp - 1)))


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


def rev_calc_tm_salt_corr_owc04_eq22(Tm2, mv_conc, fr_GC, c0NaCl):
    """
    Takes Tm1 and concentration of monovalent salts and returns calculated
    corrected melting temperature in Kelvin according to
    Owczarzy et al., Biochemistry 2004, 43, 3537-3554
    doi 10.1021/bi034621r
    equation 22
    """
    return 1 / ((1 / Tm2) - (4.29 * fr_GC - 3.95) * 1e-5 * math.log(mv_conc / (c0NaCl * 1e3)) - 9.4 * 1e-6 * ((math.log(mv_conc / 1e3)) ** 2 - (math.log(c0NaCl)) ** 2))


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


def calc_tm_salt_corr_mgb(Na, Mg):
    dna = 0
    dmg = 0
    Tmgdop = [0 for i in range(7)]
    Tnadop = [0 for i in range(7)]
    tempDop = 0
    Nalog = math.log10(Na)
    Mglog = math.log10(Mg)

    if Mg == 0.005 and Na == 0.04:
        return tempDop

    img = 0
    while img < 5 and Mg >= Tmg[img + 1]:
        img += 1

    ina = 0
    while ina < 6 and Na >= Tna[ina + 1]:
        ina += 1

    if ina == 6:
        for i in range(6):
            ad = (Ttable[6][i] - Ttable[5][i]) / (Tnalog[6] - Tnalog[5])
            bd = Ttable[6][i] - ad * Tnalog[6]
            Tnadop[i] = ad * Nalog + bd

    if img == 5:
        for i in range(7):
            ad = (Ttable[i][5] - Ttable[i][4]) / (Tmglog[5] - Tmglog[4])
            bd = Ttable[i][5] - ad * Tmglog[5]
            Tmgdop[i] = ad * Mglog + bd

    if ina == 6 and img == 5:
        ad = (Tnadop[5] - Tnadop[4]) / (Tmglog[5] - Tmglog[4])
        bd = Tnadop[5] - ad * Tmglog[5]
        tup = ad * Mglog + bd

        ad = (Tmgdop[6] - Tmgdop[5]) / (Tnalog[6] - Tnalog[5])
        bd = Tmgdop[6] - ad * Tnalog[6]
        tdown = ad * Nalog + bd

        tempDop = (tup + tdown) / 2.0

    if img != 5:
        if img == 0:
            dmg = Mg / Tmg[1]
        else:
            dmg = (Mglog - Tmglog[img]) / (Tmglog[img + 1] - Tmglog[img])

    if ina != 6:
        if ina == 0:
            dna = Na / Tna[1]
        else:
            dna = (Nalog - Tnalog[ina]) / (Tnalog[ina + 1] - Tnalog[ina])

    if ina != 6 and img != 5:
        tup = Ttable[ina][img] + dmg * (Ttable[ina][img + 1] - Ttable[ina][img])
        tdown = Ttable[ina + 1][img] + dmg * (Ttable[ina + 1][img + 1] - Ttable[ina + 1][img])
        tempDop = tup + dna * (tdown - tup)
    if img == 5 and ina != 6:
        tempDop = Tmgdop[ina] + dna * (Tmgdop[ina + 1] - Tmgdop[ina])
    if img != 5 and ina == 6:
        tempDop = Tnadop[img] + dmg * (Tnadop[img + 1] - Tnadop[img])
    return tempDop


def calc_tm_mgb(seq: str, dna_conc: float, mv_conc: float, dv_conc: float, dntp_conc: float) -> float:
    """
    Calculate the melting temperature of a sequence with MGB modifications.

    Parameters:
        seq (str): Sequence in 'Therapeutic format'.
        dna_conc (float): Concentration of nucleic acid strand in µM.
        mv_conc (float): Concentration of monovalent cations in mM.
        dv_conc (float): Concentration of divalent cations in mM.
        dntp_conc (float): Concentration of dNTPs in mM.

    Returns:
        float: Melting temperature in Celsius, or None if sequence length is too short.
    """
    # Convert 'Therapeutic' sequence to 'DNA' style
    seq_dna = utils.mix2dna_wo_mod_degen_phosph(seq).replace('U', 'T')

    if len(seq_dna) < 10:
        return -1

    # Adjust concentrations
    if dv_conc and dntp_conc:
        dv_conc = calc_effective_dv_owc08_eq17(dv_conc=dv_conc, dntp_conc=dntp_conc)
    mv_conc, dv_conc = mv_conc * 1e-3, dv_conc * 1e-3

    std_pcr, new_tab = 0, 0

    if mv_conc == 0.04 and dv_conc == 0.005:
        std_pcr, new_tab = 1, 1
    else:
        if dv_conc * 100 + 1.0E-14 > mv_conc:
            new_tab = 1
        dv_conc = max(dv_conc, 1.0E-14)
        mv_conc = max(mv_conc, 1.0E-14)
    corr_temp = calc_tm_salt_corr_mgb(mv_conc, dv_conc)

    nn_set = DNA_DNA_pe3 if not new_tab else DNA_DNA_pcr_pe3
    delta_h, delta_s = calc_dH_dS(sequence=seq_dna, nn_set=nn_set)

    def calculate_delta_s(sequence_dna, start_offset):
        delta_s_mgb = 0
        seq_rev = sequence_dna[::-1]
        for index in range(start_offset, start_offset + 5):
            pair = seq_rev[index:index + 2][::-1]
            delta_s_mgb += mgb_delta_s_pcr_pe3[pair]

        trinuc = 0
        if sequence_dna[-start_offset-7] == 'A':
            trinuc += 100
        if sequence_dna[-start_offset-6] == 'A':
            trinuc += 10
        if sequence_dna[-start_offset-5] == 'A':
            trinuc += 1

        wmax = {
            10: 1.787172519,
            100: 1.787172519,
            11: 1.787172519 + R * math.log(2.0),
            101: 1.787172519 + R * math.log(2.0),
            110: 1.787172519 + R * math.log(2.0),
            111: 1.787172519 + R * math.log(3.0)
        }.get(trinuc, 0.0)

        delta_s_mgb += wmax
        if sequence_dna[-3:] == 'CCC':
            delta_s_mgb += 3.0 if start_offset == 0 else 2.0

        return delta_s_mgb

    delta_s1 = calculate_delta_s(seq_dna, 0)
    delta_s2 = calculate_delta_s(seq_dna, 1)

    delta_s += max(delta_s1, delta_s2)

    log_term = R * math.log(dna_conc / (2 * 1e6))
    if std_pcr == 1:
        melting_t_c = (delta_h * 1000) / (delta_s + log_term) - T0 + 0.274
    elif new_tab == 0:
        melting_t_c = (delta_h * 1000) / (delta_s + log_term) - T0 + 15 * math.log10(mv_conc + 20 * dv_conc)
    else:
        melting_t_c = (delta_h * 1000) / (delta_s + log_term) - T0 + corr_temp

    return melting_t_c


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
    return melting_t_salt_corr_K - T0


def calculate_melting_temp(seq_wo_phosph_tup, sequence, target, dna_conc, mv_conc, dv_conc, dntp_conc):
    allowed_for_calc_tm_mgb = set(
        utils.dna_nucleotides + utils.modification_5_position + utils.modification_3_position)
    allowed_for_calc_tm = allowed_for_calc_tm_mgb - {'MGB', 'MGB-ECLIPSE'}

    dna_mon = all(nt in allowed_for_calc_tm for nt in seq_wo_phosph_tup)
    dna_mon_mgb = all(nt in allowed_for_calc_tm_mgb for nt in seq_wo_phosph_tup)

    if dna_mon:
        return calc_tm(seq=sequence, target=target, dna_conc=dna_conc, mv_conc=mv_conc, dv_conc=dv_conc,
                       dntp_conc=dntp_conc)
    elif dna_mon_mgb and ('MGB' in seq_wo_phosph_tup or 'MGB-ECLIPSE' in seq_wo_phosph_tup):
        return calc_tm_mgb(seq=sequence, dna_conc=dna_conc, mv_conc=mv_conc, dv_conc=dv_conc,
                           dntp_conc=dntp_conc)
    return -1
