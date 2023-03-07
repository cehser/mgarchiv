from django.urls import path
from . import views

urlpatterns = [
  path('', views.jahre, name='jahre'),
  path('jahr/<int:jahr>', views.jahr, name='jahr'),
  path('person/<int:id>', views.person, name='person'),

  path('ehrennadeltraeger/', views.ehrennadeltraeger, name='ehrennadeltraeger'),
  path('maikoenigspaare/', views.maikoenigspaare, name='maikoenigspaare'),
  path('vorsitzende/', views.vorsitzende, name='vorsitzende'),

  path('suche/', views.suche, name="suche")
]