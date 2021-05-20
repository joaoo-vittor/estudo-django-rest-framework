from django.http import request
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
    API de Curso "Estudo Django REST Framework"
    """

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        # serializando
        serializer = CursoSerializer(data=request.data)
        # verificando se os dados estão validos
        serializer.is_valid(raise_exception=True)
        # salvando dados na base
        serializer.save()
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response({"msg": "Curso criado com sucesso"}, status=status.HTTP_201_CREATED)
        return Response({"id": serializer.data['id'],
                         "titulo": serializer.data['titulo']},
                        status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    """
    API de Avaliacao "Estudo Django REST Framework"
    """

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
