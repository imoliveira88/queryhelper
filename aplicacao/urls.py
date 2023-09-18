from django.urls import path
from aplicacao.views import deleta_query, inclui_query, inclui_sistema, lista_queries, lista_sistemas, app_view, deleta_sistema

urlpatterns = [
    path('aplicacao/', app_view),
    # path('piramide/<str:pk>/', sistema, name="sistema")
    path('', lista_sistemas),
    path('aplicacao/lista_sistemas', lista_sistemas, name="sistemas"),
    path('aplicacao/inclui_sistema', inclui_sistema, name="inclui_sistema"),
    path('aplicacao/inclui_query', inclui_query, name="inclui_query"),
    path('aplicacao/lista_queries', lista_queries, name="queries"),
    path('aplicacao/deleta_sistema/<int:id>/', deleta_sistema, name='deleta_sistema'),
    path('aplicacao/deleta_query/<int:id>/', deleta_query, name='deleta_query'),
]

