from django.core.exceptions import ValidationError
import re

from . import utils


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

    if sequence_spl[0] not in set(utils.modification_5_position + utils.nucleotide_any_position):
        modification_errors.append("5'-Modification does not exist: " + sequence_spl[0])
    if len(sequence_spl) > 1:
        if sequence_spl[-1] not in set(utils.modification_3_position + utils.nucleotide_any_position):
            modification_errors.append("3'-Modification does not exist: " + sequence_spl[-1])
        for i in range(len(sequence_spl)-1):
            if i == 0: continue
            if sequence_spl[i] not in set( utils.modification_int_position +
                                           utils.modification_phosphorus +
                                           utils.nucleotide_any_position ):
                modification_errors.append("Internal modification does not exist: " + sequence_spl[i] + " at position " + str(i+1))
            if (sequence_spl[i] in utils.modification_phosphorus) and (sequence_spl[i+1] in utils.modification_phosphorus):
                modification_errors.append("Two phosphate residues at positions " + str(i+1) + " and " + str(i+2) + " cannot be nearby")
    if modification_errors:
        raise ValidationError(modification_errors)
    else:
        return sequence


def validate_seq_dna_regex(sequence):
    sequence_pattern = r'^(((\[[-+\._a-zA-Z0-9 ]+\])*?[aAcCgGtTwWsSmMkKrRyYbBdDhHvVnN* ]*?)*?)$'
    message = ('Sequence should contain A/C/G/T, degenerated bases W/S/M/K/R/Y/B/D/H/V/N,'
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
