# Monoisotopic and average masses of elements and some molecules
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
                             'rW': 12650, 'rS': 9350,  'rM': 11300, 'rK': 10700, 'rR': 13450, 'rY': 8550,
                             'rB': 9533,  'rD': 12267, 'rH': 10833, 'rV': 11367, 'rN': 11000,
                             'fA': 15400, 'fC': 7200, 'fG': 11500, 'fU': 9900,
                             'mA': 15400, 'mC': 7200, 'mG': 11500, 'mU': 9900,
                             '+A': 15400, '+Cm': 7200, '+G': 11500, '+T': 8700,
                             'moeA': 15400, 'moeCm': 7200, 'moeG': 11500, 'moeT': 8700,
                             'A': 15400, 'C': 7400, 'G': 11500, 'T': 8700, 'U': 9900}

# Michael J. Cavaluzzi and Philip N. Borer. Revised UV extinction coefficients for nucleoside-5′-monophosphates
# and unpaired DNA and RNA. Nucleic Acids Res. 2004; 32(1): e13. 10.1093/nar/gnh015
# nucleotide_extinction_260 = {'dA': 15060, 'dC': 7100, 'dG': 12180, 'dT': 8560,
#                              'rA': 15020, 'rC': 7070, 'rG': 12080, 'rU': 9660}

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
    'FAM': 21000, 'TET': 16300, 'HEX': 31600, 'JOE': 12000, 'VIC': 7200,
    'TMR-ACH': 32300, 'R6G': 18000, 'R6G-ACH': 18000, 'ROX-CLK': 22600,

    'CY3-ACH': 4930, 'CY3.5': 24000, 'CY5-CLK': 10000, 'CY5.5': 28800,
    'ALKYNE': 0,

    'DABCYL': 11100, 'BHQ0': 7700, 'BHQ1': 8000, 'BHQ2': 8000, 'BHQ3': 13000,
    'MGB': 37900, 'MGB-ECLIPSE': 44500, 'ECLIPSE': 6600,

    'YAKYEL': 23700, 'TR-CLK': 14400, 'IABK': 44510, 'AF594-CLK': 29400,

    'ATTO647N-CLK': 6000,

    'GALNAC-PRO': 0, 'CHOL-PRO': 0, 'GALNAC3-ALN': 0,

    'po': 0, 'ps': 0, '*': 0, 'ps2': 0, 'ms': 0,
}

map_compl = {
    'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'U': 'A',
    'W': 'W', 'S': 'S', 'M': 'K', 'K': 'M', 'R': 'Y', 'Y': 'R', 'B': 'V', 'D': 'H', 'H': 'D', 'V': 'B', 'N': 'N',
}

map_nucleoside = {
    'dA': 'A', 'dC': 'C', 'dG': 'G', 'dT': 'T', 'dCm': 'C', 'dU': 'U',
    'rA': 'A', 'rC': 'C', 'rG': 'G', 'rU': 'U',
    'fA': 'A', 'fC': 'C', 'fG': 'G', 'fU': 'U',
    'mA': 'A', 'mC': 'C', 'mG': 'G', 'mU': 'U',
    '+A': 'A', '+Cm': 'C', '+G': 'G', '+T': 'T',
    'moeA': 'A', 'moeCm': 'C', 'moeG': 'G', 'moeT': 'T',
}

map_deg_nucleoside = {
    'dW': 'W', 'dS': 'S', 'dM': 'M', 'dK': 'K', 'dR': 'R', 'dY': 'Y',
    'dB': 'B', 'dD': 'D', 'dH': 'H', 'dV': 'V', 'dN': 'N',
    'rW': 'W', 'rS': 'S', 'rM': 'M', 'rK': 'K', 'rR': 'R', 'rY': 'Y',
    'rB': 'B', 'rD': 'D', 'rH': 'H', 'rV': 'V', 'rN': 'N',
}

