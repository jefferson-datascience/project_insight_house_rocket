# ----------------------------- Importação das Bibliotecas -------------------------------------------------------------

import folium
import pandas as pd
import numpy as np
import streamlit as st
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

# layout
st.set_page_config(layout='wide')


# ------------------------------ Extraction ---------------------------------------------------------------------------


# Carregamento dos dados
@st.cache(allow_output_mutation=True)
def base_de_dados(file):
    dataset = pd.read_csv(file)

    dataset['date'] = pd.to_datetime(dataset['date'])

    return dataset


@st.cache(allow_output_mutation=True)
def statistic_descritive(dataset):
    # Separando somente os dados numéricos
    num_attributes = dataset.select_dtypes(include=['int64', 'float64'])

    # ------------ Tendências Centrais -----------------------------------
    # Média
    mean = pd.DataFrame(num_attributes.apply(np.mean)).T

    # Mediana
    median = pd.DataFrame(num_attributes.apply(np.median)).T

    # ------------ Tendências de Dispersão -------------------------------

    # Máximo
    maximo = pd.DataFrame(num_attributes.apply(np.max)).T

    # Mínimo
    minimo = pd.DataFrame(num_attributes.apply(np.min)).T

    # Intervalo(Range)
    intervalo = pd.DataFrame(num_attributes.apply(lambda x: x.max() - x.min())).T

    # Desvio Padrão
    desvio = pd.DataFrame(num_attributes.apply(np.std)).T

    # Skewness
    skew = pd.DataFrame(num_attributes.apply(lambda x: x.skew())).T

    # Kurtosis
    kurtosis = pd.DataFrame(num_attributes.apply(lambda x: x.kurtosis())).T

    # ---------------------- Construção da Tabela de Estatística Descritiva --------------------------------------------

    # Concatenação das Tabela
    tabela_descritiva = pd.concat([minimo, maximo, intervalo, mean, median, desvio, skew, kurtosis]).T.reset_index()
    tabela_descritiva.columns = ['atributos', 'minimo', 'maximo', 'intervalo', 'media',
                                 'mediana', 'desvio_padrao', 'skewness', 'kurtosis']

    # Exibição da tabela descritiva
    return tabela_descritiva


def visualizacao_dados(dataset):
    filter_attibutes = st.multiselect('Selecionar Colunas', dataset.columns)
    filter_regiao = st.multiselect('Filtrar Região', dataset['zipcode'].unique())
    filter_price = st.slider('Preço Máximo', int(dataset['price'].min()),
                             int(dataset['price'].max()),
                             int(dataset['price'].mean()))

    if (filter_regiao != []) & (filter_attibutes != []):
        df = dataset.loc[dataset['zipcode'].isin(filter_regiao), filter_attibutes]
    elif (filter_regiao != []) & (filter_attibutes == []):
        df = dataset.loc[dataset['zipcode'].isin(filter_regiao), :]
    elif (filter_regiao == []) & (filter_attibutes != []):
        df = dataset.loc[:, filter_attibutes]
    else:
        df = dataset.copy()

    df = df[df['price'] <= filter_price]

    return st.dataframe(df)


def visualizacao_dados_metrics(dataset):

    filter_attibutes = st.multiselect('Selecionar Colunas', dataset.columns)

    if filter_attibutes:
        df = dataset.loc[:, filter_attibutes]
    else:
        df = dataset.copy()

    return st.dataframe(df)


def visualizacao_imoveis_venda(dataset):
    df = dataset

    return st.dataframe(df)


# Transformations

# ------------------------------------------   CÓDIGO PRINCIPAL ------------------------------------------------------


st.sidebar.image('house_rocket_logo.png')

# Barra lateral
page = st.sidebar.selectbox("Navegue pelo Projeto", ["Apresentação",
                                                     "Aquisição Imóveis",
                                                     "Desempenho de Negócio - Verão",
                                                     "Desempenho de Negócio - Inverno",
                                                     "Desempenho de Negócio - Outono",
                                                     "Desempenho de Negócio - Primavera",
                                                     "Hipóteses de Negócios"])

st.sidebar.write('Página criada por Jefferson Henrique Candido')

# ----------------------------------------- PÁGINA DE APRESENTAÇÃO ----------------------------------------------------


