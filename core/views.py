from django.shortcuts import render, get_object_or_404
from .models import Homme, Femme,HommePhoto,FemmePhoto
from django.urls import reverse

# Create your views here.

def index(request):
	#hommes = reversed(Homme.objects.all())
	hommes = list(reversed(Homme.objects.all()))[0:4]
	femmes = list(reversed(Femme.objects.all()))[0:4]
	return render(request, 'index.html', {'femmes': femmes, 'hommes': hommes})


def harticle(request):
	hommes = reversed(Homme.objects.all())
	return render(request, 'harticle.html', {'hommes': hommes})

def farticle(request):
	femmes = reversed(Femme.objects.all())
	return render(request, 'farticle.html', {'femmes': femmes})

#def hdetails(request, pk):
#	homme = Homme.objects.get(pk=pk)
#	hommephoto = get_object_or_404(HommePhoto, pk=pk)
#	photo = reversed(HommePhoto.objects.all()) 
#	hommes = list(reversed(Homme.objects.exclude(pk=pk)))[0:4] 
#	return render(request, 'hdetails.html', {'homme': homme, 'hommes' : hommes, 'photo': photo,'hommephoto':hommephoto}) 

def hdetails(request, pk):
    homme = get_object_or_404(Homme, pk=pk)
    hommephotos = HommePhoto.objects.filter(homme=homme)  # Utilise filter() pour obtenir plusieurs objets
    
    hommes = Homme.objects.exclude(pk=pk).order_by('-pk')[:4]  # Récupère les autres hommes (4 derniers)

    return render(request, 'hdetails.html', {
        'homme': homme,
        'hommephotos': hommephotos,
        'hommes': hommes
    })



#def fdetails(request, pk):
#	femme = Femme.objects.get(pk=pk)
#	femmes = list(reversed(Femme.objects.exclude(pk=pk)))[0:4] 
#	return render(request, 'fdetails.html', {'femme': femme, 'femmes' : femmes} )

def fdetails(request, pk):
    femme = get_object_or_404(Femme, pk=pk)
    femmephotos = FemmePhoto.objects.filter(femme=femme)  # Utilise filter() pour obtenir plusieurs objets
    
    femmes = Femme.objects.exclude(pk=pk).order_by('-pk')[:4]  # Récupère les autres hommes (4 derniers)

    return render(request, 'fdetails.html', {
        'femme': femme,
        'femmephotos': femmephotos,
        'femmes': femmes
    })


def cart(request):
	return render(request, 'cart.html')

def essaie(request):
	return render(request, 'essaie.html')


