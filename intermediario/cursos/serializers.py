from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        # não sera mostrado o email em consultas apenas em cadastro
        extra_kwargs = {
            'email': {'write_only': True}
        }

        # model do model serializer
        model = Avaliacao

        # campos para apresentar quando os dados forem solicitados
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo',
        )


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
        )
