from django.urls import path
from .views import addcarrinho, exibir_carrinho, excluir_carrinho, finalizar_compra

urlpatterns = [
    path('addcarrinho/<int:produto_id>/', addcarrinho, name='addcarrinho'),
    path('', exibir_carrinho, name='exibir_carrinho'),
    path('excluir_carrinho/', excluir_carrinho, name='excluir_carrinho'),
    path('finalizar_compra/', finalizar_compra, name='finalizar_compra')
]