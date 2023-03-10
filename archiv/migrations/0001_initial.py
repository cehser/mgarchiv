# Generated by Django 4.1.7 on 2023-03-04 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aemter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amt', models.CharField(choices=[('MK', 'Maikönig'), ('MN', 'Maikönigin'), ('VS', 'Vorsiztender'), ('VS2', '2. Vorsitzender'), ('SF1', '1. Schriftführer'), ('SF2', '2. Schriftführer'), ('SF3', '3. Schriftführer'), ('KS1', '1. Kassierer'), ('KS2', '2. Kassierer'), ('KS3', '3. Kassierer'), ('MH', 'Maihauptmann'), ('SPEV', 'Sonderposten EV'), ('RT', 'Reiter'), ('MR', 'Mairemmel'), ('HR', 'Hauptremmel'), ('BT', 'Baumträger'), ('CT', 'Cheftechniker'), ('TR', 'Techniker')], max_length=8)),
                ('reihenfolge', models.SmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vorname', models.CharField(max_length=255)),
                ('nachname', models.CharField(max_length=255)),
                ('nachname_heirat', models.CharField(blank=True, max_length=255, null=True)),
                ('ehrennadel', models.DateField(blank=True, null=True)),
                ('todestag', models.DateField(blank=True, null=True)),
                ('ehrenmitglied_ab', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maijahr',
            fields=[
                ('jahr', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('url_vorstandsfoto', models.URLField(blank=True, null=True)),
                ('url_foto_maikoenigspaar', models.URLField(blank=True, null=True)),
                ('amtstraeger', models.ManyToManyField(through='archiv.Aemter', to='archiv.person')),
            ],
        ),
        migrations.AddField(
            model_name='aemter',
            name='maijahr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archiv.maijahr'),
        ),
        migrations.AddField(
            model_name='aemter',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archiv.person'),
        ),
    ]
