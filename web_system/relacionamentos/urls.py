from django.urls import path
import relacionamentos.views as views_funcoes
from relacionamentos.views import (saudacao_view, SaudacaoView, reporter_list, reporter_detail, reporter_delete,
                                   reporter_change_name, reporter_create, reporter_update, ReporterDetailView,
                                   ReporterUpdateView)
from relacionamentos.views import nome, Nome

from relacionamentos.views.reporter_views import ReporterListView

from relacionamentos.views.reporter_generic import ReporterGenericList, ReporterGenericRead, ReporterGenericDelete, ReporterGenericCreate, ReporterGenericUpdate

app_name = 'relacionamentos'

urlpatterns = [
    path('funcao/teste', views_funcoes.primeira_view,name='primeira_view'),

    path('funcao/saudacao', views_funcoes.saudacao,name='saudacao'),

    path('classe/saudacao', SaudacaoView.as_view(), name='saudacao_classe'),

    path('classe/teste/<str:nome>', Nome.as_view(), name='nome_classe'),

    path('reporter/function',reporter_list, name='reporter_function_list' ),

    path('reporter/function/read/<int:pk>',reporter_detail, name='reporter_function_detail' ),

    path('reporter/function/delete/<int:id>', reporter_delete, name='reporter_function_delete'),

    path('reporter/function/change_name/<int:id>', reporter_change_name, name='reporter_function_change_name'),

    path('reporter/function/create', reporter_create, name='reporter_function_create'),

    path('reporter/function/update/<int:id>', reporter_update, name='reporter_function_update'),

    path('reporter/class/list', ReporterListView.as_view(), name='reporter_class_list'),

    path('reporter/class/read/<int:id>', ReporterDetailView.as_view(), name='reporter_class_read'),

    path('reporter/class/update/<int:id>', ReporterUpdateView.as_view(), name='reporter_class_update'),

    #url using generic to list
    path('reporter/generic/list', ReporterGenericList.as_view(), name='reporter_generic_list'),

    #url using generic to list one
    path('reporter/generic/read/<int:pk>', ReporterGenericRead.as_view(), name='reporter_generic_read'),

    #url using generic to delete
    path('reporter/generic/delete/<int:pk>', ReporterGenericDelete.as_view(), name='reporter_generic_delete'),

    #url using generic to create
    path('reporter/generic/create', ReporterGenericCreate.as_view(), name='reporter_generic_create'),

#url using generic to update
    path('reporter/generic/create', ReporterGenericUpdate.as_view(), name='reporter_generic_update'),

]