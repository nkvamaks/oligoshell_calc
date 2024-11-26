from django.core.exceptions import ValidationError
import re

from . import utils
from . import taqman_find_utils


def validate_seq_mix(sequence):
    """
        Validates a sting of sequence on a right syntax. It is case-sensitive.
        String should be presented in a format:
        FAM dCm fT * rA SPACER18 moeG rU +G * GALNAC-PRO
        where the name of common nucleotides begin with small letters that represent sugar moiety
        followed by the capital letter representing nucleobase. After nucleobase it may be
        a combination of numbers and small letters indicating a modification of nucleotide.
        Other modifications are given as capital alphanumeric names.

        Available 2'-deoxynucleosides: dA, dC, dG, dT, dCm
        Available ribonucleosides: rA, rC, rG, rU
        Available 2'-fluoro-2'-deoxynucleosides: fA, fC, fG, fU
        Available 2'-methoxyribonucleosides: mA, mC, mG, mU
        Available locked nucleosides: +A, +Cm, +G, +T
        Available 2'-MOE nucleosides: moeA, moeCm, moeG, moeT

        Available phosphate modifications: po - phosphate (by default), * - phosphorothyoate
        """
    modification_errors = []
    sequence_spl = utils.sequence_split(sequence)

    if utils.get_length(sequence) == 0:
        raise ValidationError('Zero-length sequence is not allowed')
    if sequence_spl[0] not in {*utils.modification_5_position, *utils.nucleotide_any_position}:
        modification_errors.append("5'-Modification does not exist: " + sequence_spl[0])
    if utils.get_length(sequence) >= 1:
        if sequence_spl[-1] not in {*utils.modification_3_position, *utils.nucleotide_any_position}:
            modification_errors.append("3'-Modification does not exist: " + sequence_spl[-1])
        for i in range(len(sequence_spl)-1):
            if (sequence_spl[i] in utils.modification_phosphorus) and (sequence_spl[i+1] in utils.modification_phosphorus):
                modification_errors.append("Two backbones at positions " + str(i+1) + " and " + str(i+2) + " cannot be nearby")
            if i == 0: continue
            if sequence_spl[i] not in {*utils.modification_int_position,
                                       *utils.modification_phosphorus,
                                       *utils.nucleotide_any_position}:
                modification_errors.append("Internal modification does not exist: " + sequence_spl[i] + " at position " + str(i+1))
    if modification_errors:
        raise ValidationError(modification_errors)
    else:
        return sequence


def validate_seq_dna_regex(sequence):
    sequence_pattern = r'^(((\[[-+\._a-zA-Z0-9 ]+\])*?[ACGTWSMKRYBDHVN* ]*?)*?)$'
    message = ('Sequence should contain A/C/G/T, degenerate bases W/S/M/K/R/Y/B/D/H/V/N, backbones e.g. *, [ps2]'
               ' and modifications e.g. [FAM], [BHQ1] etc.')
    if not re.match(sequence_pattern, sequence):
        raise ValidationError(message)
    else:
        return sequence


def validate_seq_dna(sequence):
    """
    Validates a sting of sequence on a right syntax. It is case-sensitive.
    String should be presented in a format: [FAM]CT*A[moeG]TGAAGCTTTTCGGGGATC[BHQ1]
    where A, C, G and T are DNA nucleosides. All others non-'deoxy' nucleotides and
    modifications are given in square brackets.
    """
    seq_mix_list = []
    modification_errors = []

    # Convert dna-style sequence to a tuple: ACGT[BHQ1] -> ('A', 'C', 'G', 'T', '[BHQ1]')
    seq_dna_tup = utils.sequence2tuple(sequence)

    # Map every nucleoitde from seq_dna_tup to a 'mix' style. If nucleotide doesn't exist, raise
    # ValidationError
    for index, nt in enumerate(seq_dna_tup):
        if nt in utils.map_dna2mix:
            seq_mix_list.append(utils.map_dna2mix[nt])
        else:
            modification_errors.append('Unknown nucleotide ' + nt + ' position ' + str(index+1))
    if modification_errors:
        raise ValidationError(modification_errors)
    else:
        return ' '.join(seq_mix_list)


