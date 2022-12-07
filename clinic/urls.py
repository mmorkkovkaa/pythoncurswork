from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'clinic'
urlpatterns = [
    path('', views.Index, name='index'),
    path("create/", views.create),
    path('Dentist/', views.Dentist, name='dentist'),
    path('Surgeon/', views.Surgeon, name='surgion'),
    path('Pediatrician/', views.Pediatrician, name='pediatrician'),
    path('Gynecilogist/', views.Ginekologist, name='ginekologist'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)