# Generated by Django 4.1.7 on 2023-03-06 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aemter',
            options={'ordering': ['maijahr', 'amt', 'reihenfolge', 'person']},
        ),
        migrations.AlterModelOptions(
            name='maijahr',
            options={'ordering': ['jahr']},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['nachname', 'vorname']},
        ),
        migrations.AddField(
            model_name='maijahr',
            name='preis_koenig',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='maijahr',
            name='preis_remmel',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='aemter',
            name='amt',
            field=models.CharField(choices=[('MK', 'Maikönig'), ('MN', 'Maikönigin'), ('VS', 'Vorsitzender'), ('VS2', '2. Vorsitzender'), ('SF1', '1. Schriftführer'), ('SF2', '2. Schriftführer'), ('SF3', '3. Schriftführer'), ('KS1', '1. Kassierer'), ('KS2', '2. Kassierer'), ('KS3', '3. Kassierer'), ('MH', 'Maihauptmann'), ('SPEV', 'Sonderposten EV'), ('EPEV', 'Ehrenposten EV'), ('RT', 'Reiter'), ('MR', 'Mairemmel'), ('HR', 'Hauptremmel'), ('BT', 'Baumträger'), ('CT', 'Cheftechniker'), ('TR', 'Techniker'), ('VD', 'Vorstand')], max_length=8),
        ),
    ]
