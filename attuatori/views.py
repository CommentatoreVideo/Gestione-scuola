from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from django.http import HttpResponseNotFound
from gestioneScuola.models import Materia, Voto, Quadrimestre,Compito

@login_required(login_url='login/') 
def aggiungiVoto(request):
  quad=Quadrimestre.objects.get(id=1).quadrimestre
  materia=request.POST.get("materia")
  tipo=request.POST.get("tipologia")
  voto=float(request.POST.get("voto"))
  media=request.POST.get("media")
  if(media=="Si"):
    media=1
  else:
    media=0
  data=request.POST.get("data")
  v=Voto(tipo=tipo,voto=voto,media=media,giorno=data)
  v.save()
  indice=v.id
  materiaO=Materia.objects.get(nome=materia)
  if(quad==1):
    materiaO.voti1=materiaO.voti1+str(indice)+","
  else:
    materiaO.voti2=materiaO.voti2+str(indice)+","
  materiaO.save()
  
  Materia.objects.get(nome=materia).save()
  return render(request,"index.html")

@login_required(login_url='login/')  
def rimuoviVoto(request):
  quad=Quadrimestre.objects.get(id=1).quadrimestre
  indice=request.POST.get("id")
  try:
    Voto.objects.get(id=indice).delete()
    materie=Materia.objects.all()
    for materia in materie:
      materia.rimuoviVoto(indice,quad)
  except:
    pass
  return render(request,"rimuoviVoto.html")
  
@login_required(login_url='/login/')
def modificaVoto(request):
  materia=request.POST.get("materia")
  votoV=request.POST.get("voto")
  tipo=request.POST.get("tipo")
  media=request.POST.get("media")
  data=request.POST.get("data")
  indice=request.POST.get("indice")
  voto=Voto.objects.get(id=indice)
  voto.voto=votoV
  voto.tipo=tipo
  voto.media=media
  voto.giorno=data
  voto.save()
  return render(request,"modificaVoto.html")
  
@login_required(login_url='/login/')
def cambiaQuadrimestre(request):
  quadrimestre=request.POST.get("q")
  q=Quadrimestre.objects.get(id=1)
  q.quadrimestre=quadrimestre
  q.save()
  return render(request,"index.html")

  
@login_required(login_url='login/') 
def aggiungiCompito(request):
  materia=request.POST.get("materia")
  compito=request.POST.get("compito")
  data=request.POST.get("data")
  c=Compito(materia=materia,elenco=compito,scadenza=data)
  c.save()
  return render(request,"index.html")
  
def compitiDaFare(request):
  stringa=request.POST.get("stringa")
  gruppi=stringa.split("*")
  for i in range(len(gruppi)):
    gruppi[i]=gruppi[i].split("/")
  print(gruppi)
  for i in range(len(gruppi)):
    indice=gruppi[i][0]
    Compito.objects.get(id=indice).modifica(gruppi[i][1])
  #return HttpResponseNotFound("ciao")
  return render(request,"index.html")

def rimuoviCompito(request):
  indice=request.POST.get("id")
  try:
    Compito.objects.get(id=indice).delete()
  except:
    pass
  return render(request,"rimuoviCompito.html")