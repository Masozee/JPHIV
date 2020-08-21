
from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction
from taggit.models import Tag, TaggedItem
from django.views.generic import DetailView, ListView, TemplateView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from ARTICLES.models import *
from django.db.models import F
from .forms import *

# Create your views here.

def home(request):
    Biomed = AbstractJPHIV.objects.filter(kategori__Kategori="biomedicine").distinct()
    biomedC = Biomed.count()
    healeco = AbstractJPHIV.objects.filter(kategori__Kategori="health-economic").distinct()
    healecoC = healeco.count()
    polstud = AbstractJPHIV.objects.filter(kategori__Kategori="policy-study").distinct()
    polstudC = polstud.count()
    socbeh = AbstractJPHIV.objects.filter(kategori__Kategori="social-behavioral").distinct()
    socbehC = socbeh.count()
    epidemo = AbstractJPHIV.objects.filter(kategori__Kategori="epidemology").distinct()
    epidemoC = epidemo.count()
    abstracts = AbstractJPHIV.objects.all().order_by('-tanggal').distinct()[:6]
    abstractC = AbstractJPHIV.objects.all().distinct()
    countabs = abstractC.count()
    anotates = AnotatedJPHIV.objects.all().order_by('-tanggal').distinct()[:3]
    anotateC = AnotatedJPHIV.objects.all().distinct()
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
    paginator = Paginator(epidemo, 9)
    page = request.GET.get('page')
    try:
        epidemo = paginator.page(page)
    except PageNotAnInteger:
        epidemo = paginator.page(1)
    except EmptyPage:
        epidemo = paginator.page(paginator.num_pages)

    context = {
        'abstracts': epidemo
    }
    return render(request, "articles/abstract.html", context )

def epidem(request):
    epidemo = AbstractJPHIV.objects.filter(kategori__Kategori="epidemology").order_by('-tanggal').distinct()
    paginator = Paginator(epidemo, 9)
    page = request.GET.get('page')
    try:
        epidemo = paginator.page(page)
    except PageNotAnInteger:
        epidemo = paginator.page(1)
    except EmptyPage:
        epidemo = paginator.page(paginator.num_pages)

    context = {
        'abstracts':epidemo
    }
    return render(request, 'articles/abstract/Epidemology.html', context)


def abstractartikel(request):

    Epidem = AbstractJPHIV.objects.all()

    context = {
        'abstracts': Epidem
    }
    return render(request, 'articles/abstract/artikel.html', context)

def abstractbiomedicine(request):
    Biomed = AbstractJPHIV.objects.filter(kategori__Kategori="biomedicine").order_by('-tanggal').distinct()
    paginator = Paginator(Biomed, 9)
    page = request.GET.get('page')
    try:
        Biomed = paginator.page(page)
    except PageNotAnInteger:
        Biomed = paginator.page(1)
    except EmptyPage:
        Biomed = paginator.page(paginator.num_pages)

    return render(request, "articles/abstract/biomedic.html", {"abstracts":Biomed})

def abstracthealtheconomic(request):
    healeco = AbstractJPHIV.objects.filter(kategori__Kategori="health-economic").order_by('-tanggal').distinct()
    paginator = Paginator(healeco, 9)
    page = request.GET.get('page')
    try:
        healeco = paginator.page(page)
    except PageNotAnInteger:
        healeco = paginator.page(1)
    except EmptyPage:
        healeco = paginator.page(paginator.num_pages)

    return render(request, "articles/abstract/healthecon.html", {"abstracts":healeco})

def abstractpolicystudy(request):
    polstud = AbstractJPHIV.objects.filter(kategori__Kategori="policy-study").order_by('-tanggal').distinct()
    paginator = Paginator(polstud, 9)
    page = request.GET.get('page')
    try:
        polstud = paginator.page(page)
    except PageNotAnInteger:
        polstud = paginator.page(1)
    except EmptyPage:
        polstud = paginator.page(paginator.num_pages)

    return render(request, "articles/abstract/polstud.html", {"abstracts":polstud})

def abstractsocialbehavioral(request):
    socbeh = AbstractJPHIV.objects.filter(kategori__Kategori="social-behavioral").order_by('-tanggal').distinct()
    paginator = Paginator(socbeh, 9)
    page = request.GET.get('page')
    try:
        socbeh = paginator.page(page)
    except PageNotAnInteger:
        socbeh = paginator.page(1)
    except EmptyPage:
        socbeh = paginator.page(paginator.num_pages)

    return render(request, "articles/abstract/socbeh.html", {"abstracts":socbeh})

def annotated(request):
    anot = AnotatedJPHIV.objects.all()
    paginator = Paginator(anot, 9)
    page = request.GET.get('page')
    try:
        anot = paginator.page(page)
    except PageNotAnInteger:
        anot = paginator.page(1)
    except EmptyPage:
        anot = paginator.page(paginator.num_pages)

    context = {
        'abstracts': anot
    }
    return render(request, 'articles/anotated.html', context )

