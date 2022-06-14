# HOUSE ROCKET COMPANY

## Questão de Negócio

A empresa House Rocket é uma empresa do ramo imobiliária em que a sua atividade é a compra de imóveis abaixo do preço de mercado e, que após reformá-las, revende esses imóveis com preços compatíveis com o mercado. Dessa forma, o lucro da empresa vem da diferença entre o preço da revenda e compra. Dessa maneira, a empresa procura os melhores imóveis para obter os melhores negócios para que se tenha a maior lucratividade possível. Para ajudar nessa busca, o CEO da empresa procurou um Cientista de Dados. Portanto, para atender a demanda do CEO, devemos responder a duas perguntas:

1.) Quais imóveis a House Rocket Company devem comprar e por qual preço?

2.) Uma vez adquiridas esses imóveis, por qual preço devemos revendê-las?

No final desse projeto será entregue dois arquivos csv sendo que um é com as recomendações de compras e um com a recomendação com quais preços devem ser vendidos os imóveis. Além disso, será entregue um dashboard interativo com acesso a um mapa com os imóveis e os relatórios em csv para acessar de qualquer lugar.

## Premissas de Negócios

Premissas assumidas:

* Os valores iguais a zero na coluna yr_built são imóveis que não foram renovados.
* Os imóveis a serem comprados precisam ter condições maior ou igual a 3 e o seu valor tem que estar abaixo do preço mediano das regiões em que se localizam.
* A região em que os imóveis estão localizados e a estação do ano foram primordiais para a determinação do preço de venda.
* Os preços de vendas dos imóveis adquiridos seram estabelecidos da seguinte forma:

    Se o preço de compra do imóvel for maior que a mediana do preço da região em que ele se localiza, levando em consideração a estação do ano, então o preço de venda será o preço de compra + 10%.
    
    Se o preço de compra do imóvel for menor que a mediana do preço da região em que ele se localiza, levando em consideração a estação do ano, então o preço de venda será o preço de compra + 30%.
    


## Atributos

| ID | Código de identificação do imóvel |
| date | Preço de venda do imóvel |
 


