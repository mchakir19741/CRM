from django.db import models
from django.utils import timezone 
import datetime 


# Create your models here.

class TypePermis(models.Model):
    TypePermis = models.CharField(max_length=100)
    DescriptionTypePermis = models.TextField()

    def __str__(self):
        return self.TypePermis


class Permis(models.Model):
    ReferencePermis = models.CharField(max_length=100)
    CategoriePermis = models.ForeignKey('TypePermis', on_delete=models.CASCADE)
    DateLivraison   = models.DateField(default = datetime.date(1900, 1, 1) )
    DateFinValidite = models.DateField(default = datetime.date(1900, 1, 1) )
    
    def __str__(self):
        return self.ReferencePermis



class Nationalite(models.Model):
    Nom = models.CharField(max_length=100)

    def __str__(self):
        return self.Nom

        
class Client(models.Model):
    NumClient = models.IntegerField(default=0)
    Nom    = models.CharField(max_length=100) 
    Prenom = models.CharField(max_length=100) 
    DateNaissance = models.DateField()
    Addresse = models.CharField(max_length=100) 
    Nationalite= models.ForeignKey('Nationalite', on_delete=models.CASCADE)
    Ref_Permis_conduire=models.OneToOneField('Permis', on_delete=models.CASCADE)
    ScanPermis=models.FileField(upload_to="STATIC/Permis/%Y%M%D/",blank=True, null=True)
    Ref_CIN = models.CharField(max_length=100) 
    Scan_CIN = models.FileField(upload_to="STATIC/CIN/%Y%M%D/",blank=True, null=True)
    TEL = models.CharField(max_length=100, default="00")
    DateCreationClient = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date Creation client")
    
    class Meta:
        verbose_name = "Client"
        ordering = ['id']
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.Nom + "  " + self.Prenom 


class TypeAvenant (models.Model):
    DescriptionAvenant=models.CharField(max_length=100)

    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.DescriptionAvenant



class Produit (models.Model):
    RefProduit = models.CharField (max_length=100)
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.RefProduit

    

class Vehicule (models.Model):
    Matricule =  models.CharField(max_length=100)
    RefMarque =  models.CharField(max_length=100)
    Type =  models.CharField(max_length=100)

    def __str__(self):
        return self.Matricule

class TypePaiement (models.Model): 
    Type = models.CharField(max_length=100)

    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.Type


class Paiement (models.Model): 
    DescPaiement = models.CharField(max_length=100, default='')
    TypePaiement = models.ForeignKey('TypePaiement',on_delete=models.CASCADE)
    DatePaiement = models.DateField()
    DateOperation= models.DateField()
    MontantPaiement=models.FloatField(default=0)

    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.DescPaiement





class Contrat (models.Model):
    NumeroPolice = models.CharField(max_length=100)
    Client = models.ForeignKey('Client', on_delete=models.CASCADE)
    Produit = models.ForeignKey('Produit', on_delete=models.CASCADE)
    Vehicule = models.ForeignKey('Vehicule', on_delete=models.CASCADE)
    DateDebutEffet = models.DateField()
    DateFineffet = models.DateField()
    DateAnnulation = models.DateField()
    MontantPrime = models.FloatField(default=0)
    MontantPAYE = models.FloatField(default=0)
    RESTE = models.FloatField(default=0)
    NumeroAttestation = models.IntegerField(default=0)
    StatutPaiement = models.BinaryField (default=0)
    Paiement =models.ManyToManyField ('Paiement')

    class Meta:
        verbose_name = "Contrat"
        ordering = ['NumeroPolice']
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.NumeroPolice

