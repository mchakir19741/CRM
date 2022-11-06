from django.contrib import admin
from .models import *

#TypePermis, Permis, Nationalite, Client, TypeAvenant, Produit,Vehicule, TypePaiement, Paiement, Contrat


admin.site.register(TypePermis)
admin.site.register(Permis)
admin.site.register(Nationalite)
admin.site.register(Client)
admin.site.register(TypeAvenant)
admin.site.register(Produit)
admin.site.register(Vehicule)
admin.site.register(TypePaiement)
admin.site.register(Paiement)
admin.site.register(Contrat)
