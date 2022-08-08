from random import choices
from django.db import models
roleuser = [
        ('admin','admin'),
        ('normaluser','normaluser')
        ]
class Utilisateur(models.Model):
    fb_id= models.CharField(max_length=200,primary_key=True)
    state = models.CharField(max_length=50,default='START',blank=True)
    query = models.CharField(max_length=200,blank=True)
    role = models.CharField(max_length=10,choices=roleuser,default='normaluser')
    def __str__(self):
        return f' {self.fb_id}'
class CentreMedical(models.Model):
    class Zones(models.IntegerChoices):
        zone1=1
        zone2=2
        zone3=3
        zone4=4
        zone5=5
        zone6=6
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=200)
    localisation = models.CharField(max_length=200)
    contact = models.CharField(max_length=200,blank=True)
    verifier = models.BooleanField()
    publier_par = models.ForeignKey(Utilisateur,on_delete=models.CASCADE) 
    zone = models.IntegerField(choices=Zones.choices,default=Zones.zone1)

class Pharmacie(models.Model):
    class Zones(models.IntegerChoices):
        zone1=1
        zone2=2
        zone3=3
        zone4=4
        zone5=5
        zone6=6
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=200)
    localisation = models.CharField(max_length=200)
    contact = models.CharField(max_length=200,blank=True)
    verifier = models.BooleanField()
    publier_par = models.ForeignKey(Utilisateur,on_delete=models.CASCADE) 
    zone = models.IntegerField(choices=Zones.choices,default=Zones.zone1)
class Conseil(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField()
