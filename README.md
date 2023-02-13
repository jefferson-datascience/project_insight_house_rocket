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

### Ferramentas Utilizadas

- Python 3.9
- Jupyter Notebook
- Metodologia CRISP-DM
- Git 
- Framework Streamlit
    
## ESTRATÉGIA DE RESOLUÇÃO

**Etapa 00 - Carregamento dos Dados:** Carregamento dos dados e uma breve análise sobre os atributos.

**Etapa 01 - Descrição dos Dados:** Estudo dos atributos, verificação das dimensão dos dados, checagem e remoção de valores nulos, mudança da natureza das variáveis, estudo da estatística descritiva dos dados.

**Etapa 02 - Feature Engineering:** Criação de novas features para resolver o problema de negócio.

**Etapa 03 - Análise Exploratória dos Dados:** Anáise dos preços medianos por região para compra dos imóveis, análise dos precos medianos por sazonalidade para precificação de vendas dos imóveis e estudo aprofundado dos dados para geração de hipóteses de negócio.

**Etapa 04 - Respondedo as questões e as hipóteses de negócios:** Respondendo as questões de negócio, validação das hipóteses, geração de insights e documentação das recomendações de compras, e, de vendas de acordo com a sazonalidade.

**Etapa 05 - Resultados de Negócio:** Criação de tabela com o lucro esperado de acordo com cada sazonalidade, caso todos os imóveis sejam vendidos naquela estação.


## VALIDAÇÃO DAS HIPÓTESES + TOP 5 INSIGHTS GERADOS


##### Afirmação 1: Imóveis que possuem vista para água são 30% mais caros, na média em relação aos imóveis  sem vista para água.

Em geral essa afirmação é falsa. A mediana dos preços é de R$ 450.000,00. Além disso, conseguimos observar que Imóveis com vista para a água possuem um preço mediano de R$ 1.400.000,00, logo, concluímos que imóveis com vista para água são, na média, 300% mais caro. Logo, o insight gerado aqui é: Imóveis com vista para a água são uma ótima opção de investimento.

<img src="https://github.com/jefferson-datascience/project_insight_house_rocket/blob/main/images/hipotese_1.png" alt="logo" style="zoom: 90%;" />

##### Afirmação 2: Imóveis com data de construção menor que 1955 são 50% mais baratos, na média, em relação a imóveis com construção maior que 1955.

Em geral essa afirmação é falsa. Em termos de ano de construção, ela possuem a mediana de preço praticamente iguais. Uma vez que a mediana dos preços é de R$ 450.000,00, imóveis com ano de construção menor que 1955 possuem uma mediana de preços de R$452.000,00 e imóveis com ano de construção maior que 1955 possuem uma mediana de preços de R$ 450.000,00

<img src="https://github.com/jefferson-datascience/project_insight_house_rocket/blob/main/images/hipotese_2.png" alt="logo" style="zoom: 100%;" />

##### Afirmação 3: Imóveis com porão são 50% mais caros na média.

Essa afirmação é falsa. Observe que o preço mediano dos imóveis é R$ 450.000,00, todavia o preço mediano dos imóveis sem porão é de R$ 411.500,00 e o preço mediano dos imóveis com porão R$ 515.000,00. O interessante é que conseguimos extrair um insight relevante: Imóveis com porão é uma boa opção de negócio, uma vez que o seu valor é, na média, R$ 100.000,00 mais caro.

<img src="https://github.com/jefferson-datascience/project_insight_house_rocket/blob/main/images/hipotese_3.png" alt="logo" style="zoom: 100%;" />

##### Afirmação 4: Imóveis com mais de 2 pisos são em média, 40 % mais caros.

Essa afirmação é falsa. Observe que o preço mediano dos imóveis é R$ 450.000,00, todavia o preço mediano dos imóveis com mais de dois andares é de R$ 527.600,00 e o preço mediano  dos imóveis com menos de dois andares R$ 449.950,00. O interessante é que conseguimos extrair um insight relevante: Imóveis com mais de dois andares é uma boa opção de negócio, uma vez que o seu valor é, na média, R$ 80.000,00 mais caro.

<img src="https://github.com/jefferson-datascience/project_insight_house_rocket/blob/main/images/hipotese_4.png" alt="logo" style="zoom: 100%;" />

##### Afirmação 5:  Imóveis com condições abaixo de 3 são, na média, 35% mais baratos.

Essa afirmação é verdadeira. Observe que o preço mediano dos imóveis é R$ 450.000,00, todavia o preço mediano dos imóveis com condição abaixo  de 3 é de R$ 277.000,00 e o preço mediano  dos imóveis com menos de dois andares R$ 451.000,00. O interessante é que conseguimos extrair um insight relevante: Imóveis com condições abaixo de 3 podem ser um boa opção de negócio, uma vez que o seu valor é, na média, R$ 150.000,00 mais barato que a média do preço geral. Entretanto, seria primordial saber o custo de reforma de um imóvel nessa situação para saber se vale a pena, de fato, investir em imóveis dessa natureza.

<img src="https://github.com/jefferson-datascience/project_insight_house_rocket/blob/main/images/hipotese_5.png" alt="logo" style="zoom: 100%;" />


## RESULTADOS FINANCEIROS

|           Custo de Aquisição      |   Retorno Esperado das Vendas  |     Lucro Estimado       |
|     :-------------------------:   |  :--------------------------:  |   :------------------:   |
|       R$ 4.094.212.008,00         |         R$ 5.276.791.316,98    |    R$ 1.182.579.308,98   |

## PRÓXIMOS PASSOS

Em um próximo ciclo desse projeto, será colocado como objetivo:

- Treinar o CEO e a equipe de negócio para utilizar o dashboard.
- Realizar uma análise profunda dos imóveis com condições menor que 3 para saber se vale a pena o investimento nesses tipos de imóveis.
- Geração de novos insights de negócios.
- Setorização da análise exploratória de dados por região para extrair os melhores negócios de cada localidade.
 
Para acessar o Dashboard do projeto e o notebook com os códigos do projeto desenvolvido, basta clicar nos links abaixo:

**Dashboard da House Rocket:** https://jefferson-datascience-dashboard-house-rocket-company-app-3k3nq6.streamlit.app/

**NoteBook com os códigos e desenvolvimentos:** [Notebook House Rocket](https://github.com/jefferson-datascience/project_insight_house_rocket/blob/main/project_insight_house_rocket.ipynb)

**Código do Desenvolvimento do Dashboard**: [Código do Dashboard](https://github.com/jefferson-datascience/dashboard_house_rocket/blob/main/house_rocket_company_app.py)