map_nucleobase = {
    'dA': 'baseA', 'dC': 'baseC', 'dG': 'baseG', 'dT': 'baseT', 'dCm': 'baseCm', 'dU': 'baseU',
    'rA': 'baseA', 'rC': 'baseC', 'rG': 'baseG', 'rU': 'baseU',
    'fA': 'baseA', 'fC': 'baseC', 'fG': 'baseG', 'fU': 'baseU',
    'mA': 'baseA', 'mC': 'baseC', 'mG': 'baseG', 'mU': 'baseU',
    '+A': 'baseA', '+Cm': 'baseCm', '+G': 'baseG', '+T': 'baseT',
    'moeA': 'baseA', 'moeCm': 'baseCm', 'moeG': 'baseG', 'moeT': 'baseT',
}

map_dna2mix = {
    'A': 'dA', 'C': 'dC', 'G': 'dG', 'T': 'dT',
    'W': 'dW', 'S': 'dS', 'M': 'dM', 'K': 'dK', 'R': 'dR', 'Y': 'dY', 'B': 'dB', 'D': 'dD', 'H': 'dH', 'V': 'dV', 'N': 'dN',
    '[dCm]': 'dCm', '[dU]': 'dU',
    '[rA]': 'rA', '[rC]': 'rC', '[rG]': 'rG', '[rU]': 'rU',
    '[rW]': 'rW', '[rS]': 'rS', '[rM]': 'rM', '[rK]': 'rK', '[rR]': 'rR', '[rY]': 'rY', '[rB]': 'rB', '[rD]': 'rD', '[rH]': 'rH', '[rV]': 'rV', '[rN]': 'rN',
    '[fA]': 'fA', '[fC]': 'fC', '[fG]': 'fG', '[fU]': 'fU',
    '[mA]': 'mA', '[mC]': 'mC', '[mG]': 'mG', '[mU]': 'mU',
    '[+A]': '+A', '[+Cm]': '+Cm', '[+G]': '+G', '[+T]': '+T',
    '[moeA]': 'moeA', '[moeCm]': 'moeCm', '[moeG]': 'moeG', '[moeT]': 'moeT',
    '[ALKYNE]': 'ALKYNE', '[FAM]': 'FAM', '[TET]': 'TET', '[HEX]': 'HEX', '[JOE]': 'JOE', '[VIC]': 'VIC',
    '[TMR-ACH]': 'TMR-ACH', '[R6G]': 'R6G', '[R6G-ACH]': 'R6G-ACH', '[ROX-CLK]': 'ROX-CLK', '[CY3-ACH]': 'CY3-ACH',
    '[CY5-CLK]': 'CY5-CLK', '[CHOL-PRO]': 'CHOL-PRO', '[GALNAC-PRO]': 'GALNAC-PRO', '[GALNAC3-ALN]': 'GALNAC3-ALN',
    '[TR-CLK]': 'TR-CLK', '[AF594-CLK]': 'AF594-CLK', '[ATTO647N-CLK]': 'ATTO647N-CLK',
    '[BHQ1]': 'BHQ1', '[BHQ2]': 'BHQ2', '[MGB]': 'MGB', '[MGB-ECLIPSE]': 'MGB-ECLIPSE', '[ECLIPSE]': 'ECLIPSE',
    '*': '*', '[po]': 'po', '[ps]': 'ps', '[ps2]': 'ps2', '[ms]': 'ms',
}

