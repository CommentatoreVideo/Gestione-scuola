from django.contrib import admin

# Register your models here.
from .models import Materia,Voto

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
  pass

@admin.register(Voto)
class VotoAdmin(admin.ModelAdmin):
  pass