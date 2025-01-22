from django.db import models
from django.urls import reverse

from django.conf import settings


class Oligo(models.Model):
    OLIGO_CHOICES = [('ss', 'ss'), ('ds', 'ds')]
    TARGET_CHOICES = [('dna', 'DNA')]

    sequence = models.CharField(verbose_name="Sequence, 5'->3'", max_length=400)
    oligo_type = models.CharField(verbose_name='oligonucleotide type', max_length=10, choices=OLIGO_CHOICES, default='ss')
    target = models.CharField(verbose_name='Target type', max_length=50, choices=TARGET_CHOICES, default='dna')
    absorbance260 = models.FloatField(verbose_name='Absorbance at 260 nm (10 mm)', blank=True, null=True)
    volume = models.FloatField(verbose_name='Volume, mL', blank=True, null=True)
    mv_conc = models.FloatField(verbose_name='Na+ Conc', blank=False, null=False, default=50)
    dv_conc = models.FloatField(verbose_name='Mg2+ Conc', blank=False, null=False, default=3)
    dntp_conc = models.FloatField(verbose_name='dNTPs Conc', blank=False, null=False, default=0.8)
    dna_conc = models.FloatField(verbose_name='Oligo Conc', blank=False, null=False, default=0.2)

    class Meta:
        verbose_name_plural = 'Oligos'
        verbose_name = 'Oligo'


class TaqManFind(models.Model):
    PROBE_DYE_CHOICES = [
        ('NO-ANY', 'No any'),
        ('FAM-BHQ1', 'FAM - BHQ1'),
        ('HEX-BHQ1', 'HEX - BHQ1'),
        ('FAM-MGB', 'FAM - MGB-ECLIPSE (Thermo)'),
        ('VIC-MGB', 'VIC - MGB-ECLIPSE (Thermo)'),
        ('JUN-QSY', 'JUN - QSY (Thermo)'),
        ('TexRd-BHQ2', 'TexRd - BHQ2 (IDT)'),
        ('Cy5-BHQ2', 'Cy5 - BHQ2 (IDT)')
    ]
    fasta = models.TextField(verbose_name="Sequence in FASTA format", blank=False, null=False)
    primer1 = models.FloatField(verbose_name='Molecular weight of Primer 1', blank=False, null=False)
    primer2 = models.FloatField(verbose_name='Molecular weight of Primer 2', blank=False, null=False)
    probe = models.FloatField(verbose_name='Molecular weight of Probe', blank=False, null=False)
    probe_dye = models.CharField(verbose_name='Dye', max_length=50, choices=PROBE_DYE_CHOICES, default='FAM-BHQ1')
    amp_size = models.IntegerField(verbose_name='Amplicon length', blank=False, null=False)

    def get_absolute_url(self):
        return reverse('oligocalc:taqman_find')


# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # birthday = models.DateTimeField(blank=True, null=True)
    # photo = models.ImageField(upload_to="user/%Y/%m/%d/", blank=True)
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # def __str__(self):
    #     return f'{self.user.username} Profile'
