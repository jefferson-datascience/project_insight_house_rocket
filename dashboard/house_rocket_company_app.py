import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px


# Extraction

# Essa função realização a extração dos dados da máquina

def produto_final(file1, file2):
    dataset1 = pd.read_csv(file1)
    dataset2 = pd.read_csv(file2)

    return dataset1, dataset2


def base_de_dados(file):
    dataset = pd.read_csv(file)

    dataset['date'] = pd.to_datetime(dataset['date'])

    return dataset


def visualizacao_dados(dataset):
    filter_regiao = st.multiselect('Filtrar Região', dataset['zipcode'].unique())
    filter_price = st.slider('Preço Máximo', int(dataset['price'].min()),
                             int(dataset['price'].max()),
                             int(dataset['price'].mean()))

    if filter_regiao:
        df = dataset[data['zipcode'].isin(filter_regiao)]
    else:
        df = dataset

    df = df[df['price'] <= filter_price]

    return st.dataframe(df)


def visualizacao_imoveis_compra(dataset):
    filter_regiao = st.multiselect('Filtrar Região', dataset['zipcode'].unique())
    filter_price = st.slider('Preço Máximo', int(dataset['price'].min()), int(dataset['price'].max()),
                             int(dataset['price'].mean()))

    if filter_regiao:
        df = dataset[data['zipcode'].isin(filter_regiao)]
    else:
        df = dataset

    df = df[df['price'] <= filter_price]
    return st.dataframe(df)


def visualizacao_imoveis_venda(dataset):

    df = dataset

    return st.dataframe(df)

# Transformations

# CÓDIGO PRINCIPAL

data = base_de_dados('kc_house_data.csv')

st.sidebar.image('house_rocket_logo.png')
page = st.sidebar.selectbox("Navegue pelo Projeto", ["Apresentação", "Produto Final", "Hipóteses de Negócios"])
st.sidebar.write('Página criada por Jefferson Henrique Candido')


if page == "Apresentação":
    st.title('House Rocket Company')
    st.subheader('Questão de Negócio')
    st.write(
        'A House Rocket é uma empresa fictícia do ramo imobiliária em que a sua atividade é a compra de imóveis abaixo'
        ' do preço de mercado e,que após reformá-las, revende esses''imóveis com preços compatíveis como mercado. '
        'Dessa forma, o lucro da empresa vem da diferença entre o preço da revenda e compra.')
    st.write(
        'Com o objetivo de encontrar ótimas opções de negócios, o CEO da House Rocket Company contratou os serviços de'
        ' um Cientista de Dados para analisar o portfólio de imóveis que a sua empresa possui. Assim, o Cientista de'
        ' Dados tem duas questões principais para responder.')
    st.write('1.) Quais imóveis a House Rocket Company devem comprar e por qual preço?')
    st.write('2.) Uma vez adquiridas esses imóveis, por qual preço devemos revendê-las?')

    st.subheader('Premissas de Negócio')
    st.markdown('A região em que o imóvel se localiza foram essenciais para a decisão de aquisição.')
    st.markdown('As estações do ano e a região em que os imóveis se localizam também foram primordiais para a '
                'determinação do preço de venda.')
    st.markdown('O imóvel com 33 banheiro foi considerado um erro de digitação.')

    st.subheader('Estratégia de Resolução')

    st.markdown('1. Coleta de dados no Kaggle.')
    st.markdown('2. Entendimento do negócio')
    st.markdown('3. Tratamento de dados')
    st.markdown('4. Exploração dos dados')
    st.markdown('5. Responder as perguntas de negócio')
    st.markdown('6. Resultado para o negócio')

    st.subheader('Ferramentas Utilizadas')

    st.markdown('- Python 3.9.0')
    st.markdown('- Jupyter Notebook')
    st.markdown('- PyCharm')
    st.markdown('- Streamlit')
    st.markdown('- Heroku')

    st.subheader('Conclusão')

    st.write('No fim, conseguimos sugerir ótimas opções de compras de imóveis para o CEO com um ótimo potencial de '
             'negócio. Aém disso, retornamos para a equipe de negócios uma tabela com os melhores preços que esses '
             'imóveis devem ser vendidos levando em consideração a região e as estações do ano.')

    st.subheader('Resultados Financeiros')
    st.write('CUSTOS DE AQUISIÇÃO: US$ 4094212008.0')
    st.write('RETORNO ESPERADO DAS VENDAS: US$ 5276791316.98')
    st.write('LUCRO ESTIMADO: US$ 1182579308.98')

