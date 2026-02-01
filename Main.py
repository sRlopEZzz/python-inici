import Avaliaçao
import Clientes
import Entregas
import Metodo_pagamento
import Produtos
import Compras
import Vendas


def layout_inicial():
    print("                                                                                                                                                              ")
    print("                                                                                                                                                              ")
    print("==============================================================================================================================================================")
    print("==============================================================================================================================================================")
    print("                                             Programa de Apoio a Decisão e Gestão                                                                             ")
    print("==============================================================================================================================================================")
    print("==============================================================================================================================================================")
    print("                                                                                                                                                              ")
    print("                                                                                                                                                              ")


def menu_principal():
    print("                                                                ")
    print(" ============================================================== ")
    print(" ||||                    MENU PRINCIPAL                    |||| ")
    print(" ============================================================== ")
    print(" ||||                                                      |||| ")
    print(" ||||               1 - Informação dos Clientes            |||| ")
    print(" ||||                                                      |||| ")
    print(" ||||               2 - Informação das Vendas              |||| ")
    print(" ||||                                                      |||| ")
    print(" ||||               3 - Informação dos Produtos            |||| ")
    print(" ||||                                                      |||| ")
    print(" ||||               4 - Avaliações                         |||| ")
    print(" ||||                                                      |||| ")
    print(" ||||               5 - Médotos de Pagamento               |||| ")
    print(" ||||                                                      |||| ")
    print(" ||||               6 - Médoto Envio                       |||| ")
    print(" ||||                                                      |||| ")
    print(" ||||               7 - Sair                               |||| ")
    print(" ||||                                                      |||| ")
    print(" ============================================================== ")
    print(" ============================================================== ")


# ======================================================================================================================#
# ======================================================================================================================#
def menu_clientes():
    print("                                                                ")
    print(" ============================================================== ")
    print(" ||||                    MENU CLIENTES - ( 1 )             |||| ")
    print(" ============================================================== ")
    print(" ||||                                                      |||| ")
    print(" ||||               1 - Total de Clientes                  |||| ")
    print(" ||||                                                      |||| ")
    print(" ||||               2 - Distribuição por Idade             |||| ")
    print(" ||||                                                      |||| ")
    print(" ||||               3 - Distribuição por Localidade        |||| ")
    print(" ||||                                                      |||| ")
    print(" ||||               4 - Voltar                             |||| ")
    print(" ||||                                                      |||| ")
    print(" ============================================================== ")
    print(" ============================================================== ")


#======================================================================================================================#
#======================================================================================================================#
def menu_vendas():
    print("                                                                    ")
    print(" ================================================================== ")
    print(" ||||                     MENU VENDAS - ( 2 )                  |||| ")
    print(" ================================================================== ")
    print(" ||||                                                          |||| ")
    print(" ||||       1 - Produto mais vendido por Região                |||| ")
    print(" ||||                                                          |||| ")
    print(" ||||       2 - Produto menos vendido por Região               |||| ")
    print(" ||||                                                          |||| ")
    print(" ||||       3 - Total de Vendas por Categorias                 |||| ")
    print(" ||||                                                          |||| ")
    print(" ||||       4 - Datas com mais Vendas numa Cor                 |||| ")
    print(" ||||                                                          |||| ")
    print(" ||||       5 - Distribuição por Preço de Venda                |||| ")
    print(" ||||                                                          |||| ")
    print(" ||||       6 - Vendas Por Local e Data                        |||| ")
    print(" ||||                                                          |||| ")
    print(" ||||       7 - Vendas Por Cor e Tamanho                       |||| ")
    print(" ||||                                                          |||| ")
    print(" ||||       8 - Dia e Mês com Mais compras de uma Categoria    |||| ")
    print(" ||||                                                          |||| ")
    print(" ||||       9 - Voltar                                         |||| ")
    print(" ================================================================== ")
    print(" ================================================================== ")