map_rna2mix = {
    'A': 'rA', 'C': 'rC', 'G': 'rG', 'U': 'rU',
    'W': 'rW', 'S': 'rS', 'M': 'rM', 'K': 'rK', 'R': 'rR', 'Y': 'rY', 'B': 'rB', 'D': 'rD', 'H': 'rH', 'V': 'rV', 'N': 'rN',
    '[dCm]': 'dCm', '[dU]': 'dU',
    '[dA]': 'dA', '[dC]': 'dC', '[dG]': 'dG', '[dT]': 'dT',
    '[dW]': 'dW', '[dS]': 'dS', '[dM]': 'dM', '[dK]': 'dK', '[dR]': 'dR', '[dY]': 'dY', '[dB]': 'dB', '[dD]': 'dD', '[dH]': 'dH', '[dV]': 'dV', '[dN]': 'dN',
    '[fA]': 'fA', '[fC]': 'fC', '[fG]': 'fG', '[fU]': 'fU',
    '[mA]': 'mA', '[mC]': 'mC', '[mG]': 'mG', '[mU]': 'mU',
    '[+A]': '+A', '[+Cm]': '+Cm', '[+G]': '+G', '[+T]': '+T',
    '[moeA]': 'moeA', '[moeCm]': 'moeCm', '[moeG]': 'moeG', '[moeT]': 'moeT',
    '[ALKYNE]': 'ALKYNE', '[FAM]': 'FAM', '[TET]': 'TET', '[HEX]': 'HEX', '[JOE]': 'JOE', '[VIC]': 'VIC',
    '[TMR-ACH]': 'TMR-ACH', '[R6G]': 'R6G', '[R6G-ACH]': 'R6G-ACH', '[ROX-CLK]': 'ROX-CLK', '[CY3-ACH]': 'CY3-ACH',
    '[CY5-CLK]': 'CY5-CLK', '[CHOL-PRO]': 'CHOL-PRO', '[GALNAC-PRO]': 'GALNAC-PRO', '[GALNAC3-ALN]': 'GALNAC3-ALN',
    '[TR-CLK]': 'TR-CLK', '[AF594-CLK]': 'AF594-CLK', '[ATTO647N-CLK]': 'ATTO647N-CLK',
    '[BHQ1]': 'BHQ1', '[BHQ2]': 'BHQ2', '[MGB]': 'MGB', '[MGB-ECLIPSE]': 'MGB-ECLIPSE', '[ECLIPSE]': 'ECLIPSE',
    '*': '*', '[po]': 'po', '[ps]': 'ps', '[ps2]': 'ps2', '[ms]': 'ms',
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
    'rW', 'rS', 'rM', 'rK', 'rR', 'rY', 'rB', 'rD', 'rH', 'rV', 'rN',
    'fA', 'fC', 'fG', 'fU',
    'mA', 'mC', 'mG', 'mU',
    '+A', '+Cm', '+G', '+T',
    'moeA', 'moeCm', 'moeG', 'moeT',
)

# Modifications available only at 5'-position
modification_5_position = ['FAM', 'TET', 'HEX', 'JOE', 'VIC',
                           'TMR-ACH', 'R6G', 'R6G-ACH', 'ROX-CLK', 'TR-CLK', 'AF594-CLK',
                           'CY3-ACH', 'CY5-CLK', 'ATTO647N-CLK',
                           'ALKYNE',
                           'CHOL-PRO', 'GALNAC-PRO',
                           'po']

# Modifications available only at 3'-position
modification_3_position = ['BHQ1', 'BHQ2', 'MGB', 'MGB-ECLIPSE', 'ECLIPSE',
                           'CHOL-PRO', 'GALNAC-PRO', 'GALNAC3-ALN',
                           'po']

# Modifications available only at internal position
modification_int_position = ['BHQ1', 'BHQ2', 'ECLIPSE', 'GALNAC-PRO']

# Modifications available on phosphate
modification_phosphorus = ['po', 'ps', '*', 'ps2', 'ms']

degenerate_nucleotide = ['dW', 'dS', 'dM', 'dK', 'dR', 'dY', 'dB', 'dD', 'dH', 'dV', 'dN',
                         'rW', 'rS', 'rM', 'rK', 'rR', 'rY', 'rB', 'rD', 'rH', 'rV', 'rN']

dna_nucleotides = ['dA', 'dC', 'dG', 'dT', 'dCm', 'dU']

