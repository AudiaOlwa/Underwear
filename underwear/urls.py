from django.conf import settings
from django.conf.urls.static import static
from core import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
#    path("harticle", views.harticle, name="harticle"),
#    path("farticle", views.farticle, name="farticle"),
    path("details/<pk>/", views.product_detail, name="details"),
    path('products/<str:category>/', views.product_category, name='product'),
#    path("fdetails/<pk>/", views.fdetails, name="fdetails"),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart', views.cart, name='cart'),
    path('increase-quantity/<int:pk>/', views.increase_quantity, name='increase_quantity'),
    path('decrease-quantity/<int:pk>/', views.decrease_quantity, name='decrease_quantity'),
    path('remove_from_cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path("essaie", views.essaie, name="essaie"),
    path('login', views.custom_login, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

