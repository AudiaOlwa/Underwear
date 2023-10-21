from django.contrib import admin
#from core.models import Homme,Femme, HommePhoto, FemmePhoto, Cart
from core.models import Product, ProductPhoto, Cart

admin.site.register(Cart)


#class CategoryAdmin(admin.ModelAdmin):
#    list_display = ['nom']

#admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nom', 'category', 'description', 'image', 'prix', 'product_type')

admin.site.register(Product, ProductAdmin)

class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ('product','images')

admin.site.register(ProductPhoto, ProductPhotoAdmin)





#class HommeAdmin(admin.ModelAdmin):
#    list_display = ('nom', 'description', 'image', 'prix')
#
#admin.site.register(Homme, HommeAdmin)
#
#
#class FemmeAdmin(admin.ModelAdmin):
#    list_display = ('nom', 'description', 'image', 'prix')
#
#admin.site.register(Femme, FemmeAdmin)
#
#class HommePhotoAdmin(admin.ModelAdmin):
#    list_display = ('homme', 'image')
#
#admin.site.register(HommePhoto, HommePhotoAdmin)
#
#class FemmePhotoAdmin(admin.ModelAdmin):
#    list_display = ('femme', 'image')
#
#admin.site.register(FemmePhoto, FemmePhotoAdmin)





