# Generated by Django 4.1.7 on 2023-03-25 20:41

from django.db import migrations, models
import oligocalc.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.CharField(max_length=300, validators=[oligocalc.validators.validate_seq], verbose_name="Sequence, 5'->3'")),
                ('absorbance260', models.FloatField(blank=True, null=True, verbose_name='Absorbance at 260 nm')),
                ('volume', models.FloatField(blank=True, null=True, verbose_name='Volume, mL')),
                ('dilution_factor', models.FloatField(blank=True, null=True, verbose_name='Dilution Factor')),
            ],
            options={
                'verbose_name': 'Sequence',
                'verbose_name_plural': 'Sequences',
                'ordering': ['pk'],
            },
        ),
    ]
