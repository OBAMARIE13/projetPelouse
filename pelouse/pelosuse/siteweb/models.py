from django.db import models

# Create your models here.
class Banner(models.Model):
    libele = models.CharField(max_length = 200)
    image = models.FileField(upload_to='image_site')
    titre = models.CharField(max_length = 200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.libele

class About(models.Model):
    option_about = models.ForeignKey('option_about', on_delete=models.CASCADE, related_name='option')
    lien = models.URLField(max_length=200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.lien



class Option_about(models.Model):
    description = models.CharField(max_length = 200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.description


class Newsletters(models.Model):
    email = models.EmailField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.email

class Temoignages(models.Model):
    message = models.TextField()
    photo = models.FileField()
    poste = models.CharField(max_length = 200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.poste


class Sociaux(models.Model):
    nom = models.CharField(max_length = 200)
    icone = models.FileField(upload_to='image_site')
    liens = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.nom


class Website(models.Model):
    nondusite = models.CharField(max_length = 200)
    titre_temoignage = models.CharField(max_length = 200)
    titre_about = models.CharField(max_length = 200)
    description_about = models.TextField()
    titre_pelousecare = models.CharField(max_length = 200)
    mail = models.EmailField()
    description_service = models.TextField()
    titre_service = models.CharField(max_length = 200)
    description_contact = models.TextField()
    phone = models.CharField(max_length = 200)
    adresse = models.CharField(max_length = 200)
    site = models.CharField(max_length = 200)
    copirygth = models.CharField(max_length = 200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True) 