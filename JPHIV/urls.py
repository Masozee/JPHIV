from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from SEARCH import views as searchviews
from  USER.views import StaffSignUpView, VisitorSignUpView
from ARTICLES import views as artviews
from  USER.views import *

admin.sites.AdminSite.site_header = 'Jaringan Penelitian HIV Indonesia'
admin.sites.AdminSite.site_title = 'Jaringan Penelitian HIV Indonesia'
admin.sites.AdminSite.index_title = 'Jaringan Penelitian HIV Indonesia'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ARTICLES.url')),
    path('cari/', searchviews.SearchView.as_view(), name='cari' ),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', VisitorSignUpView.as_view(), name='visitor-signup')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)