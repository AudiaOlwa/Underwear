from django.contrib import admin
from core.models import Homme,Femme, HommePhoto, FemmePhoto


class HommeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'image', 'prix')

admin.site.register(Homme, HommeAdmin)


class FemmeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'image', 'prix')

admin.site.register(Femme, FemmeAdmin)

class HommePhotoAdmin(admin.ModelAdmin):
    list_display = ('homme', 'image')

admin.site.register(HommePhoto, HommePhotoAdmin)

class FemmePhotoAdmin(admin.ModelAdmin):
    list_display = ('femme', 'image')

admin.site.register(FemmePhoto, FemmePhotoAdmin)





