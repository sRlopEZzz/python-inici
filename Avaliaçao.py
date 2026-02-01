import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

products = pd.read_csv('products_details.csv', encoding='latin1', usecols=['Product Name','Uniqe_Id', 'Category','Color','Selling Price'], sep=';')
customer = pd.read_csv('customer_details.csv', encoding = "utf-8", sep=';', usecols = ['ID_c','Age','Gender','Location','Frequency of Purchases'])
sales = pd.read_csv("sales.csv" , encoding = 'utf-8', sep=';' , usecols = ['id_p' , 'user_id' ,'Quantity','Review Rating' , 'Payment Method' ,'Shipping Type', 'Time stamp'])

def maior_avaliaçao_por_cidade():

    avaliacao = sales['Review Rating'].drop_duplicates().sort_values().to_string(index=False).ljust(20)

    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                    Ratings das Avaliações :                    ")
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                                                                ")

    print(avaliacao)

    print("                                                                ")
    print(" ============================================================== ")
    print("                                                                ")

    localizacaoes = customer['Location'].drop_duplicates().sort_values().to_string(index=False).ljust(20)

    print(" ============================================================== ")
    print(" ============================================================== ")
    print("             Todas as Cidades Dispóniveis                       ")
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                                                                ")

    print(localizacaoes)
    print("                                                                ")
    print('----------------------------------------------------------------')

    cidade_input = input(' Escolha uma cidade: ')

    if cidade_input in customer['Location'].unique():

        vendas_na_cidade_inputada = sales[sales['user_id'].isin(customer[customer['Location'] == cidade_input]['ID_c'])]

        id_item_maior_avaliacao = vendas_na_cidade_inputada.loc[vendas_na_cidade_inputada['Review Rating'].idxmax()]['id_p']

        nome_produto_maior_avaliacao = products.loc[products['Uniqe_Id'] == id_item_maior_avaliacao]['Product Name'].values[0]

        print("                                                                                          ")
        print(" ======================================================================================== ")
        print(" ======================================================================================== ")
        print("                                                                                          ")
        print(f"O item comprado com a maior avaliação em {cidade_input} é: {nome_produto_maior_avaliacao}")
        print("                                                                                          ")
        print(" ======================================================================================== ")
        print(" ======================================================================================== ")


    else:
        print('Cidade Não Encontrada')
        return


#======================================================================================================================#
#======================================================================================================================#
def menor_avaliaçao_por_cidade():

    avaliacao = sales['Review Rating'].drop_duplicates().sort_values().to_string(index=False).ljust(20)

    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                    Ratings das Avaliações :                    ")
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                                                                ")

    print(avaliacao)

    print("                                                                ")
    print(" ============================================================== ")
    print("                                                                ")

    localizacoes = customer['Location'].drop_duplicates().sort_values().to_string(index=False).ljust(20)

    print(" ============================================================== ")
    print(" ============================================================== ")
    print("             Todas as Cidades Dispóniveis                       ")
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                                                                ")

    print(localizacoes)
    print("                                                                ")
    print('----------------------------------------------------------------')

    cidade_input = input(' Escolha uma cidade: ')

    if cidade_input in customer['Location'].unique():

        vendas_na_cidade_inputada = sales[sales['user_id'].isin(customer[customer['Location'] == cidade_input]['ID_c'])]

        id_item_menor_avaliacao = vendas_na_cidade_inputada.loc[vendas_na_cidade_inputada['Review Rating'].idxmin()]['id_p']

        nome_produto_menor_avaliacao = products.loc[products['Uniqe_Id'] == id_item_menor_avaliacao]['Product Name'].values[0]



        print("                                                                                          ")
        print(" ======================================================================================== ")
        print(" ======================================================================================== ")
        print("                                                                                          ")
        print(f"O item comprado com a menor avaliação em {cidade_input} é: {nome_produto_menor_avaliacao}")
        print("                                                                                          ")
        print(" ======================================================================================== ")
        print(" ======================================================================================== ")


    else:
        print('Cidade Não Encontrada')
        return


