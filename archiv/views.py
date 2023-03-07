from django.http import HttpResponse
from django.template import loader
from itertools import groupby
from .models import Maijahr, Person, Aemter
from .helpers import Helpers

# Create your views here.

def jahr(request, jahr):
  maijahr = Maijahr.objects.get(jahr=jahr)
  template = loader.get_template('maijahr.html')
  context = {
    'maijahr': maijahr,
  }
  return HttpResponse(template.render(context, request))

def jahre(request):
  maijahre = Maijahr.objects.all().values()
  template = loader.get_template('maijahre.html')
  context = {
    'maijahre': maijahre,
  }
  return HttpResponse(template.render(context, request))

def person(request, id):
  person = Person.objects.get(id=id)
  template = loader.get_template('person.html')
  context = {
    'person': person,
  }
  return HttpResponse(template.render(context, request))

def ehrennadeltraeger(request):
  ehrennadeltraeger = Person.objects.exclude(ehrennadel__isnull=True).order_by('ehrennadel')
  template = loader.get_template('ehrennadeltraeger.html')
  context = {
    'ehrennadeltraeger': [{'jahr': jahr, 'personen':list(group)} for jahr, group in groupby(ehrennadeltraeger, lambda x: x.ehrennadel.year)]
  }
  return HttpResponse(template.render(context, request))

def maikoenigspaare(request):
  maikoenigspaare = Aemter.objects.filter(amt__in=['MK','MN'])
  template = loader.get_template('maikoenigspaare.html')
  context = {
    'maikoenigspaare': [{'jahr': jahr, 'paar':list(group)} for jahr, group in groupby(maikoenigspaare, lambda x: x.maijahr.jahr)],
  }
  return HttpResponse(template.render(context, request))

def vorsitzende(request):
  vosis = Aemter.objects.filter(amt='VS').filter(maijahr__gte='1927').order_by('person_id', 'maijahr_id')
  vosis=[{'person': person, 'jahre':list(aemter)} for person, aemter in groupby(vosis, lambda x: x.person)]

  vosis=[{'person': p['person'], 'jahre':p['jahre'], 'jahre_str':', '.join(Helpers.ranges_to_strs(Helpers.to_ranges([x.maijahr.jahr for x in list(p['jahre'])])))} for p in vosis]

  vosis.sort(key= lambda x:x['jahre'][0].maijahr_id )

  template = loader.get_template('vorsitzende.html')
  context = {
    'vorsitzende': vosis
  }
  return HttpResponse(template.render(context, request))