all_nucleotide = {*nucleotide_any_position,
                  *modification_5_position,
                  *modification_3_position,
                  *modification_int_position} - {*modification_phosphorus}

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
    'dB': {'C': 9.67, 'H': 13.33, 'N': 3.33, 'O': 4.33},
    'dD': {'C': 10, 'H': 13.33, 'N': 4, 'O': 4},
    'dH': {'C': 9.67, 'H': 13.33, 'N': 3.33, 'O': 4},
    'dV': {'C': 9.67, 'H': 13, 'N': 4.33, 'O': 3.67},
    'dN': {'C': 9.75, 'H': 13.25, 'N': 3.75, 'O': 4},
    'rA': {'C': 10, 'H': 13, 'N': 5, 'O': 4},
    'rC': {'C': 9, 'H': 13, 'N': 3, 'O': 5},
    'rG': {'C': 10, 'H': 13, 'N': 5, 'O': 5},
    'rU': {'C': 9, 'H': 12, 'N': 2, 'O': 6},

    'rW': {'C': 9.5, 'H': 12.5, 'N': 3.5, 'O': 5},
    'rS': {'C': 9.5, 'H': 13, 'N': 4, 'O': 5},
    'rM': {'C': 9.5, 'H': 13, 'N': 4, 'O': 4.5},
    'rK': {'C': 9.5, 'H': 12.5, 'N': 3.5, 'O': 5.5},
    'rR': {'C': 10, 'H': 13, 'N': 5, 'O': 4.5},
    'rY': {'C': 9, 'H': 12.5, 'N': 2.5, 'O': 5.5},
    'rB': {'C': 9.33, 'H': 12.67, 'N': 3.33, 'O': 5.33},
    'rD': {'C': 9.67, 'H': 12.67, 'N': 4, 'O': 5},
    'rH': {'C': 9.33, 'H': 12.67, 'N': 3.33, 'O': 5},
    'rV': {'C': 9.67, 'H': 13, 'N': 4.33, 'O': 4.67},
    'rN': {'C': 9.5, 'H': 12.75, 'N': 3.75, 'O': 5},

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
    'ALKYNE': {'C': 12, 'H': 19, 'N': 1, 'O': 2},
    'FAM': {'C': 27, 'H': 25, 'N': 1, 'O': 7},
    'TMR-ACH': {'C': 31, 'H': 33, 'N': 3, 'O': 5},
    'CY3-ACH': {'C': 36, 'H': 47, 'N': 3, 'O': 2},
    'CY5-CLK': {'C': 47, 'H': 63, 'N': 7, 'O': 3},
    'VIC': {'C': 33, 'H': 26, 'Cl': 3, 'N': 1, 'O': 7},
    'TET': {'C': 27, 'H': 21, 'Cl': 4, 'N': 1, 'O': 7},
    'HEX': {'C': 27, 'H': 19, 'Cl': 6, 'N': 1, 'O': 7},
    'JOE': {'C': 29, 'H': 27, 'Cl': 2, 'N': 1, 'O': 9},
    'R6G': {'C': 33, 'H': 39, 'N': 3, 'O': 5},
    'R6G-ACH': {'C': 33, 'H': 37, 'N': 3, 'O': 5},
    'ROX-CLK': {'C': 48, 'H': 55, 'N': 7, 'O': 6},
    'TR-CLK': {'C': 46, 'H': 55, 'N': 7, 'O': 8, 'S': 2},
    'AF594-CLK': {'C': 50, 'H': 59, 'N': 7, 'O': 12, 'S': 2},
    'ATTO647N-CLK': {'C': 62, 'H': 86, 'N': 8, 'O': 7},

    'BHQ1': {'C': 25, 'H': 28, 'N': 6, 'O': 5},
    'BHQ2': {'C': 24, 'H': 26, 'N': 6, 'O': 6},
    'MGB': {'C': 44, 'H': 47, 'N': 7, 'O': 6},
    'MGB-ECLIPSE': {'C': 57, 'H': 56, 'Cl': 1, 'N': 11, 'O': 8},
    'ECLIPSE': {'C': 22, 'H': 26, 'Cl': 1, 'N': 5, 'O': 5},

    'CHOL-PRO': {'C': 39, 'H': 66, 'N': 2, 'O': 5},
    'GALNAC-PRO': {'C': 24, 'H': 43, 'N': 3, 'O': 10},
    'GALNAC3-ALN': {'C': 78, 'H': 139, 'N': 11, 'O': 31},

    'baseA': {'C': 5, 'H': 5, 'N': 5},
    'baseC': {'C': 4, 'H': 5, 'N': 3, 'O': 1},
    'baseCm': {'C': 5, 'H': 7, 'N': 3, 'O': 1},
    'baseG': {'C': 5, 'H': 5, 'N': 5, 'O': 1},
    'baseT': {'C': 5, 'H': 6, 'N': 2, 'O': 2},
    'baseU': {'C': 4, 'H': 4, 'N': 2, 'O': 2},

    'H2O': {'H': 2, 'O': 1},
    'po': {'H': 3, 'O': 4, 'P': 1},
    'ps': {'H': 3, 'O': 3, 'P': 1, 'S': 1},
    '*': {'H': 3, 'O': 3, 'P': 1, 'S': 1},
    'ps2': {'H': 3, 'O': 2, 'P': 1, 'S': 2},
    'ms': {'C': 1, 'H': 6, 'O': 5, 'N': 1, 'P': 1, 'S': 1},
}


