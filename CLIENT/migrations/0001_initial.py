# Generated by Django 3.2.12 on 2022-11-06 09:40

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumClient', models.IntegerField(default=0)),
                ('Nom', models.CharField(max_length=100)),
                ('Prenom', models.CharField(max_length=100)),
                ('DateNaissance', models.DateField()),
                ('Addresse', models.CharField(max_length=100)),
                ('ScanPermis', models.FileField(blank=True, null=True, upload_to='STATIC/Permis/%Y%M%D/')),
                ('Ref_CIN', models.CharField(max_length=100)),
                ('Scan_CIN', models.FileField(blank=True, null=True, upload_to='STATIC/CIN/%Y%M%D/')),
                ('TEL', models.CharField(default='00', max_length=100)),
                ('DateCreationClient', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Creation client')),
            ],
            options={
                'verbose_name': 'Client',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Nationalite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RefProduit', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypeAvenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DescriptionAvenant', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypePaiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypePermis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypePermis', models.CharField(max_length=100)),
                ('DescriptionTypePermis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Matricule', models.CharField(max_length=100)),
                ('RefMarque', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Permis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReferencePermis', models.CharField(max_length=100)),
                ('DateLivraison', models.DateField(default=datetime.date(1900, 1, 1))),
                ('DateFinValidite', models.DateField(default=datetime.date(1900, 1, 1))),
                ('CategoriePermis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CLIENT.typepermis')),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DescPaiement', models.CharField(default='', max_length=100)),
                ('DatePaiement', models.DateField()),
                ('DateOperation', models.DateField()),
                ('MontantPaiement', models.FloatField(default=0)),
                ('TypePaiement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CLIENT.typepaiement')),
            ],
        ),
        migrations.CreateModel(
            name='Contrat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumeroPolice', models.CharField(max_length=100)),
                ('DateDebutEffet', models.DateField()),
                ('DateFineffet', models.DateField()),
                ('DateAnnulation', models.DateField()),
                ('MontantPrime', models.FloatField(default=0)),
                ('MontantPAYE', models.FloatField(default=0)),
                ('RESTE', models.FloatField(default=0)),
                ('NumeroAttestation', models.IntegerField(default=0)),
                ('StatutPaiement', models.BinaryField(default=0)),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CLIENT.client')),
                ('Paiement', models.ManyToManyField(to='CLIENT.Paiement')),
                ('Produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CLIENT.produit')),
                ('Vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CLIENT.vehicule')),
            ],
            options={
                'verbose_name': 'Contrat',
                'ordering': ['NumeroPolice'],
            },
        ),
        migrations.AddField(
            model_name='client',
            name='Nationalite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CLIENT.nationalite'),
        ),
        migrations.AddField(
            model_name='client',
            name='Ref_Permis_conduire',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='CLIENT.permis'),
        ),
    ]
