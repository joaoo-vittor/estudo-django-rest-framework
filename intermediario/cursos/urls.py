from django.urls import path

<<<<<<< HEAD
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
=======
from .views import CursoAPIView, AvailiacaoAPIView

urlpatterns = [
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvailiacaoAPIView.as_view(), name='avaliacoes'),
>>>>>>> a9e1f1e6e4bd93075375bd866e25a0f523807a2f
]
