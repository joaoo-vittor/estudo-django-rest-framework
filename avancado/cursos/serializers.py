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
    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True,
    #                                                  read_only=True,
    #                                                  view_name='avaliacao-detail')

    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
        )
