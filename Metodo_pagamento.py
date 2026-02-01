import pandas as pd
import matplotlib.pyplot as plt

products = pd.read_csv('products_details.csv', encoding='latin1', usecols=['Product Name','Uniqe_Id', 'Category','Color','Selling Price'], sep=';')
customer = pd.read_csv('customer_details.csv', encoding = "utf-8", sep=';', usecols = ['ID_c','Age','Gender','Location','Frequency of Purchases'])
sales = pd.read_csv("sales.csv" , encoding = 'utf-8', sep=';' , usecols = ['id_p' , 'user_id' ,'Quantity','Review Rating' , 'Payment Method' ,'Shipping Type'])

def tipos_metodo_pagamento():

    tipos_metodo_pagamento = sales['Payment Method'].drop_duplicates().sort_values().to_string(index=False).ljust(20)

    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                Métodos de Pagamento Existentes                 ")
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                                                                ")


    print(tipos_metodo_pagamento)

    print("                                                                ")
    print(" ---------------------------------------------------------------")


#======================================================================================================================#
#======================================================================================================================#
def metodo_pagamento_por_distribuicao():


    pagamento_counts = sales['Payment Method'].value_counts()


    fig, ax = plt.subplots()
    ax.pie(pagamento_counts, labels=pagamento_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    ax.set_title('Distribuição de Métodos de Pagamento')

    plt.show()


#======================================================================================================================#
#======================================================================================================================#
def metodo_pagamento_com_mais_lucro():

        vendas_por_preco = pd.merge(sales, products, left_on='id_p', right_on='Uniqe_Id', how='inner')

        vendas_por_preco['valor_obitido'] = vendas_por_preco['Quantity'] * vendas_por_preco['Selling Price']

        valor_obtido_de_payment_method = vendas_por_preco.groupby('Payment Method')['valor_obitido'].sum()

        forma_mais_lucrativa = valor_obtido_de_payment_method.idxmax()

        print("                                                                       ")
        print("====================================================================== ")
        print("====================================================================== ")
        print(f' A forma de pagamento que gerou mais lucro foi: {forma_mais_lucrativa}')
        print("====================================================================== ")
        print("====================================================================== ")
        print("                                                                       ")


#======================================================================================================================#
#======================================================================================================================#
def metodo_pagamento_por_sexo():


    vendas_com_genero = pd.merge(sales, customer, left_on='user_id', right_on='ID_c', how='inner')


    pagamento_por_sexo = vendas_com_genero.groupby(['Gender', 'Payment Method']).size().reset_index(name='Count')


    pagamento_mais_comum_por_sexo = pagamento_por_sexo.loc[pagamento_por_sexo.groupby('Gender')['Count'].idxmax()]

    print("                                                                       ")
    print("====================================================================== ")
    print("====================================================================== ")
    print("                                                                       ")
    print("Forma de pagamento mais comum para cada sexo:")
    print("                                                                       ")
    print(pagamento_mais_comum_por_sexo)
    print("                                                                       ")
    print("====================================================================== ")
    print("====================================================================== ")


#======================================================================================================================#
#======================================================================================================================#
