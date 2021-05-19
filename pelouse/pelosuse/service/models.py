from django.db import models

# Create your models here.
class Prestations(models.Model):
    icone = models.CharField(max_length = 200)
    titre = models.CharField(max_length = 200)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.titre

class Blog(models.Model):
    gallerie = models.ForeignKey('gallerie', on_delete=models.CASCADE, related_name='gallerie')
    sous_titre = models.CharField(max_length = 200)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.sous_titre

class Contact(models.Model):
    image = models.FileField(upload_to='image_service')
    nom = models.CharField(max_length = 200)
    email = models.EmailField()
    sujet = models.TextField()
    message = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nom


class Gallerie(models.Model):
    image = models.FileField(upload_to='image_service')
    libelle = models.CharField(max_length = 200)
    categorie = models.ForeignKey('categorie', on_delete=models.CASCADE, related_name='categorie')
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.libelle


class Categorie(models.Model):
    nom = models.CharField(max_length = 200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.nom
    
    
class Pelouse_care(models.Model):
    nonsaison = models.CharField(max_length = 200)
    image = models.FileField(upload_to='image_service')
    description = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    
    def __str__(self) -> str:
        return self.nonsaison