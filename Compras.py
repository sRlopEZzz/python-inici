import pandas as pd
import matplotlib.pyplot as plt

products = pd.read_csv('products_details.csv', encoding='latin1',  sep=';')
customer = pd.read_csv('customer_details.csv', encoding = "utf-8", sep=';')
sales = pd.read_csv("sales.csv" , encoding = 'utf-8', sep=';')


import pandas as pd

def dia_e_mes_mais_compras_por_cor():
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                  Categorias Existentes                         ")
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                                                                ")

    print(products['Category'].drop_duplicates().sort_values().to_string(index=False).ljust(20))

    print("                                                                ")
    print(" ---------------------------------------------------------------")
    print("                                                                ")
    print("                                                                ")

    categoria_input = input("Escolha uma Categoria: ")

    cor_input = input("Introduza uma cor Pretendida: ")


    produtos_filtrados = products[(products['Category'] == categoria_input) & (products['Color'] == cor_input)]

    if produtos_filtrados.empty:
        print("Não foram encontradas compras para a categoria e cor especificadas.")

    # Mesclar produtos filtrados com vendas
    vendas_com_produtos_filtrados = sales[sales['id_p'].isin(produtos_filtrados['Uniqe_Id'])]

    if vendas_com_produtos_filtrados.empty:
        print("Não foram encontradas vendas para a categoria e cor especificadas.")

    #  cópia explícita para evitar SettingWithCopyWarning
    vendas_com_produtos_filtrados = vendas_com_produtos_filtrados.copy()

    vendas_com_produtos_filtrados['Time stamp'] = pd.to_datetime(vendas_com_produtos_filtrados['Time stamp'], dayfirst=True)

    #.loc para evitar SettingWithCopyWarning
    vendas_com_produtos_filtrados.loc[:, 'Dia da Semana'] = vendas_com_produtos_filtrados['Time stamp'].dt.day_name()
    vendas_com_produtos_filtrados.loc[:, 'Mês'] = vendas_com_produtos_filtrados['Time stamp'].dt.month_name()

    contagem_dia_semana = vendas_com_produtos_filtrados['Dia da Semana'].value_counts()
    contagem_mes = vendas_com_produtos_filtrados['Mês'].value_counts()

    dia_semana_mais_compras = contagem_dia_semana.idxmax()
    mes_mais_compras = contagem_mes.idxmax()

    print(f"O dia da semana com mais compras na categoria {categoria_input}, na cor {cor_input} é {dia_semana_mais_compras} e o mês com mais compras é {mes_mais_compras}.")


#======================================================================================================================#
#======================================================================================================================#
def valor_compras_por_local_e_dia():

    vendas_com_produtos = sales.merge(products, left_on='id_p', right_on='Uniqe_Id')

    vendas_com_produtos_e_clientes = vendas_com_produtos.merge(customer, left_on='user_id', right_on='ID_c')

    # Converter o timestamp para datetime especificando o formato correto
    vendas_com_produtos_e_clientes['Time stamp'] = pd.to_datetime(vendas_com_produtos_e_clientes['Time stamp'],dayfirst=True)

    # Extrair dia da semana
    vendas_com_produtos_e_clientes['Dia da Semana'] = vendas_com_produtos_e_clientes['Time stamp'].dt.day_name()

    # Calcular valor total da compra
    vendas_com_produtos_e_clientes['Valor Compra'] = vendas_com_produtos_e_clientes['Selling Price'].replace(r'[^\d,.-]', '', regex=True).str.replace(',', '.').astype(float) * vendas_com_produtos_e_clientes['Quantity']

    # Agrupar por local e dia da semana e somar os valores das compras
    valor_compras = vendas_com_produtos_e_clientes.groupby(['Location', 'Dia da Semana'])['Valor Compra'].sum().reset_index()

    # Ordenar por local e dia da semana
    valor_compras = valor_compras.sort_values(by=['Location', 'Dia da Semana'])

    print(valor_compras.to_string(index=False).ljust(20))


#======================================================================================================================#
#======================================================================================================================#
def dia_e_mes_mais_compra_de_uma_categoria():

    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                  Categorias Existentes                         ")
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                                                                ")

    print(products['Category'].drop_duplicates().sort_values().to_string(index=False).ljust(20))

    print("                                                                ")
    print(" ---------------------------------------------------------------")

    categoria_input = input('Introduza a Categoria: ')

    mes_input = input('Introduza o número do Mês [MM]: ')

    ano_input = input('Introduza o ano [AAAA]: ')

    data_input = pd.to_datetime(f'01/{mes_input}/{ano_input}', format='%d/%m/%Y')

    vendas_na_data = sales[(pd.to_datetime(sales['Time stamp'], format='%d/%m/%Y').dt.month == data_input.month) & (pd.to_datetime(sales['Time stamp'], format='%d/%m/%Y').dt.year == data_input.year)]

    vendas_com_categoria = vendas_na_data.merge(products, left_on='id_p', right_on='Uniqe_Id')

    vendas_categoria_especificada = vendas_com_categoria[vendas_com_categoria['Category'] == categoria_input].copy()

    vendas_categoria_especificada['Dia da Semana'] = pd.to_datetime(vendas_categoria_especificada['Time stamp'], format='%d/%m/%Y').dt.day_name()

    compras_por_dia_semana = vendas_categoria_especificada.groupby('Dia da Semana').size()

    dia_mais_compras = compras_por_dia_semana.idxmax()

    print(f"O dia da semana com mais compras na categoria '{categoria_input}' no mês de {data_input.strftime('%B')} de {ano_input} foi {dia_mais_compras}.")


#======================================================================================================================#
#======================================================================================================================#