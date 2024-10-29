from adapters import *

# Façade para o sistema de pedidos
class SistemaPedidosFacade:
    def __init__(self):
        self.transportadoras = {
            "A": TransportadoraAdapterA(),
            "B": TransportadoraAdapterB(),
            "C": TransportadoraAdapterC()
        }

    def calcularFrete(self, peso, dimensoes, enderecoDestino):
        fretes = {
            nome: adapter.calcularFrete(peso, dimensoes, enderecoDestino) for nome, adapter in self.transportadoras.items()
        }
        melhor_opcao = min(fretes, key=fretes.get)
        return melhor_opcao, fretes[melhor_opcao]

    def gerarEtiqueta(self, pedidoId, transportadora):
        return self.transportadoras[transportadora].gerarEtiqueta(pedidoId)

    def acompanharPedido(self, codigoRastreamento, transportadora):
        return self.transportadoras[transportadora].acompanharPedido(codigoRastreamento)

