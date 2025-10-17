from web_system.urls import urlpatterns

urlpatterns = [
    path('funcao/teste', views_funcoes.primeira_view, name='teste'),
    path('')
]