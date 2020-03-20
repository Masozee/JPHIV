from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from django.views.generic import ListView
from USER.decorators import staff_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from ARTICLES.models import *



class SearchView(ListView):
    template_name = 'articles/search-result.html'
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            anotate_results = AnotatedJPHIV.objects.search(query)
            abstract_results = AbstractJPHIV.objects.search(query)


            # combine querysets
            queryset_chain = chain(
                abstract_results,
                anotate_results,
            )

            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return AbstractJPHIV.objects.none()