#======================================================================================================================#
#======================================================================================================================#
def menu_produtos():
    print("                                                                   ")
    print(" ================================================================= ")
    print(" ||||                     MENU PRODUTOS - ( 3 )               |||| ")
    print(" ================================================================= ")
    print(" ||||                                                         |||| ")
    print(" ||||         1 - Top 5 de Categoria por Produto por Cores    |||| ")
    print(" ||||                                                         |||| ")
    print(" ||||         2 - Tamanho que gerou Mais Lucro                |||| ")
    print(" ||||                                                         |||| ")
    print(" ||||         3 - Voltar                                      |||| ")
    print(" ||||                                                         |||| ")
    print(" =====================================================r============ ")
    print(" ================================================================= ")


#======================================================================================================================#
#======================================================================================================================#
def menu_avalicao():
    print("                                                                              ")
    print(" ============================================================================ ")
    print(" ||||                          MENU AVALIAÇÕES - ( 4 )                   |||| ")
    print(" ============================================================================ ")
    print(" ||||                                                                    |||| ")
    print(" ||||     1 - Maior Avaliação Por Cidade                                 |||| ")
    print(" ||||                                                                    |||| ")
    print(" ||||     2 - Menor Avaliação Por Cidade                                 |||| ")
    print(" ||||                                                                    |||| ")
    print(" ||||     3 - Top 5 Avaliações Por Categoria                             |||| ")
    print(" ||||                                                                    |||| ")
    print(" ||||     4 - Top 10 Insatisfações Por localização e Produto             |||| ")
    print(" ||||                                                                    |||| ")
    print(" ||||     5 - Top 10 Produto com maior Satisfação numa data Específica   |||| ")
    print(" ||||                                                                    |||| ")
    print(" ||||     6 - Voltar                                                     |||| ")
    print(" ||||                                                                    |||| ")
    print(" ============================================================================ ")
    print(" ============================================================================ ")


#======================================================================================================================#
#======================================================================================================================#
def menu_metodo_pagamento():
    print("                                                                ")
    print(" ============================================================== ")
    print(" ||||          MENU MÉTODOS DE PAGAMENTOS - ( 5 )          |||| ")
    print(" ============================================================== ")
    print(" ||||                                                      |||| ")
    print(" ||||  1 - Tipos de Métodos de Pagamento                   |||| ")
    print(" ||||                                                      |||| ")
    print(" ||||  2 - Percentagem de Uso de Cada Forma de Pagamento   |||| ")
    print(" ||||                                                      |||| ")
    print(" ||||  3 - Método de Pagamento que gerou Mais Lucro        |||| ")
    print(" ||||                                                      |||| ")
    print(" ||||  4 - Método de Pagamento mais comum por genero       |||| ")
    print(" ||||                                                      |||| ")
    print(" ||||  5 - Relação entre Preço Venda e Método Pagamento    |||| ")
    print(" ||||                                                      |||| ")
    print(" ||||  6 - Voltar                                          |||| ")
    print(" ||||                                                      |||| ")
    print(" ============================================================== ")
    print(" ============================================================== ")


#======================================================================================================================#
#======================================================================================================================#
def menu_metodo_envio():
    print("                                                                ")
    print(" ============================================================== ")
    print(" ||||            MENU MÉTODOS DE ENVIO - ( 6 )             |||| ")
    print(" ============================================================== ")
    print(" ||||                                                      |||| ")
    print(" ||||    1 - Tipos de Métodos de Envio                     |||| ")
    print(" ||||                                                      |||| ")
    print(" ||||    2 - Relação Entre tipo de Envio e a Localização   |||| ")
    print(" ||||                                                      |||| ")
    print(" ||||    3 - Relação entre Prazo entrega e Avaliação       |||| ")
    print(" ||||                                                      |||| ")
    print(" ||||    4 - Voltar                                        |||| ")
    print(" ||||                                                      |||| ")
    print(" ============================================================== ")
    print(" ============================================================== ")


#======================================================================================================================#
#======================================================================================================================#
def main():

    opcao = 0

    while opcao != 8:

        layout_inicial()

        menu_principal()

        opcao = int(input("Intruza a opçao desejada: "))

