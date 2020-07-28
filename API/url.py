from django.urls import path, re_path, include
from .views import AbstractAPIview, AnnotatedAPIview, AbstractAPIDetail, AnnotatedAPIDetail
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [ 
    path('abstracts/', AbstractAPIview.as_view(), name='abstract-api'),
    path('abstracts/<int:pk>/', AbstractAPIDetail.as_view(), name='abstract-api-detail'),
    path('annotateds/', AnnotatedAPIview.as_view(), name='anotated-api'),
    path('annotateds/<int:pk>/', AnnotatedAPIDetail.as_view(), name='annotated-api-detail'),
]