if page == "Apresentação":

    st.title('House Rocket Company')

    st.write('Olá! Seja-Bem vindo! Aqui você vai encontrar um DashBoard com um resumo de todo um projeto desenvolvido '
             'para a empresa House Rocket. Primeiramente, vamos compreender como é o modelo de negócio da empresa, o '
             'o problema a ser resolvido e, por fim, a tomada de decisão para resolver esse problema e os resultados '
             'financeiros obtidos.')

    st.subheader('Modelo de Negócio')

    st.write("A House Rocket é uma empresa fictícia do ramo imobiliária que a sua atividade principal é a compra de "
             "imóveis abaixo do preço de mercado com condições minimamente decente e, que após reformá-las, revende "
             "esses imóveis com preços compatíveis com o mercado visando a maximização dos lucros. Dessa forma, o "
             "lucro da empresa vem da diferença entre o preço da revenda e compra do imóvel.")

    st.subheader('Problema de Negócio')

    st.write('Com o objetivo de encontrar ótimas opções de negócios, o CEO da House Rocket Company contratou os '
             'serviços de um Cientista de Dados(no caso, nossos serviços) para analisar o portfólio de imóveis que a '
             'sua empresa possui. Assim, há duas questões principais para responder.')

    st.write('1.) Quais imóveis a House Rocket Company devem comprar e por qual preço?')
    st.write('2.) Uma vez adquiridos esses imóveis, por qual preço devemos revendê-los?')

    st.subheader('Tomada de Decisão para Resolução do Problema')

    st.write('Para resolver esse problema de negócio, foi tomada a seguinte decisão. Para aquisição de imóveis temos o '
             'seguinte critério: \n'
             'Se o preço do imóvel é menor que o preço mediano de mercado e possue condições minimamente decentes, '
             'então esse imóvel receberá a sugestão de compra. Caso contrário, receberá a sugestão de não compra.')

    st.write('Para a determinação do preço de revenda dos imóveis adquiridos, foi colocado o seguinte critério:'
             'Dada a sazonalidade do ano, se o preço de compra for menor que o preço mediano de mercado, então o '
             'preço de venda será o preço de compra + 30%. Se o preço de compra for maior que o preço mediano de '
             'mercado, então o preço de venda será o preço de compra + 10%.')

    st.subheader('Conclusão')

    st.write('Dada a estratégia de resolução acima, consegui sugerir ótimas opções de compras de imóveis para o CEO '
             'com um ótimo potencial de negócio. Além disso, esse dashboard ficará em posse da equipe de negócio '
             'para que seja consultado facilmente os melhores preços que esses imóveis devam ser vendidos levando em '
             'consideração a região e as estações do ano.')

    st.subheader('Resultados Financeiros')

    st.write('CUSTOS DE AQUISIÇÃO: US$ 4.094.212.008,00')
    st.write('RETORNO ESPERADO DAS VENDAS: US$ 5.276.791.316,98')
    st.write('LUCRO ESTIMADO: US$ 1.182.579.308,98')


# --------------------------------------------- AQUISIÇÃO DE IMÓVEIS E LOCALIZAÇÃO -------------------------------------

elif page == 'Aquisição Imóveis':

    # Carregamento dos Dados
    data = base_de_dados('recomendacao_compras.csv')

    st.subheader('AQUISIÇÃO DE IMÓVEIS E LOCALIZAÇÃO')

    st.write('Logo abaixo, temos a tabela com todos os imóveis que foram sugeridos para compra')

    # Visualização dos Dados
    visualizacao_dados(data)

    st.subheader('MAPA COM LOCALIZAÇÃO DOS IMÓVEIS')

    st.write(f'Logo abaixo, temos a localização dos imóveis no mapa.')

    # Base do Mapa
    portfolio_densidade = folium.Map(location=[data['lat'].mean(), data['long'].mean()], default_zoom_start=30)

    # Marcador
    marker_cluster = MarkerCluster().add_to(portfolio_densidade)

    for name, row in data.iterrows():
        folium.Marker([row['lat'], row['long']],
                      popup='Sold R${} on: {}. Características: {} sqrt, {} bedrooms, {} bathrooms, {} Year Built.'.format(
                          row['price'], row['date'], row, ['sqft_living'], row['bedrooms'], row['bathrooms'],
                          row['yr_built'])).add_to(marker_cluster)

    folium_static(portfolio_densidade)

    st.subheader('Estatística Descritiva')

    st.write("Nessa parte, temos uma tabela com a Estatística Descritiva dos dados, como preço máximo e mínimo, por "
             "exemplo;")

    st.write(f'O custo estimado na compra desse imóveis gira em torno de R$ {data["price"].sum()}.')

    tabela = statistic_descritive(data)

    visualizacao_dados_metrics(tabela)
