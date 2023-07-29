from django.db import models



class Homme(models.Model):
    image = models.ImageField(upload_to='images/')
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return f'{self.nom}({self.description}) '

 
class HommePhoto(models.Model):
    homme = models.ForeignKey(Homme, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='images/')


class Femme(models.Model):
    image = models.ImageField(upload_to='images/')
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)
   

    def __str__(self):
        return f'{self.nom}({self.description})'

class FemmePhoto(models.Model):
    femme = models.ForeignKey(Femme, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='images/')