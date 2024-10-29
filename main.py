from facade import SistemaPedidosFacade

# Instanciando o sistema
# apenas a facade final foi importada para esse módulo
sistema = SistemaPedidosFacade()

# Calcular frete
# Gerar Ticket
peso = 10
dimensoes = (20, 30, 40)  # largura, altura, profundidade
enderecoDestino = "Rua Exemplo, 123"
pedido_id = "PED12345"

# Achar a melhor transportadora
melhor_transportadora, custo_frete = sistema.calcularFrete(peso, dimensoes, enderecoDestino)
print(f"Melhor transportadora: {melhor_transportadora} com custo: R${custo_frete}")

# Gerar Ticket
pedido_id = "PED12345"
etiqueta = sistema.gerarEtiqueta(pedido_id, melhor_transportadora)
print(f"Etiqueta gerada: {etiqueta}")

# Acompanhar pedido
codigo_rastreamento = "R123456789BR"
status = sistema.acompanharPedido(codigo_rastreamento, melhor_transportadora)
print(f"Status do pedido: {status}")