def validate_seq_rna_regex(sequence):
    sequence_pattern = r'^(((\[[-+\._a-zA-Z0-9 ]+\])*?[ACGUWSMKRYBDHVN* ]*?)*?)$'
    message = ('Sequence should contain A/C/G/U, degenerate bases W/S/M/K/R/Y/B/D/H/V/N, backbones e.g. *, [ps2]'
               ' and modifications e.g. [FAM], [BHQ1] etc.')
    if not re.match(sequence_pattern, sequence):
        raise ValidationError(message)
    else:
        return sequence


def validate_seq_rna(sequence):
    """
    Validates a sting of sequence on a right syntax. It is case-sensitive.
    String should be presented in a format: [FAM]CU*A[moeG]UGAAGCUUUUCGGGGAUC[BHQ1]
    where A, C, G and U are RNA nucleosides. All others non-'ribo' nucleotides and
    modifications are given in square brackets.
    """
    seq_mix_list = []
    modification_errors = []

    # Convert rna-style sequence to a tuple: ACGU[BHQ1] -> ('A', 'C', 'G', 'U', '[BHQ1]')
    seq_rna_tup = utils.sequence2tuple(sequence)

    # Map every nucleoitde from seq_rna_tup to a 'mix' style. If nucleotide doesn't exist, raise
    # ValidationError
    for index, nt in enumerate(seq_rna_tup):
        if nt in utils.map_rna2mix:
            seq_mix_list.append(utils.map_rna2mix[nt])
        else:
            modification_errors.append('Unknown nucleotide ' + nt + ' position ' + str(index+1))
    if modification_errors:
        raise ValidationError(modification_errors)
    else:
        return ' '.join(seq_mix_list)


def validate_dna_conc(value):
    message = 'The oligo concentration is invalid, it must be within the range 0.0001 - 5000 uM.'
    if 0.0001 < value < 5000:
        return value
    else:
        raise ValidationError(message)


def validate_mv_conc(value):
    message = 'The Na+ concentration is invalid, it must be within the range 2 - 3000 mM.'
    if 2 <= value <= 3000:
        return value
    else:
        raise ValidationError(message)


def validate_dv_conc(value):
    message = 'The Mg2+ concentration is invalid, it must be within the range 0 - 600 mM.'
    if 0 <= value <= 600:
        return value
    else:
        raise ValidationError(message)


def validate_dntp_conc(dntp_value, dv_value):
    message = 'The dNTP concentration is invalid, it must be within the range 0 - ' + str(round(dv_value * 1.2, 2)) + ' mM (20% higher than Mg2+).'
    if 0 <= dntp_value <= dv_value * 1.2:
        return dntp_value
    else:
        raise ValidationError(message)


def validate_fasta(fasta):
    fasta_seq = taqman_find_utils.simple_fasta_parser(fasta)
    nucleotides = set(fasta_seq)
    standard_nucleotides = []
    for nucleotide in nucleotides:
        standard_nucleotides.append(True if nucleotide in 'AaCcGgTtUuWwSsMmKkRrYyBbDdHhVvNn' else False)
    if not all(standard_nucleotides):
        raise ValidationError(message='Sequence contains nucleotides other than A/C/G/T/W/S/M/K/R/Y/B/D/H/V/N')
    else:
        return fasta


def validate_primer1(primer1):
    if 800 <= primer1 <= 20000:
        return primer1
    else:
        raise ValidationError(message='Mass of Primer1 must be within the range 800 - 20.000 Da')


def validate_primer2(primer2):
    if 800 <= primer2 <= 20000:
        return primer2
    else:
        raise ValidationError(message='Mass of Primer2 must be within the range 800 - 20.000 Da')


def validate_probe(probe):
    if 800 <= probe <= 20000:
        return probe
    else:
        raise ValidationError(message='Mass of Probe must be within the range 800 - 20.000 Da')


def validate_amp_size(amp_size):
    if 10 <= amp_size <= 10000:
        return amp_size
    else:
        raise ValidationError(message='Amplicon length must be within the range 10 - 10.000')

