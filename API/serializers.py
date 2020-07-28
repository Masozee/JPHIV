from rest_framework import serializers
from ARTICLES.models import AbstractJPHIV, AnotatedJPHIV

class AbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstractJPHIV
        fields = ('judul', 'tanggal','kategori', 'sumber', 'volume', 'DOI_number', 'DOI_URL', 'doctype', 'url', 'download', 'bibliografi', 'abstrak')

class AnotatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnotatedJPHIV
        fields = ('judul', 'tanggal','added_by','kategori', 'sumber', 'volume', 'DOI_number', 'DOI_URL', 'doctype', 'url', 'download', 'bibliografi')