#Monoisotopic and average masses of elements and some molecules
mass_mono = {
    'H': 1.007825035, 'Li': 7.016003, 'B': 11.0093055, 'C': 12, 'N': 14.003074, 'O': 15.99491463,
    'F': 18.99840322, 'Na': 22.9897677, 'P': 30.973762, 'S': 31.9720707, 'Cl': 34.96885272, 'K': 38.9637074,
    'Cu': 62.9295989, 'Br': 78.9183361, 'Se': 79.9165196, 'I': 126.904473, 'H2O': 18.0105647, 'DMT': 303.13850493,
}
mass_avg = {
    'H': 1.00794, 'Li': 6.941, 'B': 10.811, 'C': 12.0107, 'N': 14.0067, 'O': 15.9994,
    'F': 18.9984032, 'Na': 22.98977, 'P': 30.973761, 'S': 32.065, 'Cl': 35.453, 'K': 39.0983,
    'Cu': 63.546, 'Br': 79.904, 'Se': 78.96, 'I': 126.90447, 'H2O': 18.01528, 'DMT': 303.37436,
}


# Extinction coefficients of single nucleotides:
# https://www.sigmaaldrich.com/technical-documents/articles/biology/quantitation-of-oligos.html
# https://en.wikipedia.org/wiki/Nucleic_acid_notation for degenerate base symbols.
nucleotide_extinction_260 = {'dA': 15400, 'dC': 7400,  'dG': 11500, 'dT': 8700, 'dCm': 7400, 'dU': 9900,
                             'dW': 12050, 'dS': 9450,  'dM': 11400, 'dK': 10050, 'dR': 13450, 'dY': 8050,
                             'dB': 9200,  'dD': 11867, 'dH': 10500, 'dV': 11433, 'dN': 10750,
                             'rA': 15400, 'rC': 7200,  'rG': 11500, 'rU': 9900,
                             'fA': 15400, 'fC': 7200, 'fG': 11500, 'fU': 9900,
                             'mA': 15400, 'mC': 7200, 'mG': 11500, 'mU': 9900,
                             '+A': 15400, '+Cm': 7200, '+G': 11500, '+T': 8700,
                             'moeA': 15400, 'moeCm': 7200, 'moeG': 11500, 'moeT': 8700,
                             'A': 15400, 'C': 7400, 'G': 11500, 'T': 8700, 'U': 9900,
                             }

# Extinction coefficients of dinucleotides:
dinucleotide_extinction_260 = {'AA': 27400, 'AC': 21200, 'AG': 25000, 'AT': 22800,
                       'CA': 21200, 'CC': 14600, 'CG': 18000, 'CT': 15200,
                       'GA': 25200, 'GC': 17600, 'GG': 21600, 'GT': 20000,
                       'TA': 23400, 'TC': 16200, 'TG': 19000, 'TT': 16800,
                       'UA': 24600, 'UC': 17200, 'UG': 20000, 'UU': 19600,
                       'AU': 24000, 'CU': 16200, 'GU': 21200, 'UT': 18200, 'TU': 18200,
                       }
# dint_extinction_RNA_260 = {'AA': 27400, 'AC': 21000, 'AG': 25000, 'AU': 24000,
#                            'CA': 21000, 'CC': 14200, 'CG': 17800, 'CU': 16200,
#                            'GA': 25200, 'GC': 17400, 'GG': 21600, 'GU': 21200,
#                            'UA': 24600, 'UC': 17200, 'UG': 20000, 'UU': 19600,
#                            }

# Extinction coefficients at 260 nm of popular modifications:
modification_extinction_260 = {
    'FAM': 21000, 'TET': 16300, 'HEX': 31600, 'JOE': 12000,
    'TAMRA': 32300, 'R6G': 18000, 'ROX': 22600,
    'Cy3': 4930, 'Cy3.5': 24000, 'Cy5': 10000, 'Cy5.5': 28800,

    'BHQ1': 8000, 'BHQ2': 8000,
    'YakYel': 23700, 'TexRd': 14400, 'IaBk': 44510,

    'po': 0, 'ps': 0, '*': 0,
}

map_nucleoside = {
    'dA': 'A', 'dC': 'C', 'dG': 'G', 'dT': 'T', 'dCm': 'C', 'dU': 'U',
    'rA': 'A', 'rC': 'C', 'rG': 'G', 'rU': 'U',
    'fA': 'A', 'fC': 'C', 'fG': 'G', 'fU': 'U',
    'mA': 'A', 'mC': 'C', 'mG': 'G', 'mU': 'U',
    '+A': 'A', '+Cm': 'C', '+G': 'G', '+T': 'T',
    'moeA': 'A', 'moeCm': 'C', 'moeG': 'G', 'moeT': 'T',
}


