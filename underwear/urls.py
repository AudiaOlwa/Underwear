from django.conf import settings
from django.conf.urls.static import static
from core import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("harticle", views.harticle, name="harticle"),
    path("farticle", views.farticle, name="farticle"),
    path("hdetails/<pk>/", views.hdetails, name="hdetails"),
    path("fdetails/<pk>/", views.fdetails, name="fdetails"),
    path("cart", views.cart, name="cart"),
    path("essaie", views.essaie, name="essaie"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

