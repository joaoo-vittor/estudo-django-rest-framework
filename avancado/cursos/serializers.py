from rest_framework import serializers
from .models import Curso, Avaliacao
from django.db.models import Avg


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

    #   validate_<nome do CAMPO> Padrão do Serializer
    def validate_avaliacao(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError(
            'Avaliação precisa ser um interio entra 1 e 5.')


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True,
    #                                                  read_only=True,
    #                                                  view_name='avaliacao-detail')

    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes',
        )

    # padrão get_<NOME DO ATRIBUTO>
    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(
            Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2) / 2
