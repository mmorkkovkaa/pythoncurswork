from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import AddForm
import clinic
from clinic import models
from django.http import HttpResponseRedirect
from .models import HelpU


# Create your views here.

def index(request):
    index = models.Index.objects.all()  # заднийфон на главной странице
    backtext = models.Backtext.objects.all()  # текст в начале страницы
    backtext2 = models.Backtext2.objects.all()  # наши услуги
    posts = models.Posts.objects.all()  # наши услуги картинки
    posts2 = models.Posts2.objects.all()  # наши лучшие врачи
    doctor1 = models.Doctor1.objects.all()  # первый доктор
    news1 = models.News1.objects.all()
    news2 = models.News2.objects.all()  # наши новости
    news3 = models.News3.objects.all()
    back2 = models.Back2.objects.all()
    kontact = models.Kontact.objects.all()  # наши контакты


    context = {'index': index, 'backtext': backtext,
               'backtext2': backtext2, 'posts': posts, 'posts2': posts2,
               'doctor1': doctor1, 'news1': news1,
               'news2': news2, 'news3': news3, 'back2': back2,
               'kontact': kontact,
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == "POST":
        helpu = HelpU()
        helpu.name = request.POST.get("name")
        helpu.phone = request.POST.get("phone")
        helpu.description = request.POST.get("description")
        helpu.save()
    return HttpResponseRedirect("/")



def dentist(request):
    dentist = models.Dentist.objects.all()
    state = models.State.objects.all()  # текст в начале страницы
    backtext2stl = models.Backtext2stl.objects.all()  # наши услуги
    postsstl = models.Postsstl.objects.all()  # наши услуги картинки
    posts2stl = models.Posts2STL.objects.all()  # наши лучшие врачи текст
    doctor1stl = models.Doctor1STL.objects.all()  # стоматологи
    newsstl = models.Newsstl.objects.all()
    kontact = models.Kontact.objects.all()

    context = {
        'dentist': dentist, 'state': state,
        'backtext2stl': backtext2stl,
        'postsstl': postsstl, 'posts2stl': posts2stl,
        'doctor1stl': doctor1stl, 'newsstl': newsstl, 'kontact': kontact,
    }
    return render(request, 'Dentist.html', context)


def surgeon(request):
    surgeon = models.Surgeon.objects.all()
    stateh = models.StateH.objects.all()  # статья о хирургии
    backtext2h = models.Backtext2H.objects.all()  # услуги текст
    postsh = models.PostsH.objects.all()  # услуги картинки
    posts2h = models.Posts2H.objects.all()  # наши лучшие хирурги
    doctor1h = models.Doctor1H.objects.all()  # доктора
    newsh = models.NewsH.objects.all()
    kontact = models.Kontact.objects.all()

    context = {
        'surgeon': surgeon,
        'stateh': stateh,
        'backtext2h': backtext2h,
        'postsh': postsh, 'posts2h': posts2h,
        'doctor1h': doctor1h, 'newsh': newsh, 'kontact': kontact
    }
    return render(request, 'Surgeon.html', context)


def pediatrician(request):
    pediatrician = models.Pediatrician.objects.all()
    statep = models.StateP.objects.all()  # статья о хирургии
    backtext2p = models.Backtext2P.objects.all()  # услуги текст
    postsp = models.PostsP.objects.all()  # услуги картинки
    posts2p = models.Posts2P.objects.all()  # наши лучшие хирурги
    doctor1p = models.Doctor1P.objects.all()  # доктора
    newsp = models.NewsP.objects.all()
    kontact = models.Kontact.objects.all()

    context = {
        'pediatriсian': pediatrician,
        'statep': statep,
        'backtext2p': backtext2p,
        'postsp': postsp, 'posts2p': posts2p,
        'doctor1p': doctor1p, 'newsp': newsp, 'kontact': kontact
    }
    return render(request, 'Pediatrician.html', context)


def ginekologist(request):
    ginekologist = models.Gynecologist.objects.all()
    stateg = models.StateG.objects.all()  # статья о хирургии
    backtext2g = models.Backtext2G.objects.all()  # услуги текст
    postsg = models.PostsG.objects.all()  # услуги картинки
    posts2g = models.Posts2G.objects.all()  # наши лучшие хирурги
    doctor1g = models.Doctor1G.objects.all()  # доктора
    newsg = models.NewsG.objects.all()
    kontact = models.Kontact.objects.all()

    context = {
        'ginekologist': ginekologist,
        'stateg': stateg,
        'backtext2g': backtext2g,
        'postsg': postsg, 'posts2g': posts2g,
        'doctor1g': doctor1g, 'newsg': newsg, 'kontact': kontact
    }
    return render(request, 'Gynecologist.html', context)


def aboutas(request):
    aboutas = models.AboutAs.objects.all()
    aboutasstate = models.AboutAsState.objects.all()
    service = models.Service.objects.all()
    kontact = models.Kontact.objects.all()


    context = {'kontact': kontact,'aboutas': aboutas,
               'aboutasstate': aboutasstate ,
               'service':service,
    }
    return render(request, 'AboutUs.html', context)
