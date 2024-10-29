from abc import ABC, abstractmethod
from apis import *

# Adapter Interface genérica para os adapters
class TransportadoraAdapter(ABC):
    @abstractmethod
    def calcularFrete(self, peso, dimensoes, enderecoDestino):
        pass

    @abstractmethod
    def gerarEtiqueta(self, pedidoId):
        pass

    @abstractmethod
    def acompanharPedido(self, codigoRastreamento):
        pass


# Adapters para cada Transportadora
class TransportadoraAdapterA(TransportadoraAdapter):
    def __init__(self):
        self.transportadora = TransportadoraA()

    def calcularFrete(self, peso, dimensoes, enderecoDestino):
        return self.transportadora.calcular_envio(peso, dimensoes, enderecoDestino)

    def gerarEtiqueta(self, pedidoId):
        return self.transportadora.criar_etiqueta(pedidoId)

    def acompanharPedido(self, codigoRastreamento):
        return self.transportadora.obter_status(codigoRastreamento)


class TransportadoraAdapterB(TransportadoraAdapter):
    def __init__(self):
        self.transportadora = TransportadoraB()

    def calcularFrete(self, peso, dimensoes, enderecoDestino):
        largura, altura, profundidade = dimensoes
        return self.transportadora.calcular_preco_envio(peso, largura, altura, profundidade, enderecoDestino)

    def gerarEtiqueta(self, pedidoId):
        return self.transportadora.gerar_codigo_etiqueta(pedidoId)

    def acompanharPedido(self, codigoRastreamento):
        return self.transportadora.status_envio(codigoRastreamento)


class TransportadoraAdapterC(TransportadoraAdapter):
    def __init__(self):
        self.transportadora = TransportadoraC()

    def calcularFrete(self, peso, dimensoes, enderecoDestino):
        dados = {'peso': peso, 'dimensoes': dimensoes, 'endereco': enderecoDestino}
        return self.transportadora.calcular_frete(dados)

    def gerarEtiqueta(self, pedidoId):
        return self.transportadora.criar_etiqueta_envio({'id': pedidoId})

    def acompanharPedido(self, codigoRastreamento):
        return self.transportadora.consultar_status(codigoRastreamento)
