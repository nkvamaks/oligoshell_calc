from django.db import models

from . import validators


class Sequence(models.Model):

    sequence = models.CharField(verbose_name="Sequence, 5'->3'",
                                max_length=300)

    absorbance260 = models.FloatField(verbose_name='Absorbance at 260 nm', blank=True, null=True)
    volume = models.FloatField(verbose_name='Volume, mL', blank=True, null=True)
    dilution_factor = models.FloatField(verbose_name='Dilution Factor', blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Sequences'
        verbose_name = 'Sequence'
        ordering = ['pk']
