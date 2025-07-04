# from utils import limpar_nome_municipio
#   pip install matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt    # biblioteca de gráficos


try:
    ENDERECO_DADOS = "https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"

    df_ocorrencia = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # print(df_ocorrencia.head())

    #   DELIMITANDO VARIÁVEIS

    df_ocorrencia = df_ocorrencia[['munic', 'roubo_veiculo']]

#   TOTALIZANDO

    df_roubo_veiculo = df_ocorrencia.groupby('munic').sum(['roubo_veiculo']).reset_index()

    print(df_roubo_veiculo.to_string())

except Exception as e:

    print(f"Errdo de conexão: {e}")

    exit()

#   INICIALIZANDO ANÁLISE

try:

    print('Obtendo informações sobre padrão de roubos de veículos...')

    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])
    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
    distancia= abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo)


#   MEDIDAS DE POSIÇÃO

#   QUARTIL

    q1 = np.quantile(array_roubo_veiculo, 0.25, method='weibull')
    q2 = np.quantile(array_roubo_veiculo, 0.50, method='weibull')
    q3 = np.quantile(array_roubo_veiculo, 0.75, method='weibull')

    # print("\nMEDIDAS DE POSIÇÃO")
    # print(f'Média: {media_roubo_veiculo}')
    # print(f'Mediana: {mediana_roubo_veiculo}')
    # print(f'Distância entre a média e mediana {distancia:.3f}')

#   MEDIDAS DE DISPERSÃO

    print("\nMEDIDAS DE DISPERSÃO")
    print(67*'~')
    maximo = np.max(array_roubo_veiculo)
    minimo = np.min(array_roubo_veiculo)

    amplitude_total = maximo - minimo   # amplitude total: diferença entre o maior e o menor valor

    # print("\nMEDIDAS DE POSIÇÃO")

    # print(f'Q1: {q1}')
    # print(f'Q2: {q2}')
    # print(f'Q3: {q3}')

#   ROUBO MAIS E ROUBO MENOS

#   MENOR ROUBOS

    df_roubo_veiculo_menores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] <q1]

#   MAIOR ROUBOS

    df_roubo_veiculo_maiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] >q3]
    print('\nMunicípio com Menores números de Roubos')
    print(df_roubo_veiculo_menores.sort_values(by='roubo_veiculo', ascending=True))
    print('\nMunicípios com Maior números de Roubos')
    print(df_roubo_veiculo_maiores.sort_values(by='roubo_veiculo', ascending=False))

#   INDENTIFICANDO OUTLIERS

    #   IQR
    iqr = q3 - q1

    limite_superior = q3 + (1.5 * iqr)
    limite_inferio = q1 - (1.5 * iqr)

    # print("\nLimites - Medidas de Posição")
    # print(f'Limites inferior: {limite_inferio}')
    # print(f'Limites superior: {limite_superior}')

    print("\nMEDIDAS")
    print(67*'~')
    print(f'Limite inferior: {limite_inferio}')
    print(f'Menor Valor: {minimo}')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')
    print(f'IQR: {iqr}')
    print(f'Maior Valor: {maximo}')
    print(f'Limite superior: {limite_superior}')
    print(f'Média: {media_roubo_veiculo}')
    print(f'Mediana: {mediana_roubo_veiculo}')
    print(f'distancia média e mediana: {distancia}')

    #   MEDIDAS  DE DISPERSÃO # MEDE A VARIAÇÃO DOS DADOS EM RELAÇÃO ÀS MÉDIDAS DE POSIÇÃO
    #   VARIÂNCIA: é a média dos quadrados das diferenças entre cada valor e a média dos valores. sempre uma potencia de 2, ou seja, sempre positiva.
    variancia = np.var(array_roubo_veiculo) # VAR é a variância, que é a média dos quadrados das diferenças entre cada valor e a média dos valores

    # DISTANCIA ENTRE MÉDIA E VARIÂNCIA
    distancia_var_media = variancia / (media_roubo_veiculo ** 2)

#   DESVIO PADRÃO: é a raiz quadrada da variância, mede a dispersão dos dados em relação à média. É uma medida de dispersão mais intuitiva, pois está na mesma unidade dos dados originais.
    desvio_padrao = np.std(array_roubo_veiculo)  # STD é o desvio padrão, que é a raiz quadrada da variância

#   COEFICIENTE DE VARIAÇÃO: é o desvio padrão dividido pela média, multiplicado por 100, expressando a variabilidade relativa dos dados em relação à média.
    coef_variacao = (desvio_padrao / media_roubo_veiculo) * 100  # Coeficiente de Variação: é o desvio padrão dividido pela média, multiplicado por 100, expressando a variabilidade relativa dos dados em relação à média.

    print('\nMedidas de Dispersão')
    print(67*'~')
    print(f'Variância: {variancia:.3f}')
    print(f'Distância entre média e variância: {distancia_var_media:.3f}')
    print(f'Desvio Padrão: {desvio_padrao:.3f}')
    print(f'Coeficiente de Variação: {coef_variacao:.3f}%')

#   DESCOBRINDO oUTLIERS

    df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior]

    df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferio]


