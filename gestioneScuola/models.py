from django.db import models

# Create your models here.
class Materia(models.Model):
  nome=models.CharField(max_length=50)
  colore=models.CharField(max_length=100)
  voti1=models.CharField(max_length=5000,blank=True,default="")
  voti2=models.CharField(max_length=5000,blank=True,default="")
  
  def getVoti(self,quadrimestre):
    if(quadrimestre==1):
      if(self.voti1==""):
        return -1
      else:
        vettore=self.voti1.split(",")
        vettore.pop()
        return vettore
    else:
      if(self.voti2==""):
        return -1
      else:
        vettore=self.voti2.split(",")
        vettore.pop()
        return vettore
  
  def getMedia(self,quadrimestre):
    voti=self.voti1.split(",") if quadrimestre==1 else self.voti2.split(",")
    if(len(voti)==1 and voti[0]==''):
      return 0
    voti.pop() # Rimuovo l'elemento finale finto
    for i in range(len(voti)):
      voti[i]=float(voti[i])
    somma=0
    sommati=0
    for voto in voti:
      if(Voto.objects.get(id=voto).media==1):
        somma+=Voto.objects.get(id=voto).voto
        sommati+=1
    return somma/sommati
  def getInfoGrafico(self,quadrimestre):
    media=self.getMedia(quadrimestre)
    nome=self.nome
    colore=self.colore
    return {"media":media,"nome":nome,"colore":colore}
  def rimuoviVoto(self,indice,quad):
    voti=self.getVoti(quad)
    stringa=""
    for voto in voti:
      if(int(voto)!=int(indice)):
        stringa+=voto+","
    self.voti1=stringa
    self.save()
    
    
class Voto(models.Model):
  voto=models.FloatField() # Voto effettivo
  tipo=models.CharField(max_length=100) # Scritto/orale/pratica
  media=models.IntegerField() # Fa media
  giorno=models.CharField(max_length=100) # Giorno
  def getInformazioni(self):
    return [self.voto,self.tipo,self.media,self.giorno]
    
class Quadrimestre(models.Model):
  quadrimestre=models.IntegerField() # Numero del quadrimestre