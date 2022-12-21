from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib import admin
from . import models
#главная страница
admin.site.register(models.Index)
admin.site.register(models.Backtext)
admin.site.register(models.Backtext2)
admin.site.register(models.Posts)
admin.site.register(models.Posts2)
admin.site.register(models.Doctor1)
admin.site.register(models.News1)
admin.site.register(models.News2)
admin.site.register(models.News3)
admin.site.register(models.Kontact)
admin.site.register(models.Back2)
admin.site.register(models.HelpU)


#стоматология
admin.site.register(models.Dentist)
admin.site.register(models.State)
admin.site.register(models.Backtext2stl)
admin.site.register(models.Postsstl)
admin.site.register(models.Posts2STL)
admin.site.register(models.Doctor1STL)
admin.site.register(models.Newsstl)


#хирургия
admin.site.register(models.Surgeon)
admin.site.register(models.StateH)
admin.site.register(models.Backtext2H)
admin.site.register(models.PostsH)
admin.site.register(models.Posts2H)
admin.site.register(models.Doctor1H)
admin.site.register(models.NewsH)

#педиатрия
admin.site.register(models.Pediatrician)
admin.site.register(models.StateP)
admin.site.register(models.Backtext2P)
admin.site.register(models.PostsP)
admin.site.register(models.Posts2P)
admin.site.register(models.Doctor1P)
admin.site.register(models.NewsP)

#ГИНЕКOЛОГИЯ
admin.site.register(models.Gynecologist)
admin.site.register(models.StateG)
admin.site.register(models.Backtext2G)
admin.site.register(models.PostsG)
admin.site.register(models.Posts2G)
admin.site.register(models.Doctor1G)
admin.site.register(models.NewsG)

#О нас
admin.site.register(models.AboutAs)
admin.site.register(models.AboutAsState)
admin.site.register(models.Service)