def rev_compl(sequence):
    """
    Takes a cleared sequence in 'DNA' style format and returns reverse complement
    """
    return ''.join([map_compl[nt] for nt in sequence][::-1])


def sequence_split(sequence):
    """
    The function takes a sequence as a string and converts it into a tuple:
    e.g. FAM dC fT * rA +T moeG rU +G * CY3 is converted to
    ('FAM', 'dC', 'fT', '*', 'rA', '+T', 'moeG', 'rU', '+G', '*', 'CY3')
    """
    return tuple(sequence.strip().split())


def get_length(sequence):
    """
    Takes sequence in 'Therapeutic format' and returns length of chain (number of nucleosides)
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
    if len(sequence_split(sequence)) == 1:
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
    Takes a sequence in Therapeutic format as a string and calculates monoisotopic molecular mass of this sequence.
    Returns value of monoisotopic mass.
    """
    sequence_full = sequence_explicit(sequence)
    m_mono = 0
    if len(sequence_split(sequence)) == 1:
        for atom in formula[sequence]:
            m_mono += mass_mono[atom] * formula[sequence][atom]
        return round(m_mono, 4)
    for nt in sequence_split(sequence_full):
        for atom in formula[nt]:
            m_mono += mass_mono[atom] * formula[nt][atom]
    m_mono -= mass_mono['H2O'] * (len(sequence_split(sequence_full))-1)
    return round(m_mono, 4)


def get_formula(sequence):
    """
    Takes a sequence as a string and calculates returns it brutto formula.
    """
    sequence_full = sequence_explicit(sequence)
    if len(sequence_split(sequence)) == 1:
        brutto_formula = ''
        for atom, number in formula[sequence].items():
            brutto_formula += str(atom) + str(number)
        return brutto_formula
    brutto_formula = {}
    brutto_formula_str = ''
    for nt in sequence_split(sequence_full):
        for atom, number in formula[nt].items():
            brutto_formula[atom] = brutto_formula.get(atom, 0) + number
    for atom, number in formula['H2O'].items():
        brutto_formula[atom] = brutto_formula.get(atom, 0) - number * (len(sequence_split(sequence_full))-1)
    for atom, number in brutto_formula.items():
        brutto_formula_str += str(atom) + str(round(number, 2))
    return brutto_formula_str


def contain_degenerate_nucleotide(sequence):
    """
    Takes a sequence in Therapeutic style as a string and checks whether it contains any degenerate nucleotide.
    Returns True if yes, otherwise False
    """
    for nt in sequence_split(sequence):
        if nt in degenerate_nucleotide:
            return True
    return False