# 'Alfabet' of nucleosides. Can be at any position
# d -     deoxy
# r -     ribo
# f -     2'-fluoro
# m -     2'-methoxy
# + -     LNA
# moe -   2-MOE
nucleotide_any_position = (
    'dA', 'dC', 'dG', 'dT', 'dCm', 'dU',
    'dW', 'dS', 'dM', 'dK', 'dR', 'dY', 'dB', 'dD', 'dH', 'dV', 'dN',
    'rA', 'rC', 'rG', 'rU',
    'fA', 'fC', 'fG', 'fU',
    'mA', 'mC', 'mG', 'mU',
    '+A', '+Cm', '+G', '+T',
    'moeA', 'moeCm', 'moeG', 'moeT',
)

# Modifications available only at 5'-position
modification_5_position = ('Alkyne', 'FAM', 'TAMRA', 'Cy5',)

# Modifications available only at 3'-position
modification_3_position = ('BHQ1', 'BHQ2',)

# Modifications available only at internal position
modification_int_position = ()

all_nucleotide = nucleotide_any_position + modification_5_position + modification_3_position + modification_int_position

# Modifications available on phosphate
modification_phosphorus = ('po', 'ps', '*')

degenerate_nucleotide = ('dW', 'dS', 'dM', 'dK', 'dR', 'dY', 'dB', 'dD', 'dH', 'dV', 'dN',)

formula = {
    'dA': {'C': 10, 'H': 13, 'N': 5, 'O': 3},
    'dC': {'C': 9, 'H': 13, 'N': 3, 'O': 4},
    'dG': {'C': 10, 'H': 13, 'N': 5, 'O': 4},
    'dT': {'C': 10, 'H': 14, 'N': 2, 'O': 5},
    'dCm': {'C': 10, 'H': 15, 'N': 3, 'O': 4},
    'dU': {'C': 9, 'H': 12, 'N': 2, 'O': 5},
    'dW': {'C': 10, 'H': 13.5, 'N': 3.5, 'O': 4},
    'dS': {'C': 9.5, 'H': 13, 'N': 4, 'O': 4},
    'dM': {'C': 9.5, 'H': 13, 'N': 4, 'O': 3.5},
    'dK': {'C': 10, 'H': 13.5, 'N': 3.5, 'O': 4.5},
    'dR': {'C': 10, 'H': 13, 'N': 5, 'O': 3.5},
    'dY': {'C': 9.5, 'H': 13.5, 'N': 2.5, 'O': 4.5},
    'dB': {'C': 9.6667, 'H': 13.3333, 'N': 3.3333, 'O': 4.3333},
    'dD': {'C': 10, 'H': 13.3333, 'N': 4, 'O': 4},
    'dH': {'C': 9.6667, 'H': 13.3333, 'N': 3.3333, 'O': 4},
    'dV': {'C': 9.6667, 'H': 13, 'N': 4.3333, 'O': 3.6667},
    'dN': {'C': 9.75, 'H': 13.25, 'N': 3.75, 'O': 4},
    'rA': {'C': 10, 'H': 13, 'N': 5, 'O': 4},
    'rC': {'C': 9, 'H': 13, 'N': 3, 'O': 5},
    'rG': {'C': 10, 'H': 13, 'N': 5, 'O': 5},
    'rU': {'C': 9, 'H': 12, 'N': 2, 'O': 6},
    'fA': {'C': 10, 'H': 12, 'N': 5, 'O': 3, 'F': 1},
    'fC': {'C': 9, 'H': 12, 'N': 3, 'O': 4, 'F': 1},
    'fG': {'C': 10, 'H': 12, 'N': 5, 'O': 4, 'F': 1},
    'fU': {'C': 9, 'H': 11, 'N': 2, 'O': 5, 'F': 1},
    'mA': {'C': 11, 'H': 15, 'N': 5, 'O': 4},
    'mC': {'C': 10, 'H': 15, 'N': 3, 'O': 5},
    'mG': {'C': 11, 'H': 15, 'N': 5, 'O': 5},
    'mU': {'C': 10, 'H': 14, 'N': 2, 'O': 6},
    '+A': {'C': 11, 'H': 13, 'N': 5, 'O': 4},
    '+Cm': {'C': 11, 'H': 15, 'N': 3, 'O': 5},
    '+G': {'C': 11, 'H': 13, 'N': 5, 'O': 5},
    '+T': {'C': 11, 'H': 14, 'N': 2, 'O': 6},
    'moeA': {'C': 13, 'H': 19, 'N': 5, 'O': 5},
    'moeCm': {'C': 13, 'H': 21, 'N': 3, 'O': 6},
    'moeG': {'C': 13, 'H': 19, 'N': 5, 'O': 6},
    'moeT': {'C': 13, 'H': 20, 'N': 2, 'O': 7},
    'Alkyne': {'C': 12, 'H': 19, 'N': 1, 'O': 2},
    'FAM': {'C': 27, 'H': 25, 'N': 1, 'O': 7},
    'TAMRA': {'C': 31, 'H': 33, 'N': 3, 'O': 5},
    'Cy5': {'C': 47, 'H': 64, 'N': 7, 'O': 3},
    'BHQ1': {'C': 25, 'H': 28, 'N': 6, 'O': 5},
    'BHQ2': {'C': 24, 'H': 26, 'N': 6, 'O': 6},

    'po': {'H': 3, 'O': 4, 'P': 1},
    'ps': {'H': 3, 'O': 3, 'P': 1, 'S': 1},
    '*': {'H': 3, 'O': 3, 'P': 1, 'S': 1},
}


