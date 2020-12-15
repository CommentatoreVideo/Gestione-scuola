from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name="attuatori"
urlpatterns=[
  path('aggiungiVoto/',views.aggiungiVoto,name="aggiungiVoto"),
  path('rimuoviVoto/',views.rimuoviVoto,name="rimuoviVoto"),
  path('modificaVoto/',views.modificaVoto,name="modificaVoto"),
  path('aggiungiCompito/',views.aggiungiCompito,name='aggiungiCompito'),
  path('compitiDaFare/',views.compitiDaFare,name='compitiDaFare'),
  path('rimuoviCompito/',views.rimuoviCompito,name='rimuoviCompito'),
  path('cambiaQuadrimestre/',views.cambiaQuadrimestre,name='cambiaQuadrimestre')
]