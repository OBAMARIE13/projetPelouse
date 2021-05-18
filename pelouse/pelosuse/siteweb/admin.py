from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("libele", "image", "titre", "date_add", "date_update", "status")

# model About
@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("option_about", "lien", "date_add", "date_update", "status")


# model option about
@admin.register(models.Option_about)
class Option_aboutAdmin(admin.ModelAdmin):
    list_display = ("description", "date_add", "date_update", "status")


# model Newletters
@admin.register(models.Newsletters)
class NewslettersAdmin(admin.ModelAdmin):
    # champs a afficher
    list_display = ("email", "date_add", "date_update", "status")

# model temoignage
@admin.register(models.Temoignages)
class TemoignagesAdmin(admin.ModelAdmin):
    # champs a afficher
    list_display = ("message", "photo", "poste", "date_add", "date_update", "status")


# model sociaux
@admin.register(models.Sociaux)
class SociauxAdmin(admin.ModelAdmin):
    # champs a afficher
    list_display = ("nom", "icone", "liens", "date_add", "date_update", "status")
