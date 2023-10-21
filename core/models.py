from django.db import models
from django.contrib.auth.models import User
from django.db import models

#class Category(models.Model):
#    nom = models.CharField(max_length=10)
#
#    def __str__(self):
##        return self.nom
#
#class Product(models.Model):
#    category = models.ForeignKey(Category, on_delete=models.CASCADE)
#    nom = models.CharField(max_length=100)
#    image = models.ImageField(upload_to='products/')
#    description = models.TextField()
#    prix = models.DecimalField(max_digits=5, decimal_places=0)
#
#    def get_product_type_choices(self):
#        if self.category.nom == 'homme':
#            return [
#                ('boxers', 'boxers'),
#                ('shorts', 'shorts'),
#                ('extras', 'extras'),
#            ]
#        elif self.category.nom == 'femme':
#            return [
#                ('strings', 'strings'),
#                ('ensembles', 'ensembles'),
#                ('cullotes', 'cullotes'),
#            ]
#        else:
#            return []
#---------------------------------------------
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('homme', 'Homme'),
        ('femme', 'Femme'),
    ]

    PRODUCT_TYPE_CHOICES = [
        ('Boxers', 'Boxers'),
        ('Shorts', 'Shorts'),
        ('Extras', 'Extras'),
        ('Strings', 'Strings'),
        ('Ensembles', 'Ensembles'),
        ('Cullotes', 'Cullotes'),
    ]


    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    product_type = models.CharField(max_length=20, null=True, choices=PRODUCT_TYPE_CHOICES)
    nom = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    prix = models.DecimalField(max_digits=5, decimal_places=0)
    def __str__(self):
            return f'{self.nom}'


    

class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos')
    images = models.ImageField(upload_to='images/')
    def __str__(self):
            return f'{self.images}'
    




    
#class Homme(models.Model):
#    image = models.ImageField(upload_to='images/')
#    nom = models.CharField(max_length=100)
#    product_type = models.CharField(max_length=50, choices=[
#        ('Boxers', 'Boxers'),
#        ('Shorts', 'Shorts'),
#        ('Extras', 'Extras'),
#        ], default='Boxers')
#    description = models.TextField()
#    prix = models.DecimalField(max_digits=8)
#    def __str__(self):
#        return f'{self.nom}({self.description}) '
#
# 
#class HommePhoto(models.Model):
#    homme = models.ForeignKey(Homme, on_delete=models.CASCADE, related_name='photos')
#    image = models.ImageField(upload_to='images/')
#
#
#class Femme(models.Model):
#    image = models.ImageField(upload_to='images/')
#    nom = models.CharField(max_length=100)
#    product_type = models.CharField(max_length=50, choices=[
#        ('Strings', 'Strings'),
#        ('Ensembles', 'Ensembles'),
#        ('Cullotes', 'Cullotes'),
#    ], default='Strings')
#    description = models.TextField()
#    prix = models.DecimalField(max_digits=8, decimal_places=2)
#   
#
#    def __str__(self):
#        return f'{self.nom}({self.description})'
#
#class FemmePhoto(models.Model):
#    femme = models.ForeignKey(Femme, on_delete=models.CASCADE, related_name='photos')
#    image = models.ImageField(upload_to='images/')
#
#
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def increase_quantity_url(self):
        return reverse('increase_quantity', args=[str(self.id)])

    def decrease_quantity_url(self):
        return reverse('decrease_quantity', args=[str(self.id)])

    def total_price(self):
        return self.product.prix * self.quantity

    @staticmethod
    def total_cart_price(user):
        cart_items = Cart.objects.filter(user=user)
        total_price = sum(item.total_price() for item in cart_items)
        return total_price

    def __str__(self):
        return f'{self.user}({self.product.nom})({self.quantity}) '
    