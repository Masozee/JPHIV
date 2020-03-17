
from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.db import transaction
from taggit.models import Tag, TaggedItem
from django.views.generic import DetailView, ListView, TemplateView
from ARTICLES.models import *
from .forms import *

# Create your views here.

def home(request):
    Biomed = AbstractJPHIV.objects.filter(kategori__Kategori="biomedicine")
    biomedC = Biomed.count()
    healeco = AbstractJPHIV.objects.filter(kategori__Kategori="health-economic")
    healecoC = healeco.count()
    polstud = AbstractJPHIV.objects.filter(kategori__Kategori="policy-study")
    polstudC = polstud.count()
    socbeh = AbstractJPHIV.objects.filter(kategori__Kategori="social-behavioral")
    socbehC = socbeh.count()
    epidemo = AbstractJPHIV.objects.filter(kategori__Kategori="epidemology")
    epidemoC = epidemo.count()
    abstracts = AbstractJPHIV.objects.all().order_by('-tanggal')[:3]
    abstractC = AbstractJPHIV.objects.all()
    countabs = abstractC.count()
    anotates = AnotatedJPHIV.objects.all().order_by('-tanggal')[:3]
    anotateC = AnotatedJPHIV.objects.all()
    countanotate = anotateC.count()


    context = {
        'epidem' : epidemo,
        'epidemoc' :epidemoC,
        'helaeco' : healeco,
        'healecoc' : healecoC,
        'biomed' : Biomed,
        'biomedc' : biomedC,
        'polstud' : polstud,
        'polstudc' : polstudC,
        'socbeh' : socbeh,
        'socbehc' : socbehC,
        'abstracts' : abstracts,
        'abstractC': countabs,
        'anotates' : anotates,
        'countanotate' : countanotate
    }
    return render(request, "articles/index.html", context)

def abstract(request):
    epidemo = AbstractJPHIV.objects.all().order_by('-tanggal').distinct()

    context = {
        'abstracts': epidemo
    }
    return render(request, "articles/abstract.html", context )

def epidem(request):
    epidemo = AbstractJPHIV.objects.filter(kategori__Kategori="epidemology").order_by('-tanggal').distinct()

    context = {
        'abstracts':epidemo
    }
    return render(request, 'articles/Epidemology.html', context)


def abstractartikel(request):

    Epidem = AbstractJPHIV.objects.all()

    context = {
        'abstracts': Epidem
    }
    return render(request, 'articles/artikel.html', context)

def abstractbiomedicine(request):
    Biomed = AbstractJPHIV.objects.filter(kategori__Kategori="biomedicine").order_by('-tanggal').distinct()
    return render(request, "articles/biomedic.html", {"abstracts":Biomed})

def abstracthealtheconomic(request):
    healeco = AbstractJPHIV.objects.filter(kategori__Kategori="health-economic").order_by('-tanggal').distinct()
    return render(request, "articles/healthecon.html", {"abstracts":healeco})

def abstractpolicystudy(request):
    polstud = AbstractJPHIV.objects.filter(kategori__Kategori="policy-study").order_by('-tanggal').distinct()
    return render(request, "articles/polstud.html", {"abstracts":polstud})

def abstractsocialbehavioral(request):
    socbeh = AbstractJPHIV.objects.filter(kategori__Kategori="social-behavioral").order_by('-tanggal').distinct()
    return render(request, "articles/socbeh.html", {"abstracts":socbeh})

def anotated(request):
    anot = AnotatedJPHIV.objects.all()
    context = {
        'abstracts': anot
    }
    return render(request, 'articles/anotated.html', context )

def anotatedartikel(request):
    Epidem = AnotatedJPHIV.objects.filter(kategori__Kategori="artikel").order_by('-tanggal').distinct()
    return render(request, "articles/anotated.html", {"abstracts":Epidem})

def anotatedbiomedicine(request):
    Biomed = AnotatedJPHIV.objects.filter(kategori__Kategori="biomedicine").order_by('-tanggal').distinct()
    return render(request, "articles/anotated.html", {"abstracts":Biomed})

def anotatedhealtheconomic(request):
    healeco = AnotatedJPHIV.objects.filter(kategori__Kategori="health-economic").order_by('-tanggal').distinct()
    return render(request, "articles/anotated.html", {"abstracts":healeco})

def anotatedpolicystudy(request):
    polstud = AnotatedJPHIV.objects.filter(kategori__Kategori="policy-study").order_by('-tanggal').distinct()
    return render(request, "articles/anotated.html", {"abstracts":polstud})

def anotatedsocialbehavioral(request):
    socbeh = AnotatedJPHIV.objects.filter(kategori__Kategori="social-behavioral").order_by('-tanggal').distinct()
    return render(request, "articles/anotated.html", {"abstracts":socbeh})

def anotateDetail(request, AnotatedJPHIV_slug):
    anotate = AnotatedJPHIV.objects.get(slug=AnotatedJPHIV_slug)

    context = {
        "abstracts": anotate,
    }
    return render(request, 'articles/detail.html', context)

def abstractDetail(request, AbstractJPHIV_slug):
    abstracts = AbstractJPHIV.objects.get(slug=AbstractJPHIV_slug)
    context = {
        "abstracts": abstracts,
    }
    return render(request, 'articles/detail.html', context)


def hasil(request):
    return render(request, "articles/search-result.html")

@transaction.atomic
def AnotatedAdd(request):

    if request.method == 'POST':
        form = AnotatedForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.added_by = request.user.username
            instance.save()
            users = AnotatedJPHIV.objects.all()

            return render(request, "articles/addanotated.html", {'users': users})
    else:
        form = AnotatedForm

    return render(request, "articles/addanotated.html", {'form': form})

class authorlist(ListView):
    queryset = AbstractJPHIV.objects.all()
    template_name = "articles/tag.html"
    paginate_by = 9
    context = "authorlist"

    def get_queryset(self):
        return AbstractJPHIV.objects.filter(authors__slug__in=[self.kwargs['authors']])
