from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
#from .models import Homme, Femme,HommePhoto,FemmePhoto
from .models import Product, ProductPhoto
from django.shortcuts import redirect, reverse
from .models import Cart
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import CustomLoginForm
from django.db.models import Count
import random
# Create your views here.

def logout_user(request):
    logout(request)
    return redirect('index')
def custom_login(request):
    form = CustomLoginForm()
    message = ''
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                message = 'Identifiants invalides.'
    return render(request, 'login.html', {'form': form, 'message': message})



@login_required
def index(request):
    homme_products_all = list(Product.objects.filter(category='homme'))
# Récupérez tous les produits de la catégorie "femme"
    femme_products_all = list(Product.objects.filter(category='femme'))
# Sélectionnez au hasard 4 produits dans chaque catégorie
    homme_products = random.sample(homme_products_all, min(4, len(homme_products_all)))
    femme_products = random.sample(femme_products_all, min(4, len(femme_products_all)))
    return render(request, 'index.html', {'homme_products':homme_products, 'femme_products':femme_products})
	
	


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
# Récupère les photos supplémentaires du produit
    productphotos = ProductPhoto.objects.filter(product=product)
# Récupère tous les produits de la même catégorie que le produit actuel
    related_products_all = list(Product.objects.filter(category=product.category).exclude(pk=pk))
# Sélectionne au hasard 4 produits parmi ceux de la même catégorie
    related_products = random.sample(related_products_all, min(4, len(related_products_all)))

    return render(request, 'details.html', {
        'product': product,
        'productphotos': productphotos,
        'related_products': related_products,
        'category': product.category 
    })


def product_category(request, category):
    if request.method == "GET":
        product_type = request.GET.get('product_type')
        if product_type == "":
            products = reversed(Product.objects.filter(category=category))
        elif product_type is not None:
            products = reversed(Product.objects.filter(category=category, product_type=product_type))
        else:
            products = reversed(Product.objects.filter(category=category))
        product_types = Product.objects.filter(category=category).values('product_type').annotate(count=Count('product_type'))
        return render(request, 'product.html', {'products': products, 'product_types': product_types, 'selected_product_type': product_type, 'category': category})




def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart.quantity += 1
        cart.save()
        # Récupérer l'URL de la page actuelle à partir des méta-données de la requête
    referer = request.META.get('HTTP_REFERER', '/')
    # Rediriger vers l'URL de la page actuelle
    return redirect(referer)

    #return redirect('details', pk=pk)

def cart(request):
    user = request.user
    cart = reversed(Cart.objects.filter(user=user))
    total_price = Cart.total_cart_price(user)
    return render(request, 'cart.html', {'cart': cart, 'total_price': total_price })


def increase_quantity(request, pk):
    cart_item = get_object_or_404(Cart, pk=pk)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

def decrease_quantity(request, pk):
    cart_item = get_object_or_404(Cart, pk=pk)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('cart')

def remove_from_cart(request, pk):
    cart_item = get_object_or_404(Cart, pk=pk)
    cart_item.delete()
    return redirect('cart')


def essaie(request):
	return render(request, 'essaie.html')