def sequence_split(sequence):
    """
    The function takes raw sequence as a string and converts it into a tuple:
    e.g. VinylP-A dC fT ps rA Spacer-18 moeG rU lG ps Cy3 is converted to
    ('VinylP-A' 'dC' 'fT' 'ps' 'rA' 'Spacer-18' 'moeG' 'rU' 'lG' 'ps' 'Cy3')
    """
    return tuple(sequence.strip().split())

def get_length(sequence):
    """
    Takes sequence as a string and returns length of chain (number of nucleosides)
    """
    return len([i for i in sequence_split(sequence) if i not in modification_phosphorus])


def extinction_nn(sequence):
    """Takes sequence as a string and calculates extinction coefficient of non-modified
    single-stranded oligodeoxynucleotide using nearest neighbour method"""
    extinction_nn = 0

    # extinction coefficients are determined for pairs by reading from the 5' to 3' position.
    # extinction of overlapping nucleotides then subtracted
    for dinucleotide in range(len(sequence) - 1):
        extinction_nn += dinucleotide_extinction_260[sequence[dinucleotide:dinucleotide + 2]]
    for nucleotide in range(1, len(sequence) - 1):
        extinction_nn -= nucleotide_extinction_260[sequence[nucleotide]]
    return extinction_nn


def extinction_base_composition(sequence):
    """Takes sequence as a collection e.g. tuple and calculates extinction coefficient of modified
    single-stranded oligodeoxynucleotides containing degenerate bases"""
    extinction_bc = 0
    for nucleotide in sequence:
        extinction_bc += {**nucleotide_extinction_260, **modification_extinction_260}[nucleotide]
    return extinction_bc


def get_extinction(sequence):
    """
    Takes sequence as a string and returns extinction calculated depending on the sequence composition
    either with nearest neighbours method or by base composition model
    """
    sequence_nn = ''
    sequence_base_comp = ()

    sequence_spl = sequence_split(sequence)
    for nt in sequence_spl:
        if nt in map_nucleoside:
            sequence_nn += map_nucleoside[nt]
        else:
            sequence_base_comp += (nt,)
    if len(sequence_nn) >= 2:
        extinction = extinction_base_composition(sequence_base_comp) + extinction_nn(sequence_nn)
    else:
        extinction = extinction_base_composition(sequence_spl)
    return extinction


def sequence_explicit(sequence):
    """Takes sequence as a string and returns another string with explicit phosphates, e.g.
    'dA dC ps dT fT' --> 'dA po dC ps dT po fT'
    """
    full_seq = ''
    seq_tup = sequence_split(sequence)
    for i in range(len(seq_tup)-1):
        if (    ((seq_tup[i] in all_nucleotide) and (seq_tup[i+1] in modification_phosphorus)) or
                ((seq_tup[i] in modification_phosphorus) and (seq_tup[i + 1] in all_nucleotide))    ):
            full_seq += seq_tup[i] + ' '
        if (seq_tup[i] in all_nucleotide) and (seq_tup[i+1] in all_nucleotide):
            full_seq += seq_tup[i] + ' po '
        if i == len(seq_tup) - 2:
            full_seq += seq_tup[i+1]
    return full_seq


def get_mass_avg(sequence):
    """
    Takes a sequence as a string and calculates average molecular mass of this sequence.
    Returns value of average mass.
    """
    sequence_full = sequence_explicit(sequence)
    m_avg = 0
    if get_length(sequence) == 1:
        for atom in formula[sequence]:
            m_avg += mass_avg[atom] * formula[sequence][atom]
        return round(m_avg, 2)
    for nt in sequence_split(sequence_full):
        for atom in formula[nt]:
            m_avg += mass_avg[atom] * formula[nt][atom]
    m_avg -= mass_avg['H2O'] * (len(sequence_split(sequence_full))-1)
    return round(m_avg, 2)


def get_mass_monoisotopic(sequence):
    """
    Takes a sequence as a string and calculates monoisotopic molecular mass of this sequence.
    Returns value of monoisotopic mass.
    """
    sequence_full = sequence_explicit(sequence)
    m_mono = 0
    if get_length(sequence) == 1:
        for atom in formula[sequence]:
            m_mono += mass_mono[atom] * formula[sequence][atom]
        return round(m_mono, 5)
    for nt in sequence_split(sequence_full):
        for atom in formula[nt]:
            m_mono += mass_mono[atom] * formula[nt][atom]
    m_mono -= mass_mono['H2O'] * (len(sequence_split(sequence_full))-1)
    return round(m_mono, 4)


def contain_degenerate_nucleotide(sequence):
    """
    Takes a sequence as a string and checks whether it contains any degenerate nucleotide.
    Returns True if yes, otherwise False
    """
    for nt in sequence_split(sequence):
        if nt in degenerate_nucleotide:
            return True
    return False