##----------------------------------------------------------------------------------------------------------------

        if opcao == 1:

            menu1 = 0

            while menu1 != 4:

                menu_clientes()

                menu1 = int(input("Intruza a opçao desejada: "))

                if menu1 == 1:
                    Clientes.mostrar_inf_clientes()

                elif menu1 == 2:
                    Clientes.distribuicao_idade()

                elif menu1 == 3:
                    Clientes.distribuicao_localidade()

                elif menu1 == 4:
                    break

                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")

##----------------------------------------------------------------------------------------------------------------

        elif opcao == 2:

            menu2 = 0

            while menu2 != 9:

                menu_vendas()

                menu2 = int(input("Intruza a opçao desejada: "))

                if menu2 == 1:
                    Produtos.prod_mais_vendidos_por_regiao()

                elif menu2 == 2:
                    Produtos.prod_menos_vendidos_por_regiao()

                elif menu2 == 3:
                    Produtos.total_vendas_por_categorias()

                elif menu2 == 4:
                    Compras.dia_e_mes_mais_compras_por_cor()

                elif menu2 == 5:
                    Vendas.distribuicao_produtos_preco_venda()

                elif menu2 == 6:
                    Compras.valor_compras_por_local_e_dia()

                elif menu2 == 7:
                    Vendas.venda_por_tamanho_e_cor()

                elif menu2 == 8:
                    Compras.dia_e_mes_mais_compra_de_uma_categoria()

                elif menu2 == 9:
                    break

                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")

##----------------------------------------------------------------------------------------------------------------

        elif opcao == 3:

            menu4 = 0

            while menu4 != 3:

                menu_produtos()

                menu4 = int(input("Intruza a opçao desejada: "))

                if menu4 == 1:
                    Produtos.top5_prod_de_uma_categoria_por_cor()

                elif menu4 == 2:
                    Produtos.tamanho_com_mais_lucro()

                elif menu4 == 3:
                    break

                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")

##----------------------------------------------------------------------------------------------------------------

        elif opcao == 4:

            menu5 = 0

            while menu5 != 6:

                menu_avalicao()

                menu5 = int(input("Intruza a opçao desejada: "))

                if menu5 == 1:
                    Avaliaçao.maior_avaliaçao_por_cidade()

                elif menu5 == 2:
                    Avaliaçao.menor_avaliaçao_por_cidade()

                elif menu5 == 3:
                    Avaliaçao.top_5_avaliacao_por_categoria()

                elif menu5 == 4:
                    Avaliaçao.clientes_insatisfeitos_por_localizacao_e_produto()

                elif menu5 == 5:
                    Avaliaçao.satisfacao_por_data()

                elif menu5 == 6:
                    break

                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")

##----------------------------------------------------------------------------------------------------------------

        elif opcao == 5:

            menu6 = 0

            while menu6 != 6:

                menu_metodo_pagamento()

                menu6 = int(input("Intruza a opçao desejada: "))

                if menu6 == 1:
                    Metodo_pagamento.tipos_metodo_pagamento()

                elif menu6 == 2:
                    Metodo_pagamento.metodo_pagamento_por_distribuicao()

                elif menu6 == 3:
                    Metodo_pagamento.metodo_pagamento_com_mais_lucro()

                elif menu6 == 4:
                    Metodo_pagamento.metodo_pagamento_por_sexo()

                elif menu6 == 5:
                    Vendas.relacao_preco_venda_forma_pagamento()

                elif menu6 == 6:
                    break

                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")

##----------------------------------------------------------------------------------------------------------------

        elif opcao == 6:

            menu7 = 0

            while menu7 != 5:

                menu_metodo_envio()

                menu6 = int(input("Intruza a opçao desejada: "))

                if menu6 == 1:
                    Entregas.tipos_entrega()

                elif menu6 == 2:
                    Entregas.relacao_tipo_envio_localizacao()

                elif menu6 == 3:
                    Avaliaçao.relacao_prazo_entrega_revisao()

                elif menu6 == 4:
                    break

                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")

    ##----------------------------------------------------------------------------------------------------------------

        elif opcao == 7:
            print("Saindo...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.") 

#======================================================================================================================#
#======================================================================================================================#


if __name__ == "__main__":
    main()