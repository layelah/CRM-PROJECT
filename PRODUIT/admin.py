from django.contrib import admin
from .models import Produit,AP,Tags, Unite


admin.site.register(Produit,AP)
admin.site.register(Tags)
admin.site.register(Unite)