# ---------------------------------------------- DESEMPENHO DE NEGÓCIO - VERÃO -----------------------------------------

elif page == "Desempenho de Negócio - Verão":

    data_verao = base_de_dados('preco_vendas_verao.csv')

    st.title('Desempenho das Vendas - Verão')

    st.write('Com os imóveis adquiridos, agora vamos analisar o desempenho esperado das vendas sobre cada estação do '
             'ano. Logo abaixo, você pode ver a planilha dos imóveis com a sugestão dos preços de venda nessa época do '
             'ano.')

    visualizacao_dados(data_verao)

    st.subheader('Desempenho e Estatística Descritiva')
    st.write('Faturamento Esperado: R${}'.format(round(data_verao['sell_price_summer'].sum(), 2)))
    st.write('Lucro Esperado: R${}'.format(round(data_verao['sell_price_summer'].sum() - data_verao['price'].sum(), 2)))

    tabela_verao = statistic_descritive(data_verao)

    visualizacao_dados_metrics(tabela_verao)

    st.subheader('MAPA PARA LOCALIZAÇÃO DE IMÓVEIS')

    st.write(f'Logo abaixo, temos a localização dos imóveis no mapa.')

    # Base do Mapa
    portfolio_densidade = folium.Map(location=[data_verao['lat'].mean(), data_verao['long'].mean()],
                                     zoom_start=15)

    # Marcador
    marker_cluster = MarkerCluster().add_to(portfolio_densidade)

    for name, row in data_verao.iterrows():
        folium.Marker([row['lat'], row['long']],
                      popup='Price: R$ {}. Bathrooms: {}. Bedrooms: {}. Year Built: {} Year Renovated :{} '
                            'Zipcode: {}'.format(row['sell_price_summer'],
                                                 row['bathrooms'],
                                                 row['bedrooms'],
                                                 row['yr_built'],
                                                 row['yr_renovated'], row['zipcode'])).add_to(marker_cluster)

    folium_static(portfolio_densidade)


# ---------------------------------------------- DESEMPENHO DE NEGÓCIO - PRIMAVERA -------------------------------------


elif page == "Desempenho de Negócio - Primavera":

    data_primavera = base_de_dados('preco_vendas_primavera.csv')

    st.title('Desempenho das Vendas - Primavera')

    st.write('Com os imóveis adquiridos, agora vamos analisar o desempenho esperado das vendas sobre cada estação do '
             'ano. Logo abaixo, você pode ver a planilha dos imóveis com a sugestão dos preços de venda nessa época do '
             'ano.')

    visualizacao_dados(data_primavera)

    st.subheader('Desempenho e Estatística Descritiva')
    st.write('Faturamento Esperado: R${}'.format(round(data_primavera['sell_price_spring'].sum(), 2)))
    st.write('Lucro Esperado: R${}'.format(
        round(data_primavera['sell_price_spring'].sum() - data_primavera['price'].sum(), 2)))

    tabela_primavera = statistic_descritive(data_primavera)

    visualizacao_dados_metrics(tabela_primavera)

    st.subheader('MAPA PARA LOCALIZAÇÃO DE IMÓVEIS')

    st.write(f'Logo abaixo, temos a localização dos imóveis no mapa.')

    # Base do Mapa
    portfolio_densidade = folium.Map(location=[data_primavera['lat'].mean(), data_primavera['long'].mean()],
                                     default_zoom_start=15)

    # Marcador
    marker_cluster = MarkerCluster().add_to(portfolio_densidade)

    for name, row in data_primavera.iterrows():
        folium.Marker([row['lat'], row['long']],
                      popup='Price: R$ {}. Bathrooms: {}. Bedrooms: {}. Year Built: {} Year Renovated :{} '
                            'Zipcode: {}'.format(row['sell_price_spring'],
                                                 row['bathrooms'],
                                                 row['bedrooms'],
                                                 row['yr_built'],
                                                 row['yr_renovated'], row['zipcode'])).add_to(marker_cluster)

    folium_static(portfolio_densidade)


