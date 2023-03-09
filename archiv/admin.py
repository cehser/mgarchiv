from django.contrib import admin
from .models import Person,Maijahr,Aemter

class AemterInline(admin.TabularInline):
  model = Aemter
  extra = 1

class PersonenInline(admin.TabularInline):
  model = Person
  extra = 1

class PersonAdmin(admin.ModelAdmin):
  inlines = [AemterInline]
  search_fields = ['vorname','nachname', 'suchnamen']

class MaijahrAdmin(admin.ModelAdmin):
  inlines = [AemterInline]

# Register your models here.
admin.site.register(Person, PersonAdmin)
admin.site.register(Maijahr, MaijahrAdmin)
# admin.site.register(Aemter)