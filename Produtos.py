import pandas as pd
import matplotlib.pyplot as plt


products = pd.read_csv('products_details.csv', encoding='latin1', usecols=['Product Name','Uniqe_Id', 'Category','Color','Selling Price'], sep=';')
customer = pd.read_csv('customer_details.csv', encoding = "utf-8", sep=';', usecols = ['ID_c','Age','Gender','Location'])
sales = pd.read_csv("sales.csv" , encoding = 'utf-8', sep=';' , usecols = ['id_p' , 'user_id' ,'Quantity','Review Rating' , 'Payment Method' ,'Shipping Type'])


#======================================================================================================================#
#======================================================================================================================#
def prod_menos_vendidos_por_regiao():

    print(" ============================================================== ")
    print(" ============================================================== ")
    print("             Todas as Cidades Dispóniveis                       ")
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                                                                ")

    print(customer['Location'].drop_duplicates().sort_values().to_string(index=False).ljust(20))

    print("                                                                ")
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                                                                ")
    print("                                                                ")

    dados_merged = pd.merge(pd.merge(sales, customer, left_on='user_id', right_on='ID_c'), products, left_on='id_p', right_on='Uniqe_Id')

    cidade = input("ESCOLHA UMA CIDADE: ")

    vendas_por_cidades = dados_merged[dados_merged['Location'] == cidade]



    if vendas_por_cidades.empty:

        print(f"Não há vendas registradas para a cidade de {cidade}.")

    else:
        vendas_por_genero = vendas_por_cidades.groupby(['Gender', 'Category', 'Product Name']).agg({'Quantity': 'sum'}).reset_index()

        min_vendas = vendas_por_genero.loc[vendas_por_genero.groupby('Gender')['Quantity'].idxmin()]

        print(" ============================================================== ")
        print(f"  Produto com menor venda na cidade de {cidade} por gênero:    ")
        print(" ============================================================== ")
        print("                                                                ")

        for index, row in min_vendas.iterrows():


            print(f"   Gênero: {row['Gender']}")
            print("                                       ")
            print(f"   Nome do Produto: {row['Product Name']}")
            print("                                       ")
            print(f"   Categoria: {row['Category']}")
            print("                                       ")
            print(f"   Total de vendas: {row['Quantity']}")
            print("                                       ")
            print(" ---------------------------------------------------------- ")


#======================================================================================================================#
#======================================================================================================================#
def prod_mais_vendidos_por_regiao():
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("             Todas as Cidades Dispóniveis                       ")
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                                                                ")

    print(customer['Location'].drop_duplicates().sort_values().to_string(index=False).ljust(20))

    print("                                                                ")
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                                                                ")
    print("                                                                ")

    dados_merged = pd.merge(pd.merge(sales, customer, left_on='user_id', right_on='ID_c'), products, left_on='id_p', right_on='Uniqe_Id')

    cidade = input("ESCOLHA UMA CIDADE: ")

    vendas_por_cidades = dados_merged[dados_merged['Location'] == cidade]

    if vendas_por_cidades.empty:
        print(f"Não há vendas registradas para a cidade de {cidade}.")
    else:
        vendas_por_genero = vendas_por_cidades.groupby(['Gender', 'Category', 'Product Name']).agg({'Quantity': 'sum'}).reset_index()

        max_vendas = vendas_por_genero.loc[vendas_por_genero.groupby('Gender')['Quantity'].idxmax()]

        print(" ============================================================== ")
        print(f"  Produto com mais vendas na cidade de {cidade} por gênero:    ")
        print(" ============================================================== ")
        print("                                                                ")

        for index, row in max_vendas.iterrows():
            print(f"   Gênero: {row['Gender']}")
            print("                                       ")
            print(f"   Nome do Produto: {row['Product Name']}")
            print("                                       ")
            print(f"   Categoria: {row['Category']}")
            print("                                       ")
            print(f"   Total de vendas: {row['Quantity']}")
            print("                                       ")
            print(" ---------------------------------------------------------- ")


