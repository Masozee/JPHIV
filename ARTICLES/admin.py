from django.contrib import admin
from ARTICLES.models import *
# Register your models here.

admin.site.register(AnotatedJPHIV)
admin.site.register(AbstractJPHIV)
admin.site.register(kategori)
admin.site.register(Author)
admin.site.register(TagAnotated)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'text', 'created_date', 'active')
    list_filter = ('active', 'created_date')
    search_fields = ('post', 'text')
    actions = ['approved_comment']

    def approved_comment(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Comment, CommentAdmin)