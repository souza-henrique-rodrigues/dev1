from django.urls import path
import relacionamentos.views as views_funcoes
from relacionamentos.views import saudacao_view, SaudacaoView, reporter_list, reporter_detail, reporter_delete
from relacionamentos.views import nome, Nome

app_name = 'relacionamentos'

urlpatterns = [
    path('funcao/teste', views_funcoes.primeira_view,name='primeira_view'),

    path('funcao/saudacao', views_funcoes.saudacao,name='saudacao'),

    #path('funcao/<str:name>', views_funcoes.nome),

    #saudacao classe view
    path('classe/saudacao', SaudacaoView.as_view(), name='saudacao_classe'),

    #view nome
    path('classe/teste/<str:nome>', Nome.as_view(), name='nome_classe'),

    path('reporter/function',reporter_list, name='reporter_function_list' ),

    path('reporter/function/read/<int:pk>',reporter_detail, name='reporter_function_detail' ),

    path('reporter/function/delete/<int:reporter_id>', reporter_delete, name='reporter_function_delete')
]