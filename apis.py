import random

# Simulação das APIs das transportadoras
class TransportadoraA:
    def calcular_envio(self, peso, dimensoes, destino):
        return peso * 1.2 + random.randint(10, 20)

    def criar_etiqueta(self, pedido_id):
        return f"EtiquetaA-{pedido_id}"

    def obter_status(self, codigo_rastreamento):
        return f"StatusA para {codigo_rastreamento}"


class TransportadoraB:
    # pode receber outros parametros e executar outras operações
    def calcular_preco_envio(self, peso, largura, altura, profundidade, endereco):
        return peso * 1.1 + random.randint(15, 25)

    def gerar_codigo_etiqueta(self, id_pedido):
        return f"EtiquetaB-{id_pedido}"

    def status_envio(self, rastreio_id):
        return f"StatusB para {rastreio_id}"


class TransportadoraC:
    def calcular_frete(self, dados):
        return dados['peso'] * 1.3 + random.randint(5, 15)

    def criar_etiqueta_envio(self, pedido):
        return f"EtiquetaC-{pedido['id']}"

    def consultar_status(self, tracking_code):
        return f"StatusC para {tracking_code}"
