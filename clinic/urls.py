from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'clinic'
urlpatterns = [
    path('', views.index, name='index'),
    path("create/", views.create),
    path('Dentist/', views.dentist, name='dentist'),
    path('Surgeon/', views.surgeon, name='surgeon'),
    path('Pediatrician/', views.pediatrician, name='pediatrician'),
    path('Gynecologist/', views.ginekologist, name='gynecologist'),
    path('AboutAs/', views.aboutas, name='aboutas')
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)