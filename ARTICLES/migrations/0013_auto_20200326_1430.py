# Generated by Django 2.2 on 2020-03-26 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ARTICLES', '0012_auto_20200319_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotatedjphiv',
            name='DOI_number',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]