# ---------------------------------------------- DESEMPENHO DE NEGÓCIO - INVERNO ---------------------------------------

elif page == "Desempenho de Negócio - Inverno":

    data_winter = base_de_dados('preco_vendas_inverno.csv')

    st.title('Desempenho das Vendas - Inverno')

    st.write('Com os imóveis adquiridos, agora vamos analisar o desempenho esperado das vendas sobre cada estação do '
             'ano. Logo abaixo, você pode ver a planilha dos imóveis com a sugestão dos preços de venda nessa época do '
             'ano.')

    visualizacao_dados(data_winter)

    st.subheader('Desempenho e Estatística Descritiva')
    st.write('Faturamento Esperado: R$ {}'.format(round(data_winter['sell_price_winter'].sum(), 2)))
    st.write(
        'Lucro Esperado: R$ {}'.format(round(data_winter['sell_price_winter'].sum() - data_winter['price'].sum(), 2)))

    tabela_winter = statistic_descritive(data_winter)

    visualizacao_dados_metrics(tabela_winter)

    st.subheader('MAPA PARA LOCALIZAÇÃO DE IMÓVEIS')

    st.write(f'Logo abaixo, temos a localização dos imóveis no mapa.')

    # Base do Mapa
    portfolio_densidade = folium.Map(location=[data_winter['lat'].mean(), data_winter['long'].mean()],
                                     default_zoom_start=15)

    # Marcador
    marker_cluster = MarkerCluster().add_to(portfolio_densidade)

    for name, row in data_winter.iterrows():
        folium.Marker([row['lat'], row['long']],
                      popup='Price: R$ {}. Bathrooms: {}. Bedrooms: {}. Year Built: {} Year Renovated :{} '
                            'Zipcode: {}'.format(row['sell_price_winter'],
                                                 row['bathrooms'],
                                                 row['bedrooms'],
                                                 row['yr_built'],
                                                 row['yr_renovated'], row['zipcode'])).add_to(marker_cluster)

    folium_static(portfolio_densidade)

# ---------------------------------------------- DESEMPENHO DE NEGÓCIO - OUTONO ----------------------------------------
elif page == "Desempenho de Negócio - Outono":

    data_outono = base_de_dados('preco_vendas_outono.csv')

    st.title('Desempenho das Vendas - Outono')

    st.write('Com os imóveis adquiridos, agora vamos analisar o desempenho esperado das vendas sobre cada estação do '
             'ano. Logo abaixo, você pode ver a planilha dos imóveis com a sugestão dos preços de venda nessa época do '
             'ano.')

    visualizacao_dados(data_outono)

    st.subheader('Desempenho e Estatística Descritiva')
    st.write('Faturamento Esperado: R$ {}'.format(round(data_outono['sell_price_autmumn'].sum(), 2)))
    st.write(
        'Lucro Esperado: R$ {}'.format(round(data_outono['sell_price_autmumn'].sum() - data_outono['price'].sum(), 2)))

    tabela_outono = statistic_descritive(data_outono)

    visualizacao_dados_metrics(tabela_outono)

    st.subheader('MAPA PARA LOCALIZAÇÃO DE IMÓVEIS')

    st.write(f'Logo abaixo, temos a localização dos imóveis no mapa.')

    # Base do Mapa
    portfolio_densidade = folium.Map(location=[data_outono['lat'].mean(), data_outono['long'].mean()],
                                     default_zoom_start=15)

    # Marcador
    marker_cluster = MarkerCluster().add_to(portfolio_densidade)

    for name, row in data_outono.iterrows():
        folium.Marker([row['lat'], row['long']],
                      popup='Price: R$ {}. Bathrooms: {}. Bedrooms: {}. Year Built: {} Year Renovated :{} '
                            'Zipcode: {}'.format(row['sell_price_autmumn'],
                                                 row['bathrooms'],
                                                 row['bedrooms'],
                                                 row['yr_built'],
                                                 row['yr_renovated'], row['zipcode'])).add_to(marker_cluster)

    folium_static(portfolio_densidade)


# ----------------------------------------------- HIPÓTESES DE NEGÓCIOS ------------------------------------------------