def annotatedartikel(request):
    Epidem = AnotatedJPHIV.objects.filter(kategori__Kategori="artikel").order_by('-tanggal').distinct()
    paginator = Paginator(Epidem, 9)
    page = request.GET.get('page')
    try:
        Epidem = paginator.page(page)
    except PageNotAnInteger:
        Epidem = paginator.page(1)
    except EmptyPage:
        Epidem = paginator.page(paginator.num_pages)

    return render(request, "articles/anotated.html", {"abstracts":Epidem})

def annotatedepidem(request):
    epidemo = AnotatedJPHIV.objects.filter(kategori__Kategori="epidemology").order_by('-tanggal').distinct()
    paginator = Paginator(epidemo, 9)
    page = request.GET.get('page')
    try:
        epidemo = paginator.page(page)
    except PageNotAnInteger:
        epidemo = paginator.page(1)
    except EmptyPage:
        epidemo = paginator.page(paginator.num_pages)

    context = {
        'abstracts':epidemo
    }
    return render(request, 'articles/anotated/Epidemology.html', context)

def annotatedbiomedicine(request):
    Biomed = AnotatedJPHIV.objects.filter(kategori__Kategori="biomedicine").order_by('-tanggal').distinct()
    paginator = Paginator(Biomed, 9)
    page = request.GET.get('page')
    try:
        Biomed = paginator.page(page)
    except PageNotAnInteger:
        Biomed = paginator.page(1)
    except EmptyPage:
        Biomed = paginator.page(paginator.num_pages)
    return render(request, "articles/anotated/biomedic.html", {"abstracts":Biomed})

def annotatedhealtheconomic(request):
    healeco = AnotatedJPHIV.objects.filter(kategori__Kategori="health-economic").order_by('-tanggal').distinct()
    paginator = Paginator(healeco, 9)
    page = request.GET.get('page')
    try:
        healeco = paginator.page(page)
    except PageNotAnInteger:
        healeco = paginator.page(1)
    except EmptyPage:
        healeco = paginator.page(paginator.num_pages)

    return render(request, "articles/anotated/healthecon.html", {"abstracts":healeco})

def annotatedpolicystudy(request):
    polstud = AnotatedJPHIV.objects.filter(kategori__Kategori="policy-study").order_by('-tanggal').distinct()
    paginator = Paginator(polstud, 9)
    page = request.GET.get('page')
    try:
        polstud = paginator.page(page)
    except PageNotAnInteger:
        polstud = paginator.page(1)
    except EmptyPage:
        polstud = paginator.page(paginator.num_pages)

    return render(request, "articles/anotated/polstud.html", {"abstracts":polstud})

def annotatedsocialbehavioral(request):
    socbeh = AnotatedJPHIV.objects.filter(kategori__Kategori="social-behavioral").order_by('-tanggal').distinct()
    paginator = Paginator(socbeh, 9)
    page = request.GET.get('page')
    try:
        socbeh = paginator.page(page)
    except PageNotAnInteger:
        socbeh = paginator.page(1)
    except EmptyPage:
        socbeh = paginator.page(paginator.num_pages)

    return render(request, "articles/anotated/socbeh.html", {"abstracts":socbeh})

def anotateDetail(request, AnotatedJPHIV_slug):
    anotate = AnotatedJPHIV.objects.get(slug=AnotatedJPHIV_slug)

    anotate.visit_num = F('visit_num') + 1
    counts = anotate.visit_num
    anotate.save()

    anotate_related = anotate.tags.similar_objects()[:5]

    context = {
        "abstracts": anotate,
        "related": anotate_related,
    }
    return render(request, 'articles/detailanotated.html', context)

def abstractDetail(request, AbstractJPHIV_slug):
    abstracts = AbstractJPHIV.objects.get(slug=AbstractJPHIV_slug)

    abstracts.visit_num = F('visit_num') + 1
    counts = abstracts.visit_num
    abstracts.save()

    abstract_related = abstracts.tags.similar_objects()[:5]

    context = {
        "abstracts": abstracts,
        "related": abstract_related,

    }
    return render(request, 'articles/detail.html', context)


def hasil(request):
    return render(request, "articles/search-result.html")

class authorlist(ListView):
    queryset = AbstractJPHIV.objects.all()
    template_name = "articles/authortag.html"
    paginate_by = 9
    context = "authorlist"

    def get_queryset(self):
        return AbstractJPHIV.objects.filter(authors__slug__in=[self.kwargs['tag']])

class annotatedlist(ListView):
    queryset = AnotatedJPHIV.objects.all()
    template_name = "articles/tag-result.html"
    paginate_by = 9
    context = "authorlist"

    def get_queryset(self):
        return AnotatedJPHIV.objects.filter(Author__slug__in=[self.kwargs['tag']])


class BookCreateView(LoginRequiredMixin, CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': AnotForm()}
        return render(request, 'articles/addanotated3.html', context)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = AnotForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.added_by = request.user
            instance.save()
            form.save_m2m()

            return HttpResponseRedirect(reverse_lazy('homepage'))
        return render(request, 'articles/addanotated3.html', {'form': form})

def Overview(request):
    return render(request, 'articles/overview.html')

def Privacy(request):
    return render(request, 'articles/privacy.html')

def TOS(request):
    return render(request, 'articles/TOS.html')


#_________________HANDLER 404___________________

def handler404(request, exception):
    return render(request, '404.html', locals())