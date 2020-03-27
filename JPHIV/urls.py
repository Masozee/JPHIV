from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from SEARCH import views as searchviews
from  USER.views import StaffSignUpView, VisitorSignUpView
from ARTICLES import views as artviews
from  USER import views as userviews

admin.sites.AdminSite.site_header = 'Jaringan Penelitian HIV Indonesia'
admin.sites.AdminSite.site_title = 'Jaringan Penelitian HIV Indonesia'
admin.sites.AdminSite.index_title = 'Jaringan Penelitian HIV Indonesia'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('privacy-policy/', artviews.Privacy, name='privacy'),
    path('terms-of-service/', artviews.TOS, name='TOS'),
    path('overview/', artviews.Overview, name='overview'),
    path('', include('ARTICLES.url')),
    path('cari/', searchviews.SearchView.as_view(), name='cari' ),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/signup/', VisitorSignUpView.as_view(), name='visitor-signup'),
    path('accounts/signup/', userviews.signup, name='signup'),
    re_path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        userviews.activate, name='activate'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)