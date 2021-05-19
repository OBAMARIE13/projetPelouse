from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Prestations)
class PrestationsAdmin(admin.ModelAdmin):
    list_display = ('icone', 'titre', 'description', 'date_add', 'date_update', 'status')

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('gallerie', 'sous_titre', 'description', 'date_add', 'date_update', 'status')


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('image', 'nom', 'email', 'sujet', 'message', 'date_add', 'date_update', 'status')


@admin.register(models.Gallerie)
class GallerieAdmin(admin.ModelAdmin):
    list_display = ('image', 'libelle', 'categorie', 'date_add', 'date_update', 'status')
    

@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_add', 'date_update', 'status')
    
    
@admin.register(models.Pelouse_care)
class Pelouse_careAdmin(admin.ModelAdmin):
    list_display = ('nonsaison', 'image', 'description', 'date_add', 'date_update', 'status')