#======================================================================================================================#
#======================================================================================================================#
def relacao_prazo_entrega_revisao():

    # Limpar e converter os dados para tipos numéricos, se necessário
    sales['Time stamp'] = pd.to_datetime(sales['Time stamp'], format='%d/%m/%Y')  # Converte para tipo datetime
    sales['Review Rating'] = pd.to_numeric(sales['Review Rating'], errors='coerce')

    # Criar o gráfico de dispersão
    plt.figure(figsize=(10, 6))

    # Adicionar os dados ao gráfico de dispersão
    plt.scatter(sales['Time stamp'], sales['Review Rating'], alpha=0.5, color='blue')

    # Adicionar rótulos e título
    plt.xlabel('Data da Compra')
    plt.ylabel('Avaliação')
    plt.title('Relação entre Data da Compra e Avaliação')

    plt.tight_layout()
    plt.show()


#======================================================================================================================#
#======================================================================================================================#
def top_5_avaliacao_por_categoria():
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                  Categorias Existentes                         ")
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                                                                ")

    print(products['Category'].drop_duplicates().sort_values().to_string(index=False).ljust(20))

    print("                                                                ")
    print(" ---------------------------------------------------------------")

    categoria = input('Introduza a categoria pretendida: ')
    print("                                                                ")

    produtos_filtrados = products[products['Category'] == categoria]

    if produtos_filtrados.empty:
        print("Não foram encontrados produtos para a categoria especificada.")

    vendas_com_produtos_filtrados = sales.merge(produtos_filtrados, left_on='id_p', right_on='Uniqe_Id')

    if vendas_com_produtos_filtrados.empty:
        print("Não foram encontradas vendas para a categoria especificada.")


    top_produtos = vendas_com_produtos_filtrados.sort_values(by='Review Rating', ascending=False).head(5)

    # Selecionar colunas relevantes
    top_produtos = top_produtos[['Product Name', 'Review Rating']]

    print(f"Top 5 produtos na categoria '{categoria}' por classificação de comentários:")
    print(top_produtos.to_string(index=False))


#======================================================================================================================#
#======================================================================================================================#
def clientes_insatisfeitos_por_localizacao_e_produto():

    fasquia = 3

    vendas_com_avaliacoes = sales.merge(products, left_on='id_p', right_on='Uniqe_Id')

    vendas_com_avaliacoes = vendas_com_avaliacoes.merge(customer, left_on='user_id', right_on='ID_c')

    avaliacoes_por_cliente_localizacao_produto = vendas_com_avaliacoes.groupby(['user_id', 'Location', 'Product Name'])['Review Rating'].mean().reset_index()

    clientes_insatisfeitos = avaliacoes_por_cliente_localizacao_produto[avaliacoes_por_cliente_localizacao_produto['Review Rating'] < fasquia]

    clientes_insatisfeitos = clientes_insatisfeitos.sort_values(by='Review Rating').head(10)

    print(" ============================================================== ")
    print(" ============================================================== ")
    print(" Top 10 clientes insatisfeitos por localização e produto:       ")
    print(" ============================================================== ")
    print(" ============================================================== ")

    print(clientes_insatisfeitos[['user_id', 'Location', 'Product Name', 'Review Rating']].to_string(index=False))
    print(" ============================================================== ")
    print(" ============================================================== ")


#======================================================================================================================#
#======================================================================================================================#
def satisfacao_por_data():

    mes_input = input('Introduza o número do Mês [MM]: ')
    ano_input = input('Introduza o ano [AAAA]: ')

    data_input = pd.to_datetime(f'01/{mes_input}/{ano_input}', format='%d/%m/%Y')

    vendas_na_data = sales[pd.to_datetime(sales['Time stamp'], format='%d/%m/%Y').dt.to_period('M') == data_input.to_period('M')]

    vendas_com_produtos = vendas_na_data.merge(products, left_on='id_p', right_on='Uniqe_Id')

    media_avaliacoes_por_produto = vendas_com_produtos.groupby('Product Name')['Review Rating'].mean().reset_index()

    produtos_mais_satisfeitos = media_avaliacoes_por_produto.sort_values(by='Review Rating', ascending=False)


    print("Produtos com maior satisfação na data especificada:")

    print(produtos_mais_satisfeitos.head(10).to_string(index=False))


#======================================================================================================================#
#======================================================================================================================#
