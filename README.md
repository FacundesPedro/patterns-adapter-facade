# Sistema de Gestão aplicando os padrões Adapter e Facade

Este projeto demonstra um sistema modularizado de gestão de pedidos para e-commerce que integra múltiplos provedores de envio usando Python. Ele utiliza os padrões de projeto **Facade** e **Adapter** para fornecer uma interface unificada para cálculo de frete, geração de etiquetas e rastreamento de encomendas de diferentes transportadoras.

## Estrutura 

- **`facade.py`**: Contém a classe `SistemaPedidosFacade`, que fornece uma única interface para gerenciar operações de envio.
- **`adapters.py`**: Classe Base e outras Classes Adapter que envolvem a API de cada transportadora para fornecer uma interface consistente.
- **`apis.py`**: Classes de API simuladas das transportadoras (`TransportadoraA`, `TransportadoraB`, `TransportadoraC`) com métodos e formatos específicos.

## Principais Funcionalidades

1. **Padrão Facade**: `SistemaPedidosFacade` simplifica a interação com várias transportadoras, oferecendo um único ponto de acesso para operações de envio.
2. **Padrão Adapter**: Os Adapters padronizam a comunicação entre a facade e as APIs únicas de cada transportadora.
3. **Seleção Automática de Transportadora**: A facade seleciona a melhor transportadora com base em fatores como o menor custo de envio.

## Requisitos

- Python 3.12 ou superior.

## Como Executar

1. Clone o repositório:
```bash
  git clone https://github.com/FacundesPedro/patterns-adapter-facade
  cd patterns-adapter-facade
```
 
2. Execute o arquivo main.py para simular o sistema:
```bash
  python main.py
```