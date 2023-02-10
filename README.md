# HOUSE ROCKET COMPANY

<img src="https://github.com/jefferson-datascience/project_insight_house_rocket/blob/main/images/house_rocket.jpg" alt="logo" style="zoom: 90%;" />

O projeto tem como objetivo realizar uma análise exploratória dos dados do portfólio de imóveis com o ojetivo de encontrar os melhores imóveis para o negócio da compania.

O contexto de negócio é fictício. Todavia, o planejamento, execução, desenvolvimento e implementação da solução seguem todos os passos de um projeto real.

## PROBLEMA DE NEGÓCIO

A empresa House Rocket é uma empresa do ramo imobiliário em que a sua atividade é a compra de imóveis abaixo do preço de mercado e, que após reformá-los, revende esses imóveis com preços compatíveis com o mercado. Dessa forma, o lucro da empresa vem da diferença entre o preço da revenda e compra. Dessa maneira, a empresa procura os melhores imóveis para obter os melhores negócios para que se tenha a maior lucratividade possível. Para ajudar nessa busca, o CEO da empresa procurou um Cientista de Dados( no caso, eu) para encontrar esses melhores imóveis para o negócio. Portanto, para atender a demanda do CEO, devemos responder a duas perguntas:

1.) Quais imóveis a House Rocket Company devem comprar e por qual preço?

2.) Uma vez adquiridas esses imóveis, por qual preço devemos revendê-los?

### Planejamento de Solução

**Qual é a solução?** A solução para esse problema é realizar uma análise exploratória dos dados do portfólio da empresa com o objetivo de encontrar os melhores imóveis que possuam o maior retorno possível e, para que isso aconteça, será adota do o seguinte critério de compra:

- Se o preço do imóvel é menor que o preço mediano de mercado e possue condições minimamente decentes, então esse imóvel receberá a sugestão de compra. Caso contrário, receberá a sugestão de não compra.

Para a determinação do preço de revenda dos imóveis adquiridos, foi colocado o seguinte critério levando em consideração a sazonalidade do ano: 
- Se o preço de compra for menor que o preço mediano de mercado, então o preço de venda será o preço de compra + 30%. 
- Se o preço de compra for maior que o preço mediano de mercado, então o preço de venda será o preço de compra + 10%.

Além disso, no decorrer do projeto, como consequência da análise exploratória, teremos alguns insights de negócio.

**Como vai ser a entrega do produto final?**

Será entregue dois produtos no final do projeto:

**i.** Será entregue dois arquivos csv's sendo que um é com as recomendações de compras e um com as recomendação de quais preços devem ser vendidos os imóveis depois de adquiridos.

**ii.** Para otimizar o processo de tomada decisão sobre qual imóvel comprar e qual preço vender, de acordo com a sazonalidade, será entregue um dashboard interativo que estará hospedade em um serviço de nuvem para que o CEO e a equipe de negócio possa acessar essas informações de qualquer lugar, bastando apenas ter um dispositivo e internet.

## ATRIBUTOS

|    Atributos    |                         Significado                                                                                              |
| :-------------: | :-------------------------------------------------------------------------------------------------------------------------------:|             
|       id        |                        Numeração única de identificação de cada imóvel                                                           |
|      date       |                                     Data da venda da casa                                                                        |
|      price      |                     Preço que a casa está sendo vendida pelo proprietário                                                        |
|    bedrooms     |                                       Número de quartos                                                                          |
|    bathrooms    |                  Número de banheiros (0.5 = banheiro em um quarto, mas sem chuveiro)                                             |
|   sqft_living   |                  Medida (em pés quadrado) do espaço interior dos apartamentos                                                    |
|    sqft_lot     |                      Medida (em pés quadrado) quadrada do espaço terrestre                                                       |
|     floors      |                                  Número de andares do imóvel                                                                     |
|   waterfront    | Variável que indica a presença ou não de vista para água (0 = não e 1 = sim)                                                     |
|      view       | Um índice de 0 a 4 que indica a qualidade da vista da propriedade. Varia de 0 a 4, onde: 0 = baixa  4 = alta                     |
|    condition    | Um índice de 1 a 5 que indica a condição da casa. Varia de 1 a 5, onde: 1 = baixo \|-\| 5 = alta                                 | 
|      grade      | Um índice de 1 a 13 que indica a construção e o design do edifício. Varia de 1 a 13, onde: 1-3 = baixo, 7 = médio e 11-13 = alta |
|  sqft_basement  | A metragem quadrada do espaço habitacional interior acima do nível do solo                                                       |
|    yr_built     |                                Ano de construção de cada imóvel                                                                  |
|  yr_renovated   |                                 Ano de reforma de cada imóvel                                                                    |
|     zipcode     |                                          CEP da casa                                                                             |
|       lat       |                                            Latitude                                                                              |
|      long       |                                           Longitude                                                                              |
| sqft_livining15 |                  Medida (em pés quadrado) do espaço interno de habitação para os 15 vizinhos mais próximo                        |
|   sqft_lot15    |                  Medida (em pés quadrado) dos lotes de terra dos 15 vizinhos mais próximo                                        |


## PREMISSAS DE NEGÓCIO

Premissas assumidas:

* Os imóveis a serem comprados precisam ter condições maior ou igual a 3 e o seu valor tem que estar abaixo do preço mediano das regiões em que se localizam.
* A região em que os imóveis estão localizados e a estação do ano foram primordiais para a determinação do preço de venda.
    
## ESTRATÉGIA DE RESOLUÇÃO

**Etapa 00 - Carregamento dos Dados:** Carregamento dos dados e uma breve análise sobre os atributos.
**Etapa 01 - Descrição dos Dados:** Estudo dos atributos, verificação das dimensão dos dados, checagem e remoção de valores nulos, mudança da natureza das variáveis, estudo da estatística descritiva dos dados.
**Etapa 02 - Feature Engineering:** Criação de novas features para resolver o problema de negócio.
**Etapa 03 - Análise Exploratória dos Dados:** Anáise dos preços medianos por região para compra dos imóveis, análise dos precos medianos por sazonalidade para precificação de vendas dos imóveis e estudo aprofundado dos dados para geração de hipóteses de negócio.
**Etapa 04 - Respondedo as questões e as hipóteses de negócios:** Respondendo as questões de negócio, validação das hipóteses, geração de insights e documentação das recomendações de compras, e, de vendas de acordo com a sazonalidade.
**Etapa 05 - Resultados de Negócio:** Criação de tabela com o lucro esperado de acordo com cada sazonalidade, caso todos os imóveis sejam vendidos naquela estação.


## VALIDAÇÃO DAS HIPÓTESES + TOP 5 INSIGHTS GERADOS

1. Imóveis com vista para a água são, na média, 210% mais caros em relação a imóveis que não tem vista para a água.
2. Imóveis com data de construção menor que 1955 não necessariamente são 50% mais baratos.
3. Imóveis com porão não necessariamente são mais caros, na verdade, existem regiões que se tem imóveis sem poraõ muito mais caros.
4. Imoveis com mais de 2 pisos são mais caros em quase todas as regiões.

## Resultados Finaceiros
|       Custo de Aquisição    |  Retorno Esperado das Vendas |    Lucro Estimado    |
| :-------------------------: | :--------------------------: | :------------------: |
|       US$ 4094212008.0      |       US$ 5276791316.98      |   US$ 1182579308.98  |


#### ACESSE OS RESULTADOS DO PROJETO ATRAVÉS DO LINK: https://jefferson-datascience-dashboard-house-rocket-company-app-3k3nq6.streamlit.app/
