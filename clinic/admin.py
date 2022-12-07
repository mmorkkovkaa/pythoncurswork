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
admin.site.register(models.Help)
admin.site.register(models.Bodrost)


admin.site.register(models.Dentist)
admin.site.register(models.State)
admin.site.register(models.PostsSTL)
admin.site.register(models.Posts2STL)
admin.site.register(models.Doctor1STL)
