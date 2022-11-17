from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [

    path('', views.inicio, name="inicio"),
    path('bands/', views.pagina_bandas, name="pagina_bandas"),
    path('discs/', views.discos, name="pagina_disco"),
    path('about/', views.pagina_acerca, name="pagina_acerca"),
    path('discs/crear', views.crear_disco, name="crear_disco"),
    path('editar/<int:id>', views.editar_disco, name="editar_disco"),
    path('eliminar/<int:id>',views.borrar_disco, name="borrar")


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)