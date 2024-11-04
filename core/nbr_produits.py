from django.shortcuts import get_object_or_404
from .models import Cart
#CE FICHIER SERT A AFFICHER LE NOMBRE DE PRODUIT SE TROUVANT DANS LE PANIER (sur toutes les pages du site)
class CartItems:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            cart_items_count = Cart.objects.filter(user=user).count()
            request.cart_items_count = cart_items_count
        else:
            request.cart_items_count = 0
        response = self.get_response(request)
        return response
