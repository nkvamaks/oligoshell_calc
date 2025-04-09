import math
from . import utils
from . import tm


SPAN = 1
mass_nucleoside = {'A': 251.10184, 'C': 227.09061, 'G': 267.09675, 'T': 242.09027, 'p': 61.95576}
mass_probe_dye = {'NO-ANY': 0, 'FAM-MGB': 1656.4748, 'VIC-MGB': 1834.3892, 'JUN-QSY': 1641.494,
                  'FAM-BHQ1': 1091.2867, 'HEX-BHQ1': 1295.053,
                  'TexRd-BHQ2': 1436.46, 'Cy5-BHQ2': 1088.43, 'ATTO647N-BHQ2': 1362.60}


def simple_fasta_parser(fasta):
    fasta_lines = fasta.split('\n')
    fasta_str = ''.join(line.strip() for line in fasta_lines if '>' not in line)
    return ''.join(letter.upper() for letter in fasta_str if letter not in ' \t\n\r\x0b\x0c')


def brutforce_oligo_composition(oligo_mass):
    min_len = math.ceil((oligo_mass + mass_nucleoside['p']) / (mass_nucleoside['G'] + mass_nucleoside['p']) - SPAN/2)
    max_len = math.floor((oligo_mass + mass_nucleoside['p']) / (mass_nucleoside['C'] + mass_nucleoside['p']) + SPAN/2)
    composition_list = []
    for k in range(min_len, max_len + 1):
        for a in range(k + 1):
            for c in range(k - a + 1):
                for g in range(k - a - c + 1):
                    t = k - a - c - g
                    brutforce_mass = a * mass_nucleoside['A'] + c * mass_nucleoside['C'] + g * mass_nucleoside['G'] + t * mass_nucleoside['T'] + (k - 1) * mass_nucleoside['p']
                    if (oligo_mass - SPAN / 2) <= brutforce_mass <= (oligo_mass + SPAN / 2):
                        composition_list.append({'a': a, 'c': c, 'g': g, 't': t, 'k': k})
    return composition_list


def find_seq_in_fasta_from_list(composition_list, fasta_seq):
    seq_list = []
    for compos in composition_list:
        oligo_len = compos['k']
        for pos_in_fasta in range(len(fasta_seq) - oligo_len + 1):
            oligo = fasta_seq[pos_in_fasta:pos_in_fasta + oligo_len]
            if [oligo.count(x) for x in 'ACGT'] == [compos['a'], compos['c'], compos['g'], compos['t']]:
                seq_list.append((oligo, pos_in_fasta))
                if len(seq_list) > 200:
                    break
    return seq_list


def find_matching_pair(seq_listF, seq_listR, amplicon_len, fasta_seq_len):
    matching_pair = []
    for seqF_seq, seqF_pos in seq_listF:
        for seqR_seq, seqR_pos in seq_listR:
            if fasta_seq_len - seqF_pos - seqR_pos == amplicon_len:
                matching_pair.append((seqF_seq, seqF_pos, seqR_seq, seqR_pos))
    return matching_pair


def get_taqman_assay(seqF_seq, seqR_seq, amplicon, seq_list_Pf, seq_list_Pr, seqF_pos):
    assay = ''
    if seq_list_Pf:
        probe_pf_count = 1
        for probe_pf, pos_pf in seq_list_Pf:
            assay += "<strong>Probe" + str(probe_pf_count) + "</strong> sense" + (8 - len(str(probe_pf_count))) * '&nbsp' + "5'- " + '&nbsp' * pos_pf + probe_pf + '<br>'
            probe_pf_count += 1
    assay += "<strong>Position in RefSeq</strong>" + 5 * '&nbsp' + "<small>" + str(seqF_pos) + '</small><br>'
    assay += "<strong>Forward</strong> sense" + 6 * '&nbsp' + "5'- " + seqF_seq + '<br>'
    assay += "<strong>Amplicon</strong> sense" + 5 * '&nbsp' + "5'- " + amplicon + " -3'" + '<br>'
    assay += "<strong>Amplicon</strong> antisense 3'- " + utils.rev_compl(amplicon)[::-1] + " -5'" + '<br>'
    assay += "<strong>Reverse</strong> antisense" + 2 * '&nbsp' + "3'- " + '&nbsp' * (len(amplicon) - len(seqR_seq)) + seqR_seq[::-1] + " -5'" + '<br>'
    if seq_list_Pr:
        probe_pr_count = 1
        for probe_pr, pos_pr in seq_list_Pr:
            assay += "<strong>Probe" + str(probe_pr_count) + "</strong> antisense" + (4 - len(str(probe_pr_count))) * '&nbsp' + "3'- " + '&nbsp' * (len(amplicon) - len(probe_pr) - pos_pr) + probe_pr[::-1] + '<br>'
            probe_pr_count += 1
    return assay


def calculate_mass_tm(seq_list, probe_dye):
    """
    Input: seq_list is a list of tuples [('ACGT...GTA', 345), ('GTGT...AAG', 789)]
    where tuple consists of oligo sequence and pos_in_amplicon, and probe_dye - mass of modifications
    Output: [(mass, tm), ] of correspondent sequences
    """
    list_mass_tm = []
    for seq, pos in seq_list:
        seq_mass = utils.get_mass_monoisotopic(utils.dna2mix(seq)) + mass_probe_dye[probe_dye]
        if probe_dye in ('FAM-MGB', 'VIC-MGB'):
            seq_tm = tm.calc_tm_mgb(seq=utils.dna2mix(seq),
                                    dna_conc=0.2,
                                    mv_conc=50,
                                    dv_conc=3,
                                    dntp_conc=0.8
                                    )
        else:
            seq_tm = tm.calc_tm(seq=utils.dna2mix(seq),
                                target='dna',
                                dna_conc=0.2,
                                mv_conc=50,
                                dv_conc=3,
                                dntp_conc=0.8
                                )
        list_mass_tm.append((seq_mass, seq_tm))
    return list_mass_tm