#======================================================================================================================#
#======================================================================================================================#
def top5_prod_de_uma_categoria_por_cor():
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                  Categorias Existentes                         ")
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                                                                ")

    print(products['Category'].drop_duplicates().sort_values().to_string(index=False).ljust(20))

    print("                                                                ")
    print(" ---------------------------------------------------------------")

    categoria = input('Introduza a categoria Pretendida: ')
    print("                                                                ")


    print(products['Color'].drop_duplicates().sort_values().to_string(index=False).ljust(20))

    print("                                                                ")
    print(" ---------------------------------------------------------------")

    cor = input('Introduza a Cor Pretendida: ')

    produtos_por_cor = products[(products['Category'] == categoria) & (products['Color'] == cor)]

    if produtos_por_cor.empty:
        print("Não há produtos disponíveis nessa cor.")
    else:
        top_5_produtos = produtos_por_cor[['Product Name', 'Color']].head(5)

        print(top_5_produtos)


#======================================================================================================================#
#======================================================================================================================#
def total_vendas_por_categorias():
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                  Categorias Existentes                         ")
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                                                                ")

    print(products['Category'].drop_duplicates().sort_values().to_string(index=False).ljust(20))

    print("                                                                ")
    print(" ---------------------------------------------------------------")

    categoria = input('Introduza a categoria Pretendida: ')

    if categoria in products['Category'].unique():

        print("-----------------------------------------------------------")
        print(f"Categoria selecionada: {categoria} ")
        print("-----------------------------------------------------------")

        vendas_categoria = sales[sales['id_p'].isin( products[products['Category']== categoria]['Uniqe_Id'])]

        quant_total_vendas_categoria = vendas_categoria['Quantity'].sum()
        quant_total_faturada_categoria = products['Selling Price'].replace(r'[^\d,.-]', '', regex=True).str.replace(',', '.').astype(float).sum()

        quant_total_vendas_geral = sales['Quantity'].sum()

        print(f"Total de Nº de vendas da categoria '{categoria}': {quant_total_vendas_categoria}")
        print("                                                                             ")
        print(f"Valor faturado em vendas na categoria '{categoria}': {quant_total_faturada_categoria:.2f}")
        print("                                                                             ")

    else:
        print('Categoria Não Encontrada')
        return

    s_n = input('Pretende ver o Grafico ?? [s/n]: ')

    if s_n == 's':

        labels = ['Nº de Vendas da ' + categoria, 'Outras Vendas']
        sizes = [quant_total_vendas_categoria, quant_total_vendas_geral - quant_total_vendas_categoria]
        explode = (0.1, 0)

        plt.figure(figsize=(12, 8))
        plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.title(f"Relação do Nº de Vendas da categoria '{categoria}' com o total de Nº Vendas")
        plt.show()

    elif s_n == 'n':
        print('Saindo....')


#======================================================================================================================#
#======================================================================================================================#
def tamanho_com_mais_lucro():


    vendas_por_preco = pd.merge(sales, products, left_on='id_p', right_on='Uniqe_Id', how='inner')


    vendas_por_preco['valor_obitido'] = vendas_por_preco['Quantity'] * vendas_por_preco['Selling Price']


    vendas_por_preco['tamanho'] = vendas_por_preco['Product Name'].str.extract(r'\b([S M L XL]+)\b')


    valor_obtido_de_size = vendas_por_preco.groupby('tamanho')['valor_obitido'].sum()


    tamanho_mais_lucrativo = valor_obtido_de_size.idxmax()

    print("                                                                       ")
    print("====================================================================== ")
    print("====================================================================== ")
    print(f' O tamanho que gerou mais lucro foi: {tamanho_mais_lucrativo} ')
    print("====================================================================== ")
    print("====================================================================== ")
    print("                                                                       ")


#======================================================================================================================#
#======================================================================================================================#