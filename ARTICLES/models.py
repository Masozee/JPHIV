from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _
#from users.models import CustomUser
from django.utils.text import slugify
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from taggit.models import TagBase, GenericTaggedItemBase
from datetime import date
from django.db.models import Q
from USER.models import CustomUser
from django.conf import settings



class Author(TagBase):
    ket = models.TextField(blank=True)

    class Meta:
        verbose_name = _("Peneliti")
        verbose_name_plural = _("Peneliti")

    def __str__(self):
        return self.Name

class TaggedAuthor(GenericTaggedItemBase):
    tag = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_items",
    )
    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Author")

class TagAnotated(TagBase):
    class Meta:
        verbose_name = _("Annotated Tags")
        verbose_name_plural = _("Annotated Tags")

class TaggedAnnotated(GenericTaggedItemBase):
    tag = models.ForeignKey(
        TagAnotated,
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_items",
    )
    class Meta:
        verbose_name = _("Annotate Tags")
        verbose_name_plural = _("Annotate Tags")

class kategori(models.Model):
    KATEGORI_CHOICES = (
        ('epidemiologi', 'epidemiologi'),
        ('biomedis', 'biomedis'),
        ('ekonomi-kesehatan', 'ekonomi-kesehatan'),
        ('studi-kebijakan', 'studi-kebijakan'),
        ('sosial-perilaku', 'sosial-perilaku')
    )
    Kategori = models.CharField(max_length=20, choices=KATEGORI_CHOICES)
    Subkategori = models.CharField(max_length=150, blank=True)
    Keterangan = models.TextField(blank=True)

    def __str__(self):
        return str(self.Kategori)+"-"+self.Subkategori

    class Meta:
        verbose_name = ("Kategori")
        verbose_name_plural = ("Kategori")

class abstractQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(judul__icontains=query)
                         )
            qs = qs.filter(or_lookup)# distinct() is often necessary with Q lookups
        return qs

class abstractManager(models.Manager):
    def get_queryset(self):
        return abstractQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

# Create your models here.
class AbstractJPHIV(models.Model):
    judul = models.CharField(max_length=300)
    slug = models.SlugField(default='', editable=False, max_length=140)
    tanggal = models.DateField()
    kategori = models.ForeignKey(kategori, on_delete=models.PROTECT)
    authors = TaggableManager(through=TaggedAuthor, related_name='abstracts', verbose_name='Author')
    sumber = models.CharField(max_length=120, blank=True)
    volume = models.CharField(max_length=10, blank=True)
    DOI_number = models.CharField(max_length=20, blank=True)
    DOI_URL = models.URLField(blank=True)
    doctype = models.CharField(max_length=4, blank=True)
    url = models.URLField(blank=True)
    download = models.FileField(upload_to='abstract/', blank=True)
    bibliografi = RichTextField(blank=True)
    abstrak = RichTextField(blank=True)
    visit_num = models.PositiveIntegerField(default=0)
    tags = TaggableManager()


    objects = abstractManager()

    class Meta:
        verbose_name = ("Abstract")
        verbose_name_plural = ("Abstract")

    def __str__(self):
        return self.judul

    def save(self, *args, **kwargs):
        value = self.judul
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    @property
    def tgl(self):
        return self.tanggal.strftime('%d %B %Y')

class anotatedQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(judul__icontains=query)
                        )
            qs = qs.filter(or_lookup)# distinct() is often necessary with Q lookups
        return qs

class anotatedManager(models.Manager):
    def get_queryset(self):
        return anotatedQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

# Create your models here.
class AnotatedJPHIV(models.Model):
    KATEGORI_CHOICES = (
        ('epidemology', 'epidemology'),
        ('biomedicine', 'biomedicine'),
        ('health-economic', 'health-economic'),
        ('policy-study','policy-study'),
        ('social-behavioral', 'social-behavioral')
    )

    judul = models.CharField(max_length=300)
    slug = models.SlugField(default='', editable=False, max_length=140)
    tanggal = models.DateField()
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        null=True, blank=True, on_delete=models.SET_NULL)
    kategori = models.ForeignKey(kategori, on_delete=models.PROTECT)
    Author = TaggableManager(through=TaggedAuthor, related_name='+', verbose_name='Author')
    sumber = models.CharField(max_length=120, blank=True)
    volume = models.CharField(max_length=10, blank=True)
    DOI_number = models.CharField(max_length=120, blank=True)
    DOI_URL = models.URLField(blank=True)
    doctype = models.CharField(max_length=4, blank=True)
    url = models.URLField(blank=True)
    download = models.FileField(upload_to='anotated/', blank=True)
    bibliografi = RichTextField(blank=True)
    anotated = RichTextField(blank=True)
    visit_num = models.PositiveIntegerField(default=0)

    tags = TaggableManager(through=TaggedAnnotated, related_name='tagannotated', verbose_name='Annotated Tags')

    objects = anotatedManager()

    class Meta:
        verbose_name = ("Anotated")
        verbose_name_plural = ("Anotated")

    def __str__(self):
        return self.judul

    def get_absolute_url(self):
        return reverse('books:detail', args=[self.id])

 #  def save_model(self, request, obj, form, change):
  #      obj.added_by = request.user
   #     super().save_model(request, obj, form, change)

    def save(self, *args, **kwargs):
        value = self.judul
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.added_by = request.user
        super().save_model(request, obj, form, change)

    @property
    def tgl(self):
        return self.tanggal.strftime('%d %B %Y')

class Comment(models.Model):
    post = models.ForeignKey(AnotatedJPHIV, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return str(self.post)