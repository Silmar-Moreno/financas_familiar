from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('', login_required(views.TransacaoListView.as_view()), name='transacao_list'),
    path('transacao/nova/', login_required(views.TransacaoCreateView.as_view()), name='transacao_create'),
    path('transacao/<int:pk>/editar/', login_required(views.TransacaoUpdateView.as_view()), name='transacao_update'),
    path('categorias/', login_required(views.CategoriaListView.as_view()), name='categoria_list'),
    path('categoria/nova/', login_required(views.CategoriaCreateView.as_view()), name='categoria_create'),
    path('resumo/', login_required(views.resumo), name='resumo'),
    path('categoria/<int:pk>/editar/', login_required(views.CategoriaUpdateView.as_view()), name='categoria_edit'),
    path('categoria/<int:pk>/excluir/', login_required(views.CategoriaDeleteView.as_view()), name='categoria_delete'),
    path('salvar-saldos-faturas/', login_required(views.salvar_saldos_faturas), name='salvar_saldos_faturas'),
]


