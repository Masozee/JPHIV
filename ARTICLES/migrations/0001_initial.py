# Generated by Django 2.2 on 2020-03-12 12:19

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='kategori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Kategori', models.CharField(choices=[('epidemology', 'epidemology'), ('biomedicine', 'biomedicine'), ('health-economic', 'health-economic'), ('policy-study', 'policy-study'), ('social-behavioral', 'social-behavioral')], max_length=20)),
                ('Subkategori', models.CharField(blank=True, max_length=150)),
                ('Keterangan', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Kategori',
                'verbose_name_plural': 'Kategori',
            },
        ),
        migrations.CreateModel(
            name='AnotatedJPHIV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=300)),
                ('slug', models.SlugField(default='', editable=False, max_length=140)),
                ('tanggal', models.DateField()),
                ('url', models.URLField(blank=True)),
                ('download', models.FileField(blank=True, upload_to='MEDIA/anotated/')),
                ('bibliografi', ckeditor.fields.RichTextField(blank=True)),
                ('anotated', ckeditor.fields.RichTextField(blank=True)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ARTICLES.kategori')),
                ('tag', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Anotated',
                'verbose_name_plural': 'Anotated',
            },
        ),
        migrations.CreateModel(
            name='AbstractJPHIV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=300)),
                ('slug', models.SlugField(default='', editable=False, max_length=140)),
                ('tanggal', models.DateField()),
                ('url', models.URLField(blank=True)),
                ('download', models.FileField(blank=True, upload_to='MEDIA/abstract/')),
                ('bibliografi', ckeditor.fields.RichTextField(blank=True)),
                ('abstrak', ckeditor.fields.RichTextField(blank=True)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ARTICLES.kategori')),
                ('tag', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Abstract',
                'verbose_name_plural': 'Abstract',
            },
        ),
    ]
