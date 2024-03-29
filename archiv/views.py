from django.http import HttpResponse
from django.template import loader
from itertools import groupby
from .models import Maijahr, Person, Aemter
from .helpers import Helpers
from .filters import PersonFilter
from datetime import datetime
from django.db.models.functions import Concat
from django.db.models import Q

from django.shortcuts import redirect

# Create your views here.
def home(request):
  template = loader.get_template('home.html')
  context = {
  }
  return HttpResponse(template.render(context, request))

def jahr(request, jahr):
  maijahr = Maijahr.objects.get(jahr=jahr)
  maijahre = Maijahr.objects.all()
  aemter= [{'amt': amt, 'personen':list(group)} for amt, group in groupby(maijahr.aemter_set.order_by('amt'), lambda x: x.amt)]
  ehrenmitglieder = Person.objects.filter(ehrenmitglied_ab__lte=str(maijahr.jahr)+'-12-31').filter(Q(todestag__isnull=True) | Q(todestag__gte=str(maijahr.jahr)+'-01-01')).order_by('ehrenmitglied_ab')

  order = [key for (key, value) in Aemter.AEMTER_CHOICES]
  aemter.sort(key= lambda x: order.index(x['amt']))

  try:
    maikoenig   = [x['personen'] for x in aemter if x['amt']=='MK'][0][0].person
    maikoenigin = [x['personen'] for x in aemter if x['amt']=='MN'][0][0].person
  except IndexError:
    maikoenig = None
    maikoenigin = None

  novd = not any(ele['amt'] == 'VD' for ele in aemter)

  template = loader.get_template('maijahr.html')
  context = {
    'maijahr': maijahr, 
    'maijahre' : maijahre,
    'maikoenig': maikoenig,
    'maikoenigin': maikoenigin,
    'aemter': aemter,
    'ehrenmitglieder': ehrenmitglieder,
    'keinVorstand': novd,
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
  #aemter = Aemter.objects.filter(person_id=id).order_by('amt')
  #aemter = [{'amt': x['Name'],'jahre':person.aemter_set.filter(amt__in=x['Aemter'])} for x in Aemter.AEMTER_GROUPS]
  
  aemter_maijahre = [{'amt': x['Name'],'jahre':[amt.maijahr for amt in person.aemter_set.filter(amt__in=x['Aemter'])]} for x in Aemter.AEMTER_GROUPS]
  
  if person.ehrenmitglied_ab:
    ehrenmitglied_jahre = Maijahr.objects.filter(jahr__gte=person.ehrenmitglied_ab.year).filter(jahr__lte=(person.todestag or datetime.today()).year)
    aemter_maijahre = [x | {'jahre': x['jahre'] if x['amt']  != 'Vorstand' else list(x['jahre']) + list(ehrenmitglied_jahre )} for x in aemter_maijahre]

  aemter = [x | {'jahre_str': ', '.join(Helpers.list_to_range_strs([jahr.jahr for jahr in x['jahre']]))
                 , 'jahre': x['jahre']}  for x in aemter_maijahre]

  template = loader.get_template('person.html')
  context = {
    'person': person,
    'aemter': aemter,
    'ehrennadel_maifest': person.ehrennadel and person.ehrennadel.month == 5 and person.ehrennadel.day == 1,
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

  vosis=[{'person': p['person'], 'jahre':[x.maijahr for x in list(p['jahre'])], 'jahre_str':', '.join(Helpers.ranges_to_strs(Helpers.to_ranges([x.maijahr.jahr for x in list(p['jahre'])])))} for p in vosis]

  vosis.sort(key= lambda x:x['jahre'][0].jahr )

  template = loader.get_template('vorsitzende.html')
  context = {
    'vorsitzende': vosis
  }
  return HttpResponse(template.render(context, request))

def suche(request):
  q = request.GET.get('q')

  try:
    Maijahr.objects.get (jahr=q)
    return redirect(jahr, q)
  except:
    q_split = q.split(' ')
    personen =  Person.objects.annotate(fullname=Concat('vorname','nachname','suchnamen')).all()
    for q1 in q_split:
      personen =  personen.filter(fullname__icontains=q1)  

    template = loader.get_template('suche.html')
    context = {
      'q': q,
      'ergebnis': personen,
    }
    return HttpResponse(template.render(context, request))