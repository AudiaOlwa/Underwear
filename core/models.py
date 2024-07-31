from django.db import models
from django.contrib.auth.models import User
from django.db import models


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
    