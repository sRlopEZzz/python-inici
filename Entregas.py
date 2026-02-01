import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


products = pd.read_csv('products_details.csv', encoding='latin1', usecols=['Product Name','Uniqe_Id', 'Category','Color','Selling Price'], sep=';')
customer = pd.read_csv('customer_details.csv', encoding = "utf-8", sep=';', usecols = ['ID_c','Age','Gender','Location','Frequency of Purchases'])
sales = pd.read_csv("sales.csv" , encoding = 'utf-8', sep=';' , usecols = ['id_p' , 'user_id' ,'Quantity','Review Rating' , 'Payment Method' ,'Shipping Type', 'Time stamp'])


def tipos_entrega():
    print("                                                                ")
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("               Tipos de entregas existentes                     ")
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                                                                ")

    print(sales['Shipping Type'].drop_duplicates().sort_values().to_string(index=False).ljust(20))

    print("                                                                ")
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                                                                ")

#======================================================================================================================#
#======================================================================================================================#
def relacao_tipo_envio_localizacao():
    # Mesclar os dataframes sales e customer com base na coluna 'user_id' e 'ID_c'
    dados_merge = pd.merge(sales, customer, left_on='user_id', right_on='ID_c', how='inner')

    # Calcular a frequência de cada tipo de envio por localização
    frequencia_tipo_envio_localizacao = dados_merge.groupby(['Location', 'Shipping Type']).size().unstack(fill_value=0)

    # Identificar o tipo de envio mais frequente para cada localização
    tipo_envio_mais_frequente = frequencia_tipo_envio_localizacao.idxmax(axis=1)
    frequencia_maxima = frequencia_tipo_envio_localizacao.max(axis=1)

    # Criar um dataframe para visualização
    tipo_envio_frequente_df = pd.DataFrame({'Localização': tipo_envio_mais_frequente.index,'Tipo de Envio Mais Frequente': tipo_envio_mais_frequente.values,'Frequência': frequencia_maxima.values})

    plt.figure(figsize=(18, 8))
    sns.barplot(data=tipo_envio_frequente_df, x='Localização', y='Frequência', hue='Tipo de Envio Mais Frequente', dodge=False)

    plt.title('Tipo de Envio Mais Frequente por Localização')
    plt.xlabel('Localização')
    plt.ylabel('Frequência')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


#======================================================================================================================#
#======================================================================================================================#