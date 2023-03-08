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
  AEMTER_GROUPS = [
    {
      'Name': 'Maikönig',
      'Aemter': ['MK'],
    },
    {
      'Name': 'Maikönigin',
      'Aemter': ['MN'],
    },
    {
      'Name': 'Vorsitzender',
      'Aemter': ['VS'],
    },
    {
      'Name': '2. Vorsitzender',
      'Aemter': ['VS2'],
    },
    {
      'Name': '1. Schriftführer', 
      'Aemter': ['SF1'],
    },
    {
      'Name': '1. Kassierer', 
      'Aemter': ['KS1'],
    },
    {
      'Name': '2. Schriftführer', 
      'Aemter': ['SF2'],
    },
    {
      'Name': '2. Kassierer', 
      'Aemter': ['KS2'],
    },
    {
      'Name': '3. Schriftführer', 
      'Aemter': ['SF3'],
    },
    {
      'Name': '3. Kassierer', 
      'Aemter': ['KS3'],
    },
    {
      'Name': 'Maihauptmann', 
      'Aemter': ['MH'],
    },
    {
      'Name': 'Ehrenposten EV', 
      'Aemter': ['EPEV'],
    },
    {
      'Name': 'Sonderposten EV', 
      'Aemter': ['SPEV'],
    },
    {
      'Name': 'Vorstand', 
      'Aemter': ['MK', 'VS', 'VS2', 'SF1', 'SF2', 'SF3', 'KS1', 'KS2', 'KS3', 'MH','EPEV', 'SPEV', 'HR', 'VD'],
    },
    {
      'Name': 'Reiter', 
      'Aemter': ['MH', 'RT'],
    },
    {
      'Name': 'Hauptremmel', 
      'Aemter': ['HR'],
    },
    {
      'Name': 'Mairemmel', 
      'Aemter': ['HR', 'MR'],
    },
    {
      'Name': 'Baumträger', 
      'Aemter': ['BT'],
    },
    {
      'Name': 'Cheftechniker', 
      'Aemter': ['CT'],
    },
    {
      'Name': 'Techniker', 
      'Aemter': ['TR'],
    },
  ]
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
    ("VD", "Vorstand"),
    ("RT", "Reiter"),
    ("HR", "Hauptremmel"),
    ("MR", "Mairemmel"),
    ("BT", "Baumträger"),
    ("CT", "Cheftechniker"),
    ("TR", "Techniker"),
  ]
  person      = models.ForeignKey(Person, on_delete=models.CASCADE)
  maijahr     = models.ForeignKey(Maijahr, on_delete=models.CASCADE)
  amt         = models.CharField(max_length=8,choices=AEMTER_CHOICES)
  reihenfolge = models.SmallIntegerField(blank=True, null=True)

  class Meta:
    ordering = ['maijahr', 'amt', 'reihenfolge', 'person']

  def __str__(self):
    return str(self.maijahr) + ' ' + self.amt +  ' ' + str(self.person)
    