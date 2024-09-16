# Previsão de Custo de Anúncio por Região

Este projeto é uma API desenvolvida em FastAPI para prever o custo de anúncio em diferentes regiões, utilizando informações sobre a importância do transporte público e da infraestrutura de cada região. A previsão é feita com base em um modelo de regressão linear treinado em dados históricos.

## Funcionalidades

- **Criação de nova região**: Adicione uma nova região com dados de importância do transporte público e infraestrutura.
- **Previsão de custo**: Consulte o preço previsto para uma determinada região, com base no modelo de IA.

## Estrutura do Projeto

- **FastAPI**: Backend da aplicação.
- **Scikit-learn**: Utilizado para o treinamento e previsão com o modelo de regressão linear.
- **Pandas**: Utilizado para manipulação dos dados.
- **Numpy**: Utilizado para operações matemáticas e manipulação de arrays.

## Instalação

Instale utilizando o organizador de pacotes pip 

```bash
    pip install -r requirements.txt
```
    

## Utilização

```bash
    python -m uvicorn main:app --reload
```

## Endpoints

### 1. Criar Nova Região

`POST /regiao/`

Cria uma nova região com a importância do transporte público e infraestrutura.

- **Request Body**:
  ```json
  {
    "imp_transp_pub": 3.5,
    "imp_infra": 7.0,
    "nome": "Nome da Região"
  }
Retorno:

```json
{
  "preco_previsto": 51.0
}
```


### 1. Criar Nova Região

`GET /previsao/{nome}`

Prevê o custo do anúncio baseado nas informações da região previamente cadastrada.

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `nome` | `str` | **Obrigatório**. Nome da região |

Retorno:

```json
{
  "regiao": "Nome da Região",
  "valor_previsao": 1200.00
}
```

