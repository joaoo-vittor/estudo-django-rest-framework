from django.urls import path

from .views import CursoAPIView, CursosAPIView, AvaliacaoAPIView, AvaliacoesAPIView

urlpatterns = [
    # coleções
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),

    # individuais
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('avaliacoes/<int:avaliacao_pk>/',
         AvaliacaoAPIView.as_view(), name='avaliacao'),

    # Com filtros
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/',
         AvaliacaoAPIView.as_view(), name='curso_avaliacao'),
    path('cursos/<int:curso_pk>/avaliacoes/',
         AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
]