def get_ms_fragments(sequence):
    """
    Takes a sequence as a string, returns theoretical masses of several charge states of the following ions:
    d, c, b, a, a-B, w, x, y, z
    """
    d = {}
    c = {}
    b = {}
    a = {}
    a_B = {}
    w = {}
    x = {}
    y = {}
    z = {}
    seq_full_tup = sequence_split(sequence_explicit(sequence))
    mass = get_mass_monoisotopic(sequence)
    count_nt = 0

    for index in range(len(seq_full_tup)):
        if seq_full_tup[index] in all_nucleotide and index < len(seq_full_tup)-2:
            count_nt += 1
            seq_part_tup_l = seq_full_tup[:index + 1]
            seq_part_tup_l_plus_phos = seq_full_tup[:index + 2]
            seq_part_tup_r_plus_phos = seq_full_tup[index + 1:]
            seq_part_tup_r = seq_full_tup[index + 2:]
            seq_part_l = ' '.join(seq_part_tup_l)
            seq_part_l_plus_phos = ' '.join(seq_part_tup_l_plus_phos)
            seq_part_r_plus_phos = ' '.join(seq_part_tup_r_plus_phos)
            seq_part_r = ' '.join(seq_part_tup_r)
            b[count_nt] = get_mass_monoisotopic(seq_part_l)
            a[count_nt] = round(b[count_nt] - mass_mono['H2O'], 4)
            d[count_nt] = get_mass_monoisotopic(seq_part_l_plus_phos)
            c[count_nt] = round(d[count_nt] - mass_mono['H2O'], 4)
            y[count_nt + 1] = get_mass_monoisotopic(seq_part_r)
            z[count_nt + 1] = round(y[count_nt + 1] - mass_mono['H2O'], 4)
            w[count_nt + 1] = get_mass_monoisotopic(seq_part_r_plus_phos)
            x[count_nt + 1] = round(w[count_nt + 1] - mass_mono['H2O'], 4)
            if seq_part_tup_l[-1] in map_nucleobase:
                a_B[count_nt] = round(a[count_nt] - get_mass_monoisotopic(map_nucleobase[seq_part_tup_l[-1]]), 4)
            else:
                a_B[count_nt] = 0

        if seq_full_tup[index] in all_nucleotide and (index == len(seq_full_tup)-1 or index == len(seq_full_tup)-2):
            a[count_nt + 1] = 0
            a_B[count_nt + 1] = 0
            b[count_nt + 1] = 0
            c[count_nt + 1] = 0
            d[count_nt + 1] = 0
            w[1] = 0
            x[1] = 0
            y[1] = 0
            z[1] = 0
    return a, a_B, b, c, d, w, x, y, z


def get_ms_fragments_esi_series(frag_dict):
    """
    Takes dictionary containing mass fragments and creates another dict containing esi series of fragments,
    up to half-charged states.
    """
    frag_dict_esi = {}
    for index, mass in frag_dict.items():
        mass_esi = ()
        for charge_state in range(1, len(frag_dict)):
            mass_esi += (round((mass - charge_state * mass_mono['H']) / charge_state, 3), )
        frag_dict_esi[index] = mass_esi
    return frag_dict_esi


def dna2mix(sequence):
    """
    Takes a sequence in 'DNA' style format, convert it in 'Therapeutic' style format
    """
    seq_tup = sequence2tuple(sequence)
    seq_mix = [map_dna2mix[nt] for nt in seq_tup]
    return ' '.join(seq_mix)


def rna2mix(sequence):
    """
    Takes a sequence in 'RNA' style format, convert it in 'Therapeutic' style format
    """
    seq_tup = sequence2tuple(sequence)
    seq_mix = [map_rna2mix[nt] for nt in seq_tup]
    return ' '.join(seq_mix)


