from meta.views import Meta


def get_about_meta(request):
    return Meta(
        title="About Oligonucleotide Properties Calculator",
        description="OligoShell is a free online calculator for oligonucleotide properties. It can calculate melting temperatures (Tm) of duplexes, the exact mass, molecular weight, ESI series and MS/MS fragments, extinction coefficients and it can also be used for quantification.",
        keywords=['oligonucleotide', 'melting temperature', 'Tm', 'MGB', 'minor groove binder', 'exact mass', 'molecular weight', 'ESI', 'MS/MS', 'extinction coefficient', 'DNA', 'RNA', 'PMO', 'morpholino', 'modified', 'therapeutic'],
    )


def get_contact_meta(request):
    return Meta(
        title="Contact OligoShell: Get Support and Information",
        description="Need help with OligoShell, our free online oligonucleotide properties calculator? Contact our team for support, feedback, or questions. We're here to assist you!",
        keywords=['contact', 'support', 'oligonucleotide calculator', 'help', 'information', 'feedback'],
    )


def get_modifications_meta(request):
    return Meta(
        title="Oligonucleotide Modifications: Explore Options with OligoShell",
        description="Discover a range of oligonucleotide modifications and their codes in OligoShell. Our free online calculator supports calculations for modified oligonucleotides.",
        keywords=['oligonucleotide modifications', 'modified oligonucleotides', 'oligonucleotide calculator', 'melting temperature', 'Tm', 'chemical modifications', 'DNA modifications', 'RNA modifications', 'PMO modifications', 'therapeutic oligonucleotides', 'carboxyfluoresceine', 'FAM', 'carboxytetramethylrhodamine', 'TAMRA', 'cyanine', 'dye', 'Cy5', 'alkyne', 'azide', 'click'],
    )
