# Generated by Django 3.0.5 on 2023-07-18 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Etablissement', '0003_auto_20230718_1201'),
        ('Laboratoire', '0004_remove_laboratoire_etablissement'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratoire',
            name='Etablissement',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Etablissement.Etablissement'),
        ),
    ]