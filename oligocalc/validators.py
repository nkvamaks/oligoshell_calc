from django.core.exceptions import ValidationError
from . import utils


def validate_seq(sequence):
    """
        Validates a sting of sequence on a right syntax. It is case-sensitive.
        String should be presented in a format:
        [VinylP-A] dC_5me fT ps rA [Spacer-18] moeG rU lG ps [Cy3]
        where the name of common nucleotides begin with small letters that represent sugar moiety
        followed by the capital letter representing nucleobase. After nucleobase and underscore it may be
        a combination of numbers and small letters indicating a modification of nucleotide.
        Other modifications are given in square brackets.

        Available 2'-deoxynucleosides: dA, dC, dG, dT, dC_5me
        Available ribonucleosides: rA, rC, rG, rU
        Available 2'-fluoro-2'-deoxynucleosides: fA, fC, fG, fU
        Available 2'-methoxyribonucleosides: mA, mC, mG, mU
        Available locked nucleosides: lA, lC_5me, lG, lT
        Available 2'-MOE nucleosides: moeA, moeC_5me, moeG, moeT

        Available phosphate modifications: po - phosphate, ps - phosphorothyoate (po by default)
        """
    modification_error = []

    sequence_spl = utils.sequence_split(sequence)

    if sequence_spl[0] not in set(utils.modification_5_position + utils.nucleotide_any_position):
        modification_error.append("5'-Modification does not exist: " + sequence_spl[0])
    if len(sequence_spl) > 1:
        if sequence_spl[-1] not in set(utils.modification_3_position + utils.nucleotide_any_position):
            modification_error.append("3'-Modification does not exist: " + sequence_spl[-1])
        for i in range(len(sequence_spl)-1):
            if i == 0: continue
            if sequence_spl[i] not in set( utils.modification_int_position +
                                           utils.modification_phosphorus +
                                           utils.nucleotide_any_position ):
                modification_error.append("Internal modification does not exist: " + sequence_spl[i] + " at position " + str(i+1))
            if (sequence_spl[i] in utils.modification_phosphorus) and (sequence_spl[i+1] in utils.modification_phosphorus):
                modification_error.append("Two phosphate residues at positions " + str(i+1) + " and " + str(i+2) + " cannot be nearby")
    if modification_error:
        raise ValidationError(modification_error)
    else:
        return sequence