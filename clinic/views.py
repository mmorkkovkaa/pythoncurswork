from django.shortcuts import render
from django.views.generic.edit import CreateView
from . forms import AddForm
import clinic
from clinic import models
from django.http import HttpResponseRedirect
from .models import Help

# Create your views here.

def Index(request):
    index = models.Index.objects.all() #заднийфон на главной странице
    backtext = models.Backtext.objects.all()  #текст в начале страницы
    backtext2 = models.Backtext2.objects.all() #наши услуги
    posts = models.Posts.objects.all() #наши услуги картинки
    posts2 = models.Posts2.objects.all() #наши лучшие врачи
    doctor1 = models.Doctor1.objects.all() #первый доктор
    news1 = models.News1.objects.all()
    news2 = models.News2.objects.all()     #наши новости
    news3 = models.News3.objects.all()
    back2 = models.Back2.objects.all()
    kontact = models.Kontact.objects.all() #наши контакты
    bodrost = models.Bodrost.objects.all()
    return render(request, 'index.html', {'index': index ,'backtext': backtext ,
                                          'backtext2': backtext2 , 'posts': posts, 'posts2': posts2,
                                          'doctor1': doctor1,  'news1': news1 ,
                                          'news2': news2 , 'news3': news3 ,'back2': back2,  'kontact':kontact, 'bodrost': bodrost})

def create(request):
    if request.method == "POST":
        help = Help()
        help.name = request.POST.get("name")
        help.email = request.POST.get("email")
        help.save()
    return HttpResponseRedirect("/")


def Dentist(request):
    dentist = models.Dentist.objects.all()
    state = models.State.objects.all()  #текст в начале страницы
    postsstl = models.PostsSTL.objects.all() #наши услуги картинки
    posts2stl = models.Posts2STL.objects.all() #наши лучшие врачи
    doctor1stl = models.Doctor1STL.objects.all() #стоматолог1
    news1 = models.News1.objects.all()
    news2 = models.News2.objects.all()
    news3 = models.News3.objects.all()
    kontact = models.Kontact.objects.all()
    return render(request, 'Dentist.html', {'dentist': dentist ,'state': state,
                                          'postsstl': postsstl, 'posts2stl': posts2stl,
                                          'doctor1stl': doctor1stl, 'news1': news1 ,
                                          'news2': news2 , 'news3': news3 , 'kontact':kontact })

def Surgeon(request):
    surgeon = models.Surgeon.objects.all()
    return render(request, 'Surgeon.html', {'surgeon': surgeon})

def Pediatrician(request):
    pediatrician = models.Pediatrician.objects.all()
    return render(request, 'Pediatrician.html', {'pediatrisian': pediatrician})

def Ginekologist(request):
    ginekologist = models.Gynecologist.objects.all()
    return render(request, 'Gynecologist.html', {'ginekologist': ginekologist})