elif page == "Produto Final":

    st.header('Produto Final')

    imoveis_compra, imoveis_precos_venda = produto_final('imoveis_compra.csv', 'imoveis_preco_venda_estacao.csv')

    st.write('Logo abaixo temos o portfólio de imóveis da House Rocket Company. Esse é o conjunto de dados com o qual '
             'trabalhamos.')

    visualizacao_dados(data)
    # --------------------------------------------------------------------------------------------------------

    st.subheader('Tabela: Sugestões dos Imóveis a Serem Comprados')

    st.write('Após realizar a análise exploratória de dados do portfólio que a empresa forneceu, temos abaixo quais os'
             'imóveis devem ser adquridos atendem as condições colocadas no início:')
    st.write('1.) Os imóveis devem ter condição maior que 2.')
    st.write('2.) Os imóveis adquiridos tem preço de compra abaixo da média levando em consideração as regiões em que'
             'se localizam.')

    visualizacao_imoveis_compra(imoveis_compra)
    # --------------------------------------------------------------------------------------------------------

    st.subheader('Tabela: Preço de Vendas dos Imóveis')

    st.write('Uma vez adquiridos os imóveis, é necessário revendê-los. Dessa forma os preços de venda foram'
             'formulados com base na estação do ano e na mediana dos preços dos imóveis em relação a cada região'
             'onde eles se localizam.')
    st.write('De forma mais detalhada, os imóveis foram precificados da seguinte forma: ')
    st.write('Se o preço de compra do imóvel for menor que a mediana do preço, levando em consideração a estaçao '
             'do ano, então o preço de venda será o preço de compra + 30%.')
    st.write('Se o preço de compra do imóvel for maior que a mediana do preço, levando em consideração a estaçao '
             'do ano, então o preço de venda será o preço de compra + 10%.')
    st.write('Logo abaixo, temos a tabela dos imóveis com os preços a serem vendidos em cada estação do ano.')

    visualizacao_imoveis_venda(imoveis_precos_venda)

elif page == "Hipóteses de Negócios":

    st.header('Hipóteses de Negócios')

    st.write('Nessa seçaõ vamos responder a 5 hipóteses de negócios que vão permitir que o CEO da empresa e a '
             'sua equipe de negócios tenha uma visão mais ampla do negócio em que estão inseridos e possam tomar '
             'decisões mais estratégicas.')

    st.subheader('HIPÓTESE 1: Imóveis que possuem vista para água, são 30% mais caros, na média.')

    st.write('Essa afirmação é falsa. Na verdade, temos que imóveis com vista para a água são, na média, 210% mais '
             'caros que imóveis que não tem vista para a água.')
    st.write('TRADUÇÃO DE NEGÓCIO: Investir em imóveis com vista para água é um ótima opção.')

    st.image('hipotese_1.png')

    # --------------------------------------------------------------------------------------------------------------

    st.subheader('HIPÓTESE 2: Imóveis com data de construção menor que 1955, são 50% mais baratos, na média.')

    st.write('Nessa hipótese decidimos levar em consideração cada região em que os imóveis se localizam, pois isso tem '
             'uma forte influência sobre o preço. Por exemplo, ao analisar as regiões 98136, 98027 e 98042, vemos que '
             'os imóveis com data de construção menor que 1955 são são em torno de 35% a 50% mais baratos. Dessa forma '
             'para essas regiões é um ótima opção investir em imóveis com construção menor que 1955.')
    st.write('Todavia, na região 98198, os imóveis com data de construção menor que 1955 são, na média, 50% mais caros '
             'Logo, para a tradução de negócio, nessa região é um ótimo negócio investir em imóveis com ano de '
             'construção maior que 1955.')

    st.write('TRADUÇAÕ DE NEGÓCIO: Nas regiões 98136, 98027 e 98042 é uma ótima opção de investimento os imóveis com '
             'data de construção menor que 1955. Entretanto, na região 98198, é um ótimo negócio investir em imóveis '
             'com ano de construção maior que 1955. Em relação aos outras regiões a nossa hipótese de negócio é falsa. '
             'Assim, a decisão sobre as outras regiões estaria totalmente nas mão da equipe, uma vez que as '
             'informações foram fornecidas pelo Cientista de Dados.')

    st.image('hipotese_2.png')

    # -------------------------------------------------------------------------------------------------------------

    st.subheader('HIPÓTESE 3: Imóveis com porão são 50% mais caros na média.')

    st.write('Essa hipótese é falsa. Podemos ver em todas as regiões que essa diferença no preço é relativamente '
             'pequena.')
    st.write('TRADUÇÃO DE NEGÓCIO: Investir em imóveis independente se tem porão ou não.')

    st.image('hipotese_3.png')

    # -------------------------------------------------------------------------------------------------------------

    st.subheader('HIPÓTESE 4: Imóveis com mais de 2 pisos são em média, 40 % mais caros.')

    st.write('Ao analisar as regiões vemos que em quase todas que possuem imóveis com mais de 2 pisos a hipótese é '
             'válida. Uma região em que a hipótese perde total validade é a 98004. Além disso, existem regiões em que '
             'não faz diferença entre investir em imóveis com mais de 2 pisos ou não, como por exemplo a região 98119. '
             'Assim, vemos que a região interfere bastante na tomada de decisão.')

    st.write('TRADUÇÃO DE NEGÓCIO: As regiões 98006, 98008, 98014, 98033, 98034, 98038 e 98074 são ótimas opções para '
             'investir. ')

    st.image('hipotese_4.png')

    # --------------------------------------------------------------------------------------------------------------

    st.subheader('HIPÓTESE 5: Imóveis com condições abaixo de 3 são, na média, 40% mais baratos.')

    st.write('Essa hipótese é verdadeira em geral, ou seja, os imóveis com condição abaixo de 3 são 40% mais baratos '
             'na média. Entretanto, existe um região em que a hipótese perde totalmente a sua validade, que é a '
             'região 98116.')

    st.write('Não podemos afirmar se imóveis com condições abaixo de 3 são ótimas opções de compra, pois seria '
             'necessário ter informações sobre o quanto que é gasto em uma reforma para saber se no final o retorno '
             'financeiro seria bom ou não.')

    st.image('hipotese_5.png')
