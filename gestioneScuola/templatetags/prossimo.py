from django import template

register = template.Library()

@register.filter
def prossimo(elenco, indice):
  print(indice)
  print(elenco)
  return elenco[int(indice)+1] # Ritorna un elemento di una lista