from django.db import models

from . import validators


class Sequence(models.Model):

    sequence = models.CharField(verbose_name="Sequence, 5'->3'",
                                max_length=300)

    absorbance260 = models.FloatField(verbose_name='Absorbance at 260 nm', blank=True, null=True)
    volume = models.FloatField(verbose_name='Volume, mL', blank=True, null=True)

    mv_conc = models.FloatField(verbose_name='Na+ Conc', blank=False, null=False, default=50)
    dv_conc = models.FloatField(verbose_name='Mg2+ Conc', blank=False, null=False, default=0)
    dntp_conc = models.FloatField(verbose_name='dNTPs Conc', blank=False, null=False, default=0)
    dna_conc = models.FloatField(verbose_name='Oligo Conc', blank=False, null=False, default=0.25)


    class Meta:
        verbose_name_plural = 'Sequences'
        verbose_name = 'Sequence'
        ordering = ['pk']
