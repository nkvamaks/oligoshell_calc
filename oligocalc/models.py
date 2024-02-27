from django.db import models


class Oligo(models.Model):
    OLIGO_CHOICES = [('ss', 'ss'), ('ds', 'ds')]
    TARGET_CHOICES = [('dna', 'DNA')]

    sequence = models.CharField(verbose_name="Sequence, 5'->3'", max_length=300)
    oligo_type = models.CharField(verbose_name='oligonucleotide type', max_length=10, choices=OLIGO_CHOICES, default='ss')
    target = models.CharField(verbose_name='Target type', max_length=50, choices=TARGET_CHOICES, default='dna')
    absorbance260 = models.FloatField(verbose_name='Absorbance at 260 nm (10 mm)', blank=True, null=True)
    volume = models.FloatField(verbose_name='Volume, mL', blank=True, null=True)
    mv_conc = models.FloatField(verbose_name='Na+ Conc', blank=False, null=False, default=50)
    dv_conc = models.FloatField(verbose_name='Mg2+ Conc', blank=False, null=False, default=0)
    dntp_conc = models.FloatField(verbose_name='dNTPs Conc', blank=False, null=False, default=0)
    dna_conc = models.FloatField(verbose_name='Oligo Conc', blank=False, null=False, default=0.25)

    class Meta:
        verbose_name_plural = 'Oligos'
        verbose_name = 'Oligo'
