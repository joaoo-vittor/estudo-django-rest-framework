from django.urls import path

from .views import CursoAPIView, AvailiacaoAPIView

urlpatterns = [
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvailiacaoAPIView.as_view(), name='avaliacoes'),
]
