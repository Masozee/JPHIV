
from django.urls import path, re_path, include
from ARTICLES import views as artviews

urlpatterns = [
    path('', artviews.home, name='homepage'),

    path('abstract/', artviews.abstract, name='abstract'),
    path('abstract/epidemology/', artviews.epidem, name='abstract-epidemology'),
    path('abstract/biomedicine/', artviews.abstractbiomedicine, name='abstract-biomedicine'),
    path('abstract/health-economic/', artviews.abstracthealtheconomic, name='abstract-health'),
    path('abstract/policy-study/', artviews.abstractpolicystudy, name='abstract-policy'),
    path('abstract/social-behavioral/', artviews.abstractsocialbehavioral, name='abstract-social'),
    re_path('abstract/(?P<AbstractJPHIV_slug>[\w-]+)/$', artviews.abstractDetail, name='abstract-detail'),

    path('anotated-bibliography/', artviews.anotated, name='anotated'),
    path('anotated-bibliography/epidemology/', artviews.anotatedepidem, name='anot-epidemology'),
    path('anotated-bibliography/biomedicine/', artviews.anotatedbiomedicine, name='anot-biomedicine'),
    path('anotated-bibliography/health-economic/', artviews.anotatedhealtheconomic, name='anot-health'),
    path('anotated-bibliography/policy-study/', artviews.anotatedpolicystudy, name='anot-policy'),
    path('anotated-bibliography/social-behavioral/', artviews.anotatedsocialbehavioral, name='anot-social'),
    re_path('anotated-bibliography/(?P<AnotatedJPHIV_slug>[\w-]+)/$', artviews.anotateDetail, name='anotate-detail'),
    path('add/anotated-bibliography/', artviews.BookCreateView.as_view(), name='add-anotated'),
    re_path('author/(?P<tag>[\w-]+)/$', artviews.authorlist.as_view(), name='author-tag'),


    path('hasil/', artviews.hasil, name='hasil-detail'),

]

