# Generated by Django 2.2 on 2020-07-21 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('ARTICLES', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abstractjphiv',
            old_name='tag',
            new_name='tags',
        ),
        migrations.RemoveField(
            model_name='anotatedjphiv',
            name='tag',
        ),
        migrations.AddField(
            model_name='abstractjphiv',
            name='DOI_URL',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='abstractjphiv',
            name='DOI_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='abstractjphiv',
            name='doctype',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AddField(
            model_name='abstractjphiv',
            name='sumber',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='abstractjphiv',
            name='visit_num',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abstractjphiv',
            name='volume',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='anotatedjphiv',
            name='DOI_URL',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='anotatedjphiv',
            name='DOI_number',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='anotatedjphiv',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='anotatedjphiv',
            name='doctype',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AddField(
            model_name='anotatedjphiv',
            name='sumber',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='anotatedjphiv',
            name='visit_num',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='anotatedjphiv',
            name='volume',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='abstractjphiv',
            name='download',
            field=models.FileField(blank=True, upload_to='abstract/'),
        ),
        migrations.AlterField(
            model_name='anotatedjphiv',
            name='download',
            field=models.FileField(blank=True, upload_to='anotated/'),
        ),
        migrations.AlterField(
            model_name='kategori',
            name='Kategori',
            field=models.CharField(choices=[('epidemiologi', 'epidemiologi'), ('biomedis', 'biomedis'), ('ekonomi-kesehatan', 'ekonomi-kesehatan'), ('studi-kebijakan', 'studi-kebijakan'), ('sosial-perilaku', 'sosial-perilaku')], max_length=20),
        ),
        migrations.CreateModel(
            name='TaggedAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles_taggedauthor_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='articles_taggedauthor_items', to='ARTICLES.Author')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Author',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ARTICLES.AnotatedJPHIV')),
            ],
        ),
        migrations.AddField(
            model_name='abstractjphiv',
            name='authors',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', related_name='abstracts', through='ARTICLES.TaggedAuthor', to='ARTICLES.Author', verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='anotatedjphiv',
            name='Author',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', related_name='+', through='ARTICLES.TaggedAuthor', to='ARTICLES.Author', verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='anotatedjphiv',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', related_name='tagannotated', through='ARTICLES.TaggedAnnotated', to='ARTICLES.TagAnotated', verbose_name='Annotated Tags'),
        ),
    ]
