# Generated by Django 3.0.5 on 2023-07-20 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Visiteur', '0002_alter_visiteur_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visiteur',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
