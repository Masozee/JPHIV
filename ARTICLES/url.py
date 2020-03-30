
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

    path('annotated-bibliography/', artviews.annotated, name='anotated'),
    path('annotated-bibliography/epidemology/', artviews.annotatedepidem, name='anot-epidemology'),
    path('annotated-bibliography/biomedicine/', artviews.annotatedbiomedicine, name='anot-biomedicine'),
    path('annotated-bibliography/health-economic/', artviews.annotatedhealtheconomic, name='anot-health'),
    path('annotated-bibliography/policy-study/', artviews.annotatedpolicystudy, name='anot-policy'),
    path('annotated-bibliography/social-behavioral/', artviews.annotatedsocialbehavioral, name='anot-social'),
    re_path('annotated-bibliography/(?P<AnotatedJPHIV_slug>[\w-]+)/$', artviews.anotateDetail, name='anotate-detail'),
    path('add/annotated-bibliography/', artviews.BookCreateView.as_view(), name='add-anotated'),
    re_path('author/(?P<tag>[\w-]+)/$', artviews.authorlist.as_view(), name='author-tag'),


    path('hasil/', artviews.hasil, name='hasil-detail'),

]

