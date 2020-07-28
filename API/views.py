from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

from ARTICLES.models import AbstractJPHIV, AnotatedJPHIV
from .serializers import AbstractSerializer, AnotatedSerializer

class AbstractAPIview(APIView):
    def get(self, request):
        abstrak = AbstractJPHIV.objects.all()
        serializer=AbstractSerializer(abstrak,many=True)
        return Response({"articles": serializer.data})

class AbstractAPIDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return AbstractJPHIV.objects.get(pk=pk)
        except AbstractJPHIV.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        abstrak = self.get_object(pk)
        serializer = AbstractSerializer(abstrak)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        abstrak = self.get_object(pk)
        serializer = AbstractSerializer(abstrak, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        abstrak = self.get_object(pk)
        abstrak.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AnnotatedAPIview(APIView):
    def get(self, request):
        annotated = AnotatedJPHIV.objects.all()
        serializer=AnotatedSerializer(annotated,many=True)
        return Response({"annotated": serializer.data})

class AnnotatedAPIDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return AnotatedJPHIV.objects.get(pk=pk)
        except AnotatedJPHIV.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        annotated = self.get_object(pk)
        serializer = AnotatedSerializer(annotated)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        annotated = self.get_object(pk)
        serializer = AnotatedSerializer(annotated, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        annotated = self.get_object(pk)
        annotated.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)