#   OUTLIERS INFERIORES
    print(f'\nOutliers Inferiores')

    if len(df_roubo_veiculo_outliers_inferiores) == 0:

        print('Não há outliers inferiores')

    else:

        print(df_roubo_veiculo_outliers_inferiores.sort_values(by='roubo_veiculo', ascending=True))


#   OUTLIERS SUPERIORES

    print(f'\nOutliers Superiores') 

    if len(df_roubo_veiculo_outliers_superiores) == 0:
        print('Não há outliers Superiores')

    else:

        print(df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=False))

except Exception as e:

    print(f"Erro de processamento de dados: {e}")

    exit()

#   SE PASSOU DO LIMITE É OUTLIER, SE NÃO PASSOU DO LIMITE NÃO É OUTLIEr

# IQR MEDIDA DE DISPERSÃO NAO PADRONIZADA

# PLOTANDO GRÁFICO
# Matplotlib
try:
    # import matplotlib.pyplot as plt
    # fig, ax = plt.subplots(figsize=(10, 6))
    # ax.boxplot(array_roubo_veiculo, vert=False, showmeans=True)
    plt.subplots(2, 2, figsize=(16, 10))
    plt.suptitle('Análise de roubo de veículos no RJ')

    # POSIÇÃO 01
    # BOXPLOT
    plt.subplot(2, 2, 1)
    plt.boxplot(array_roubo_veiculo, vert=False, showmeans=True)
    plt.title("Boxplot dos Dados")

    # POSIÇÃO 02
    # MEDIDAS
    # Exibição de informações estatísticas
    plt.subplot(2, 2, 2)
    plt.title('Medidas Estatísticas')
    plt.text(0.1, 0.9, f'Limite inferior: {limite_inferio}', fontsize=10)
    plt.text(0.1, 0.8, f'Menor valor: {minimo}', fontsize=10)
    plt.text(0.1, 0.7, f'Q1: {q1}', fontsize=10)
    plt.text(0.1, 0.6, f'Mediana: {mediana_roubo_veiculo}', fontsize=10)
    plt.text(0.1, 0.5, f'Q3: {q3}', fontsize=10)
    plt.text(0.1, 0.4, f'Média: {media_roubo_veiculo:.3f}', fontsize=10)
    plt.text(0.1, 0.3, f'Maior valor: {maximo}', fontsize=10)
    plt.text(0.1, 0.2, f'Limite superior: {limite_superior}', fontsize=10)
    plt.text(0.5, 0.9, f'Distância Média e Mediana: {distancia:.4f}', fontsize=10)
    plt.text(0.5, 0.8, f'IQR: {iqr}', fontsize=10)
    plt.text(0.5, 0.7, f'Amplitude Total: {amplitude_total}', fontsize=10)

    # POSIÇÃO 03
    # OUTLIERS INFERIORES
    plt.subplot(2, 2, 3)
    plt.title('Outliers Inferiores')
    # Se o DataFrame do outliers não estiver vazio
    if not df_roubo_veiculo_outliers_inferiores.empty:
        dados_inferiores = df_roubo_veiculo_outliers_inferiores.sort_values(by='roubo_veiculo', ascending=True)     # crescente
        # Gráfico de Barras
        plt.barh(dados_inferiores['munic'], dados_inferiores['roubo_veiculo'])
    else:
        # Se não houver outliers
        plt.text(0.5, 0.5, 'Sem Outliers Inferiores', ha='center', va='center', fontsize=12)
        plt.title('Outilers Inferiores')
        plt.xticks([])
        plt.yticks([])

    # POSIÇÃO 04
    # OUTLIERS SUPERIORES
    plt.subplot(2, 2, 4)
    plt.title('Outliers Superiores')
    if not df_roubo_veiculo_outliers_superiores.empty:
        dados_superiores = df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=True)

        # Cria o gráfico e guarda as barras
        barras = plt.barh(dados_superiores['munic'], dados_superiores['roubo_veiculo'], color='black')
        # Adiciona rótulos nas barras
        plt.bar_label(barras, fmt='%.0f', label_type='edge', fontsize=8, padding=2)

        # Diminui o tamanho da fonte dos eixos
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)

        plt.title('Outliers Superiores')
        plt.xlabel('Total Roubos de Veículos')
    else:
        # Se não houver outliers superiores, exibe uma mensagem no lugar.
        plt.text(0.5, 0.5, 'Sem outliers superiores', ha='center', va='center', fontsize=12)
        plt.title('Outliers Superiores')
        plt.xticks([])
        plt.yticks([])

    # Ajusta os espaços do layout para que os gráficos não fiquem espremidos
    plt.tight_layout()
    # Mostra a figura com os dois gráficos
    plt.show()

except Exception as e:
    print(f'Erro ao plotar {e}')
    exit()

#   se os dados forem heterogeêneos, ou seja, se os dados forem muito diferentes entre si,
#   o desvio padrão será maior, indicando que os dados estão mais dispersos em relação à média.
#   Se os dados forem homogêneos, o desvio padrão será menor,
#   indicando que os dados estão mais próximos da média.