elif page == "Hipóteses de Negócios":

    st.header('Hipóteses de Negócios')

    st.write('Nessa seçaõ vamos responder a 5 hipóteses de negócios que vão permitir que o CEO da empresa e a '
             'sua equipe de negócios tenha uma visão mais ampla do negócio em que estão inseridos e possam tomar '
             'decisões mais estratégicas.')

    st.subheader('HIPÓTESE 1: Imóveis que possuem vista para água, são 30% mais caros, na média.')

    st.write('Essa afirmação é verdadeira. A mediana dos preços é de 450.000,00. Além disso, conseguimos '
             'observar que Imóveis com vista para a água possuem um preço mediano de 1.400.000,00, logo, concluímos '
             'que imóveis com vista para água são, na média, 300% mais caro. Logo, o insight gerado aqui é: Imóveis '
             'com vista para a água são uma ótima opção de investimento.')

    st.write('TRADUÇÃO DE NEGÓCIO: Investir em imóveis com vista para água é um ótima opção.')

    st.image('hipotese_1.png')

    # --------------------------------------------------------------------------------------------------------------

    st.subheader('HIPÓTESE 2: Imóveis com data de construção menor que 1955, são 50% mais baratos, na média.')

    st.write('Em geral essa afirmação é falsa. Em termos de ano de construção, ela possuem a mediana de preço '
             'praticamente iguais. Uma vez que a mediana dos preços é de 450.000,00, imóveis com ano de construção '
             'menor que 1955 possuem uma mediana de preços de R$452.000,00 e imóveis com ano de construção maior que '
             '1955 possuem uma mediana de preços de 450.000,00')

    st.write('TRADUÇAÕ DE NEGÓCIO: Não há diferença, a primeira vista, investir em imóveis com ano de construção acima '
             'de 1955 ou antes de 1955.')

    st.image('hipotese_2.png')

    # -------------------------------------------------------------------------------------------------------------

    st.subheader('HIPÓTESE 3: Imóveis com porão são 50% mais caros na média.')

    st.write('Essa afirmação é falsa. Observe que o preço mediano dos imóveis é 450.000,00, todavia, o preço '
             'mediano dos imóveis sem porão é de 411.500,00 e o preço mediano dos imóveis com porão é de '
             '515.000,00. O interessante é que conseguimos extrair um insight relevante: Imóveis com porão é uma '
             'boa opção de negócio, uma vez que o seu valor é, na média, 100.000,00 mais caro do que imóveis sem '
             'porão.')
    st.write('TRADUÇÃO DE NEGÓCIO: Investir em imóveis que possuem porão é um bom negócio.')

    st.image('hipotese_3.png')

    # -------------------------------------------------------------------------------------------------------------

    st.subheader('HIPÓTESE 4: Imóveis com mais de 2 pisos são em média, 40 % mais caros.')

    st.write('Essa afirmação é falsa. Observe que o preço mediano dos imóveis é 450.000,00, todavia o preço mediano '
             'dos imóveis com mais de dois andares é de 527.600,00 e o preço mediano dos imóveis com menos de dois '
             'andares é de 449.950,00. O interessante é que conseguimos extrair um insight relevante: Imóveis com '
             'mais de dois andares é uma boa opção de negócio, uma vez que o seu valor é, na média, 80.000,00 mais '
             'caro.')

    st.write('Investir em imóveis com mais de 2 pisos é uma boa opção.')

    st.image('hipotese_4.png')

    # --------------------------------------------------------------------------------------------------------------

    st.subheader('HIPÓTESE 5: Imóveis com condições abaixo de 3 são, na média, 40% mais baratos.')

    st.write('Essa afirmação é verdadeira. Observe que o preço mediano dos imóveis é 450.000,00, todavia o preço '
             'mediano dos imóveis com condição abaixo de 3 é de 277.000,00 e o preço mediano dos imóveis com '
             'condição maior ou igual a 3 é de 451.000.0. O interessante é que conseguimos extrair um insight '
             'relevante: Imóveis com condições abaixo de 3 PODEM ser um boa opção de negócio, uma vez que o seu valor '
             'é, na média, 150.000,00 mais barato que a média do preço geral.')

    st.write('Dizemos que os imóveis com condição menor que 3 PODEM ser uma boa opção de negócio, pois '
             'não sabemos o quanto seria necessário para reformar um imóvel nessa condição. Logo, seria '
             'primordial ter informações sobre o quanto seria gasto em média em uma reforma com um imóvel nessas '
             'condições, para saber se no final o retorno financeiro seria bom ou não.')

    st.image('hipotese_5.png')
