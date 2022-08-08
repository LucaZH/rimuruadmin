from django.contrib import admin
from .models import Utilisateur,CentreMedical,Pharmacie,Conseil


# admin.site.index_template=
class Utilisateuradminview(admin.ModelAdmin):
    list_display = ['fb_id','state','query','role']
    # list_editabe = ['fb_id','state','query','role']
class CentreMedicaladminview(admin.ModelAdmin):
    list_display = ['id','nom','localisation','contact','verifier','publier_par','zone']
    list_editable =['verifier','contact','nom','zone','localisation'] 
class Pharmacieadminview(admin.ModelAdmin):
    list_display = ['id','nom','localisation','contact','verifier','publier_par','zone']
    list_editable =['verifier','contact','nom','zone','localisation']   
class Conseiladminview(admin.ModelAdmin):
    list_display = ['id','text']
    list_editable = ['text']
    
admin.site.register(Utilisateur,Utilisateuradminview)
admin.site.register(CentreMedical,CentreMedicaladminview)
admin.site.register(Pharmacie,Pharmacieadminview)
admin.site.register(Conseil,Conseiladminview)
admin.site.site_title = "Rimuru"
admin.site.site_header = "Rimuru Admin"
