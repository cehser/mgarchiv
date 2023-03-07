from django.db import models

# Create your models here.
class Person(models.Model):
  vorname           = models.CharField(max_length=255)
  nachname          = models.CharField(max_length=255)
  nachname_heirat   = models.CharField(max_length=255, blank=True, null=True)
  ehrennadel        = models.DateField(blank=True, null=True)
  todestag          = models.DateField(blank=True, null=True)
  ehrenmitglied_ab  = models.DateField(blank=True, null=True)

  class Meta:
    ordering = ['nachname', 'vorname']

  def __str__(self):
      return self.vorname + ' ' + self.nachname

class Maijahr(models.Model):
  jahr                      = models.PositiveSmallIntegerField(primary_key=True)
  url_vorstandsfoto         = models.URLField(blank=True, null=True)
  url_foto_maikoenigspaar   = models.URLField(blank=True, null=True)
  preis_koenig              = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
  preis_remmel              = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
  amtstraeger               = models.ManyToManyField(
        Person,
        through='Aemter',
    )

  class Meta:
    ordering = ['jahr']


  def __str__(self):
      return str(self.jahr)


class Aemter(models.Model):
  AEMTER_CHOICES = [
    ("MK", "Maikönig"),
    ("MN", "Maikönigin"),
    ("VS", "Vorsitzender"),
    ("VS2", "2. Vorsitzender"),
    ("SF1", "1. Schriftführer"),
    ("SF2", "2. Schriftführer"),
    ("SF3", "3. Schriftführer"),
    ("KS1", "1. Kassierer"),
    ("KS2", "2. Kassierer"),
    ("KS3", "3. Kassierer"),
    ("MH", "Maihauptmann"),
    ("SPEV", "Sonderposten EV"),
    ("EPEV", "Ehrenposten EV"),
    ("RT", "Reiter"),
    ("MR", "Mairemmel"),
    ("HR", "Hauptremmel"),
    ("BT", "Baumträger"),
    ("CT", "Cheftechniker"),
    ("TR", "Techniker"),
    ("VD", "Vorstand"),
  ]
  person      = models.ForeignKey(Person, on_delete=models.CASCADE)
  maijahr     = models.ForeignKey(Maijahr, on_delete=models.CASCADE)
  amt         = models.CharField(max_length=8,choices=AEMTER_CHOICES)
  reihenfolge = models.SmallIntegerField(blank=True, null=True)

  class Meta:
    ordering = ['maijahr', 'amt', 'reihenfolge', 'person']

  def __str__(self):
    return str(self.maijahr) + ' ' + self.amt +  ' ' + str(self.person)
    