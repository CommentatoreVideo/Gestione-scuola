from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from django.http import HttpResponseNotFound
from .models import Materia, Voto, Quadrimestre,Compito

@login_required(login_url='login/')
def index(request):
  quad=Quadrimestre.objects.get(id=1).quadrimestre
  materie=Materia.objects.all()
  elencoVoti=Voto.objects.all()
  medie=[]
  nomi=[]
  colori=[]
  voti=[]
  for materia in materie:
    info=materia.getInfoGrafico(quad)
    medie.append(info["media"])
    nomi.append(info["nome"])
    colori.append(info["colore"])
    votiMateria=materia.getVoti(quad)
    if(votiMateria!=-1):
      vo=[]
      for i in range(len(votiMateria)):
        votiMateria[i]=int(votiMateria[i])
        voto=Voto.objects.get(id=votiMateria[i])
        vo.append(voto)
      vo.sort(key = lambda v: datetime.strptime(str(v.giorno), '%d/%m/%Y')) 
      provvisorio=[]
      for v in vo: 
        provvisorio.append(v.getInformazioni())
      voti.append(provvisorio)
    else:
      voti.append(-1)
  context={"nomiMaterieMedie":nomi,"votiMaterieMedie":medie,"coloriMaterieMedie":colori,"votiMaterie":voti,"quad":quad,"indice":True}
  return render(request,"index.html",context)
  
@login_required(login_url='/login/')
def aggiungiVoto(request):
  data=date.today().strftime("%d/%m/%Y")
  quad=Quadrimestre.objects.get(id=1).quadrimestre
  materie=Materia.objects.all()
  elencoMaterie=[]
  for i in range(len(materie)):
    elencoMaterie.append(materie[i].nome)
  context={"elencoMaterie":elencoMaterie,"data":data,"quad":quad}
  return render(request,"aggiungiVoto.html",context)

  
@login_required(login_url='/login/')
def rimuoviVoto(request):
  righe=[]
  quad=Quadrimestre.objects.get(id=1).quadrimestre
  materie=Materia.objects.all()
  for materia in materie:
    riga=[]
    indiciVoti=materia.getVoti(quad)
    voti=[]
    if(indiciVoti!=-1):
      riga.append(materia.nome)
      for i in indiciVoti:
        oggetto=Voto.objects.get(id=i)
        voto=oggetto.voto
        tipo=oggetto.tipo
        media=oggetto.media
        giorno=oggetto.giorno
        if(media==1):
          media="Si"
        else:
          media="No"
        voti.append([voto,tipo,media,giorno,i])
      riga.append(voti)
      righe.append(riga)
  return render(request,"rimuoviVoto.html",{"righe":righe,"quad":quad})
  
@login_required(login_url='/login/')
def modificaVoto(request):
  quad=Quadrimestre.objects.get(id=1).quadrimestre
  righe=[]
  elencoMaterie=[]
  materie=Materia.objects.all()
  for materia in materie:
    riga=[]
    indiciVoti=materia.getVoti(quad)
    voti=[]
    elencoMaterie.append(materia.nome)
    if(indiciVoti!=-1):
      riga.append(materia.nome)
      for i in indiciVoti:
        oggetto=Voto.objects.get(id=i)
        voto=oggetto.voto
        tipo=oggetto.tipo
        media=oggetto.media
        giorno=oggetto.giorno
        if(media==1):
          media="Si"
        else:
          media="No"
        voti.append([voto,tipo,media,giorno,i])
      riga.append(voti)
      righe.append(riga)
  return render(request,"modificaVoto.html",{"righe":righe,"materie":elencoMaterie,"quad":quad})
  
@login_required(login_url='/login/')
def cambiaQuadrimestre(request):
  quadrimestre=request.POST.get("q")
  q=Quadrimestre.objects.get(id=1)
  q.quadrimestre=quadrimestre
  q.save()
  return render(request,"index.html")
  
@login_required(login_url='/login/')
def aggiungiCompito(request):
  data=date.today().strftime("%d/%m/%Y")
  quad=Quadrimestre.objects.get(id=1).quadrimestre
  materie=Materia.objects.all()
  elencoMaterie=[]
  for i in range(len(materie)):
    elencoMaterie.append(materie[i].nome)
  context={"elencoMaterie":elencoMaterie,"data":data,"quad":quad}
  return render(request,"aggiungiCompito.html",context)

@login_required(login_url='/login/')
def compitiDaFare(request):
  righe=[]
  elencoMaterie=[]
  quad=Quadrimestre.objects.get(id=1).quadrimestre
  compiti=Compito.objects.all()
  for compito in compiti:
    riga=[]
    riga.append(compito.materia)
    riga.append(compito.scadenza)
    riga.append(compito.elenco.split("*"))
    riga.append(compito.id)
    righe.append(riga)
  return render(request,"compitiDaFare.html",{"righe":righe,"quad":quad})


def rimuoviCompito(request):
  righe=[]
  quad=Quadrimestre.objects.get(id=1).quadrimestre
  compiti=Compito.objects.all()
  for compito in compiti:
    riga=[]
    riga.append(compito.materia)
    riga.append(compito.scadenza)
    riga.append(compito.elenco.split("*"))
    riga.append(compito.id)
    righe.append(riga)
  print(righe)
  
  return render(request,"rimuoviCompito.html",{"righe":righe})