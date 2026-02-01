import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


products = pd.read_csv('products_details.csv', encoding='latin1', usecols=['Product Name','Uniqe_Id', 'Category','Color','Selling Price'], sep=';')
customer = pd.read_csv('customer_details.csv', encoding = "utf-8", sep=';', usecols = ['ID_c','Age','Gender','Location'])
sales = pd.read_csv("sales.csv" , encoding = 'utf-8', sep=';' , usecols = ['id_p' , 'user_id' ,'Quantity','Review Rating' , 'Payment Method' ,'Shipping Type' , 'Size' ])

def distribuicao_produtos_preco_venda():
    # remover os caracteres não numéricos em selling price
    products['Selling Price'] = products['Selling Price'].str.replace('[^0-9.]', '', regex=True)

    # Convert 'Selling Price' column to numeric type
    products['Selling Price'] = pd.to_numeric(products['Selling Price'])

    # Now you can perform your groupby operation
    category_price_summary = products.groupby('Category')['Selling Price'].mean().reset_index()

    # Plotar o gráfico de linha

    category_price_summary.plot(x='Category', y='Selling Price', kind='line', marker='o', color='b')
    plt.title('Preço Médio de Venda por Categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Preço Médio de Venda')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


#======================================================================================================================#
#======================================================================================================================#
def venda_por_tamanho_e_cor():
    print("==============================================================")
    print("==============================================================")
    print("                     Tamanhos Disponíveis                     ")
    print("==============================================================")
    print("==============================================================")
    print("                                                              ")

    tamanhos = sales['Size'].drop_duplicates().dropna().sort_values().to_string(index=False).ljust(20)

    num_produtos_sem_size_especificados = sales['Size'].isna().sum()

    print(tamanhos)
    print("                                                             ")
    print("-------------------------------------------------------------")
    print("                                                             ")
    print(f'Existem {num_produtos_sem_size_especificados} produtos sem tamanhos especificados.')
    print("-------------------------------------------------------------")
    print("                                                              ")

    t_Grandes = sales[sales['Size'] == 'L'].shape[0]

    t_medios = sales[sales['Size'] == 'M'].shape[0]

    t_pequenos = sales[sales['Size'] == 'S'].shape[0]

    t_extra_grande = sales[sales['Size'] == 'XL'].shape[0]

    print("==============================================================")
    print("==============================================================")
    print("                                                              ")
    print(f'Total de vendas de produtos tamanho L: {t_Grandes}')
    print(f'Total de vendas de produtos tamanho M: {t_medios}')
    print(f'Total de vendas de produtos tamanho S: {t_pequenos}')
    print(f'Total de vendas de produtos tamanho XL: {t_extra_grande}')
    print("                                                              ")
    print("==============================================================")
    print("==============================================================")

    s_n = input('Pretende ver o Grafico ?? [s/n]: ')

    if s_n == 's':

        total_vendas = len(sales)

        percentuais = [
                        t_Grandes / total_vendas * 100,
                        t_medios / total_vendas * 100,
                        t_pequenos / total_vendas * 100,
                        t_extra_grande / total_vendas * 100,
                        num_produtos_sem_size_especificados / total_vendas * 100
                      ]

        labels = ['Grande (L)', 'Médio (M)', 'Pequeno (S)', 'Extra Grande (XL)', 'Não Especificado']


        plt.figure(figsize=(8, 6))
        plt.pie(percentuais, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Percentagem de vendas por tamanho')
        plt.axis('equal')
        plt.show()

    elif s_n == 'n':
        print('OK....')
        print("      ")

    print("============================================================================")
    print("============================================================================")
    print("                                                                            ")
    print(' Agora Vamos vamos verificar os tamanhos mais vendidos por uma cor especíca.')
    print("                                                                            ")
    print("============================================================================")
    print("============================================================================")
    print("                                                                            ")
    print("                                                                            ")

    cor_input = input('Escolha uma Cor: ')

    produtos_filtrados_por_cor = products[(products['Color'] == cor_input)]

    vendas_por_tamanho = sales.merge(produtos_filtrados_por_cor, left_on='id_p', right_on='Uniqe_Id')

    vendas_por_tamanho = vendas_por_tamanho.groupby('Size')['Quantity'].sum()

    tamanho_mais_vendido = vendas_por_tamanho.idxmax()

    print("============================================================================")
    print("============================================================================")
    print("                                                                            ")
    print(f"O tamanho mais vendido para a cor '{cor_input}' é: {tamanho_mais_vendido}")
    print("                                                                            ")
    print("============================================================================")
    print("============================================================================")


#======================================================================================================================#
#======================================================================================================================#
def relacao_preco_venda_forma_pagamento():

    products.rename(columns={'Uniqe_Id': 'id_p'}, inplace=True)

    # Limpar e converter a coluna 'Selling Price' para numérico
    products['Selling Price'] = products['Selling Price'].replace(r'[^\d,.-]', '', regex=True).str.replace(',','.').astype(float)

    # Combinar dataframes
    merged_df = pd.merge(sales, products, on='id_p')

    plt.figure(figsize=(12, 8))
    sns.boxplot(x='Payment Method', y='Selling Price', data=merged_df)

    plt.title('Distribuição do Preço de Venda por Forma de Pagamento')
    plt.xlabel('Forma de Pagamento')
    plt.ylabel('Preço de Venda')
    plt.xticks(rotation=45)
    plt.show()


#======================================================================================================================#
#======================================================================================================================#