# HOUSE ROCKET COMPANY

<img src="https://github.com/jefferson-datascience/project_insight_house_rocket/blob/main/images/house_rocket.jpg" alt="logo" style="zoom: 90%;" />

## Questão de Negócio

A empresa House Rocket é uma empresa do ramo imobiliária em que a sua atividade é a compra de imóveis abaixo do preço de mercado e, que após reformá-las, revende esses imóveis com preços compatíveis com o mercado. Dessa forma, o lucro da empresa vem da diferença entre o preço da revenda e compra. Dessa maneira, a empresa procura os melhores imóveis para obter os melhores negócios para que se tenha a maior lucratividade possível. Para ajudar nessa busca, o CEO da empresa procurou um Cientista de Dados. Portanto, para atender a demanda do CEO, devemos responder a duas perguntas:

1.) Quais imóveis a House Rocket Company devem comprar e por qual preço?

2.) Uma vez adquiridas esses imóveis, por qual preço devemos revendê-las?

No final desse projeto será entregue dois arquivos csv sendo que um é com as recomendações de compras e um com a recomendação com quais preços devem ser vendidos os imóveis. Além disso, será entregue um dashboard interativo com acesso a um mapa com os imóveis e os relatórios em csv para acessar de qualquer lugar.

## Atributos

|    Atributos    |                         Significado                          |
| :-------------: | :----------------------------------------------------------: |
|       id        |       Numeração única de identificação de cada imóvel        |
|      date       |                    Data da venda da casa                     |
|      price      |    Preço que a casa está sendo vendida pelo proprietário     |
|    bedrooms     |                      Número de quartos                       |
|    bathrooms    | Número de banheiros (0.5 = banheiro em um quarto, mas sem chuveiro) |
|   sqft_living   | Medida (em pés quadrado) do espaço interior dos apartamentos |
|    sqft_lot     |     Medida (em pés quadrado) quadrada do espaço terrestre     |
|     floors      |                 Número de andares do imóvel                  |
|   waterfront    | Variável que indica a presença ou não de vista para água (0 = não e 1 = sim) |
|      view       | Um índice de 0 a 4 que indica a qualidade da vista da propriedade. Varia de 0 a 4, onde: 0 = baixa  4 = alta |
|    condition    | Um índice de 1 a 5 que indica a condição da casa. Varia de 1 a 5, onde: 1 = baixo \|-\| 5 = alta |
|      grade      | Um índice de 1 a 13 que indica a construção e o design do edifício. Varia de 1 a 13, onde: 1-3 = baixo, 7 = médio e 11-13 = alta |
|  sqft_basement  | A metragem quadrada do espaço habitacional interior acima do nível do solo |
|    yr_built     |               Ano de construção de cada imóvel               |
|  yr_renovated   |                Ano de reforma de cada imóvel                 |
|     zipcode     |                         CEP da casa                          |
|       lat       |                           Latitude                           |
|      long       |                          Longitude                           |
| sqft_livining15 | Medida (em pés quadrado) do espaço interno de habitação para os 15 vizinhos mais próximo |
|   sqft_lot15    | Medida (em pés quadrado) dos lotes de terra dos 15 vizinhos mais próximo |


## Premissas de Negócios

Premissas assumidas:

* Os imóveis a serem comprados precisam ter condições maior ou igual a 3 e o seu valor tem que estar abaixo do preço mediano das regiões em que se localizam.
* A região em que os imóveis estão localizados e a estação do ano foram primordiais para a determinação do preço de venda.
    
## Estratégia de Solução

1. Coleta de dados no Kaggle
2. Entendimento do negócio
3. Tratamento de dados
4. Exploração dos dados
5. Responder as perguntas de negócio
6. Resultado para o negócio
7. Conclusão

## Os 5 principais insights

1. Imóveis com vista para a água são, na média, 210% mais caros em relação a imóveis que não tem vista para a água.
2. Imóveis com data de construção menor que 1955 não necessariamente são 50% mais baratos.
3. Imóveis com porão não necessariamente são mais caros, na verdade, existem regiões que se tem imóveis sem poraõ muito mais caros.
4. Imoveis com mais de 2 pisos são mais caros em quase todas as regiões.

## Resultados Finaceiros
|       Custo de Aquisição    |  Retorno Esperado das Vendas |    Lucro Estimado    |
| :-------------------------: | :--------------------------: | :------------------: |
|       US$ 4094212008.0      |       US$ 5276791316.98      |   US$ 1182579308.98  |


# ACESSE OS RESULTADOS DO PROJETO ATRAVÉS DO LINK: https://house-rocket-company-app.herokuapp.com/