def mix2dna_wo_mod_degen_phosph(sequence):
    """
    Takes a sequence in 'Therapeutic' style format, convert it in 'DNA' style format.
    Phosphates, modifications and degenerate nucleosides are omitted.
    """
    seq_dna = [map_nucleoside[nt] for nt in sequence_split(sequence) if nt in map_nucleoside]
    return ''.join(seq_dna)


def mix2dna_wo_mod_phosph(sequence):
    """
    Takes a sequence in 'Therapeutic' style format, convert it in 'DNA' style format
    Phosphates and modifications are omitted.
    """
    map_nt = {**map_nucleoside, **map_deg_nucleoside}
    seq_dna = [map_nt[nt] for nt in sequence_split(sequence) if nt in map_nt]
    return ''.join(seq_dna)


def sequence2tuple(sequence):
    """The function takes a sequence as a string and converts it into a tuple:
        e.g. NN[6FAM]AACTNRG[BHQ1dT]TTACGTC[DABCYL]TT is converted to
        ('N','N','[6FAM], ... ,'[DABCYL]','T','T')
        """
    sequence_tuple = ()
    mod_str = ''
    mod = False

    for nt in sequence:
        if nt == '[' or mod is True:
            mod = True
            if nt !=' ':
                mod_str += nt
            if nt == ']':
                sequence_tuple += (mod_str,)
                mod = False
                mod_str = ''
            continue
        if nt != ' ':
            sequence_tuple += (nt,)
    return sequence_tuple


def wo_phosph(sequence):
    """
    Takes a sequence in 'Therapeutic' style format, removes all different phosphates
    """
    return ' '.join(nt for nt in sequence_split(sequence) if nt not in modification_phosphorus)


def gc_content(sequence_tup):
    """
    Takes sequence as a tuple of nucleosides w/o phosphates and returns GC content as a fraction of 1
    """
    sequence_str_wo_mod = ''.join(map_nucleoside[nt] for nt in sequence_tup if nt in map_nucleoside)
    g_c = sequence_str_wo_mod.count('G') + sequence_str_wo_mod.count('C')
    if len(sequence_str_wo_mod):
        return round(g_c / len(sequence_str_wo_mod), 2)
    else:
        return -1


def calculate_od260(epsilon260, mass_average):
    if epsilon260:
        nmol_OD260 = (1 / epsilon260) * 1e6
        ug_OD260 = (1 / epsilon260) * mass_average * 1e3
    else:
        nmol_OD260, ug_OD260 = -1, -1
    return nmol_OD260, ug_OD260


def calculate_esi_series(sequence, length, mass_average, mass_monoisotopic):
    esi_series = []
    for z in range(1, length):
        esi_series_avg_dmt_off = (mass_average - z * mass_avg['H']) / z
        esi_series_mono_dmt_off = (mass_monoisotopic - z * mass_mono['H']) / z if not contain_degenerate_nucleotide(sequence) else None
        esi_series.append((z, esi_series_avg_dmt_off, esi_series_mono_dmt_off))
    return esi_series


def calculate_mass_fragments(sequence, length, seq_wo_phosph_tup):
    mass_fragments_array = []
    a_esi, a_B_esi, b_esi, c_esi, d_esi, w_esi, x_esi, y_esi, z_esi = map(get_ms_fragments_esi_series,
                                                                          get_ms_fragments(sequence))
    for charge in range(1, length):
        mass_fragments_array.append([
            (d_esi[seq_ind][charge - 1], c_esi[seq_ind][charge - 1], b_esi[seq_ind][charge - 1],
             a_esi[seq_ind][charge - 1], a_B_esi[seq_ind][charge - 1], seq_wo_phosph_tup[seq_ind - 1],
             w_esi[seq_ind][charge - 1], x_esi[seq_ind][charge - 1], y_esi[seq_ind][charge - 1],
             z_esi[seq_ind][charge - 1]) for seq_ind in range(1, length + 1)
        ])
    return mass_fragments_array
