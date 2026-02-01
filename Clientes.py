import pandas as pd
import matplotlib.pyplot as plt

customer = pd.read_csv('customer_details.csv', encoding = "utf-8", sep=';', usecols = ['ID_c','Age','Gender','Location'])

def mostrar_inf_clientes():

    c_femininos = customer[customer['Gender'] == 'Female'].shape[0]
    c_masculinos = customer[customer['Gender'] == 'Male'].shape[0]
    c_nao_especificado = customer[(customer['Gender'] != 'Female') & (customer['Gender'] != 'Male')].shape[0]

    total_customer = int(c_femininos) + int(c_masculinos)

    percentagem_masculinos = (c_masculinos / total_customer) * 100
    percentagem_femininos = (c_femininos / total_customer) * 100


    print("                                                                             ")
    print("                                                                             ")
    print(" ================= NÚMERO TOTAL DE CLIENTES:", total_customer, "============")
    print("                                                                             ")
    print(" ================= FEMININOS:",c_femininos, "===========================")
    print("                                                                             ")
    print(" ================= MASCULINOS:",c_masculinos, "==========================")
    print("                                                                             ")
    print(" ================= NÃO ESPECÍFICADOS:",c_nao_especificado, "======================")
    print("                                                                             ")
    print("                                                                             ")

    s_n = input('Pretende ver o Grafico ?? [s/n]: ')

    if s_n == 's':
        # Criando um gráfico de pizza
        labels = ['Masculino', 'Feminino']
        sizes = [percentagem_masculinos, percentagem_femininos]
        colors = ['blue', 'pink']
        explode = (0.1, 0)  # destaca o primeiro pedaço (masculino)

        plt.figure(figsize=(8, 6))
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',shadow=True, startangle=140)
        plt.title('Distribuição de Clientes por Sexo')
        plt.axis('equal')  # garante que o gráfico de pizza seja desenhado como um círculo
        plt.show()
    elif s_n == 'n':
        print('Saindo....')


#======================================================================================================================#
#======================================================================================================================#
def distribuicao_idade():

    f_etarias = [0, 20, 65, float('inf')]

    tipos_f_etarias = ['Jovens', 'Adultos', 'Idosos']

    customer['Faixa Etária'] = pd.cut(customer['Age'], bins=f_etarias, labels=tipos_f_etarias, right=False)

    contagem_faixas_etarias = customer['Faixa Etária'].value_counts()


    mostrar_inf_clientes.total_customer = len(customer)

    percentagem_jovens = (contagem_faixas_etarias ['Jovens'] / len(customer)) * 100
    percentagem_adultos = (contagem_faixas_etarias['Adultos'] / len(customer)) * 100
    percentagem_idosos = (contagem_faixas_etarias['Idosos'] / len(customer)) * 100

    categorias = ['Jovens', 'Adultos', 'Idosos']
    percentagens = [percentagem_jovens, percentagem_adultos, percentagem_idosos]

    cores = ['lightblue', 'lightgreen', 'lightcoral']

    plt.figure(figsize=(8, 6))
    plt.pie(percentagens, labels=categorias, colors=cores, autopct='%1.1f%%', startangle=140)
    plt.title('Distribuição de Clientes por Faixa Etária')
    plt.axis('equal')
    plt.show()


#======================================================================================================================#
#======================================================================================================================#
def distribuicao_localidade():

    contagem_localidades = customer['Location'].value_counts()

    mostrar_inf_clientes.total_customer = len(customer)

    distribuicao_percentual = (contagem_localidades / len(customer)) * 100

    print(" ============================================================== ")
    print(" ============================================================== ")
    print("             Distribuição percentual das localidades:           ")
    print(" ============================================================== ")
    print(" ============================================================== ")
    print("                                                                ")
    print("                                                                ")

    print("{:<20} {:<10}".format("LOCALIDADE", "PERCENTAGEM"))

    print("---------------------------------------------------------------")

    for localidade, percentual in distribuicao_percentual.items():

        print("{:<20} {:<0.2f}%".format(localidade, percentual))

    print("                                                                ")
    print(" ============================================================== ")
    print(" ============================================================== ")


#======================================================================================================================#
#======================================================================================================================#