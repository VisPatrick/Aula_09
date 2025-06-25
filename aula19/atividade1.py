#   pip install sqlalchemy pymysql pandas matplotlib numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   # biblioteca de gráficos

try:
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    df_ocorrencia = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    # print(df_ocorrencia)
#   VARIÁVEIS
    df_ocorrencia = df_ocorrencia[['munic', 'estelionato']]
#   AGRUPANDO
    df_ocorrencia = df_ocorrencia.groupby('munic').sum(['estelionato']).reset_index()
    print(df_ocorrencia.to_string())
except Exception as e:
    print(f"Erro de conexão: {e}")
    exit()

#   ANALISE DE DADOS


try:
    print('\nOBTENDO INFORMAÇÕES SOBRE ESTELIONATOS')
    array_estelionatos = np.array(df_ocorrencia['estelionato'])
    media_estelionato = np.mean(array_estelionatos)
    mediana_estelionato = np.median(array_estelionatos)
    distancia = abs((media_estelionato - mediana_estelionato)) / mediana_estelionato

    # print('\nMEDIAS')
    # print(30*'~')
    # print(f'Média: {media_estelionato:.2f}')
    # print(f'Mediana: {mediana_estelionato:.2f}')
    # print(f'Distancia entre médias: {distancia:.2f}')

#   MEDIDAS DE DISPERSÃO #  dispersão é a variação dos dados em relação à média
    print('\nMEDIDAS DE DISPERSÃO')
    print(67*'~')
    maximo = np.max(array_estelionatos)
    minimo = np.min(array_estelionatos)
    amplitude_total = maximo - minimo # amplitude total é a diferença entre o maior e o menor valor

    # print(f'Máximo: {maximo}')
    # print(f'Mínimo: {minimo}')
    # print(f'Amplitude Total: {amplitude_total}')

#   MEDIDAS DE POSIÇÃO

#   QUARTIL
    q1 = np.quantile(array_estelionatos, 0.25)
    q2 = np.quantile(array_estelionatos, 0.50)
    q3 = np.quantile(array_estelionatos, 0.75)

    print('\nMEDIDAS DE POSSIÇÃO')
    print(30*'~')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')

#   MINIC COM MENOS CASOS
    df_menor_estelionato = df_ocorrencia[df_ocorrencia['estelionato'] <q1]
#   MUNIC COM MAIS CASOS
    df_maior_estelionato = df_ocorrencia[df_ocorrencia['estelionato'] <q3]

    print('\nMUNIC COM MENORES CASOS SE ESTELIONATO')
    print(67*'~')
    print(df_menor_estelionato.sort_values(by='estelionato', ascending=True))

    print('\nMUNIC COM MAIORES CASOS SE ESTELIONATO')
    print(67*'~')
    print(df_menor_estelionato.sort_values(by='estelionato', ascending=False))

#   INDENTIFICANDO OUTLIERS
    #   IQR
    iqr = q3 - q1

    limite_superior = q3 + (1.5 * iqr)
    limite_inferio = q1 - (1.5 * iqr)

    # print("\nLimites - Medidas de Posição")
    # print(67*'~')
    # print(f'Limites inferior: {limite_inferio}')
    # print(f'Limites superior: {limite_superior}')

    print('\nMEDIDAS')
    print(67*'=')
    print(f'Limite Inferior: {limite_inferio:.2f}')
    print(f'Menor Valor: {minimo:.2f}')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')
    print(f'IQR: {iqr:.2f}')    # interquartil range é a diferença entre o terceiro quartil e o primeiro quartil
    print(f'Maior Valor: {maximo:.2f}')
    print(f'Limite Superior: {limite_superior:.2f}')
    print(f'Média: {media_estelionato:.2f}')
    print(f'Mediana: {mediana_estelionato:.2f}')
    print(f'Distância entre médias: {distancia:.2f}')

#   MEDIDAS DE DISPERSÃO  # dispersão é a variação dos dados em relação à média
    #   VARIÂNCIA
    variancia = np.var(array_estelionatos)
    #   DISTANCIA ENTRE MÉDIA E VARIÂNCIA
    distancia_var_media = variancia / media_estelionato
    #   DESVIO PADRÃO
    desvio_padrao = np.std(array_estelionatos)
    #   COEFICIENTE DE VARIAÇÃO
    coeficiente_variacao = (desvio_padrao / media_estelionato) * 100    # coeficiente de variação é a relação entre o desvio padrão e a média, expressa em porcentagem

    print('\nMEDIDAS DE DISPERSÃO')
    print(67*'=')
    print(f'Variância: {variancia:.2f}')
    print(f'Distância entre média e variância: {distancia_var_media:.2f}')
    print(f'Desvio Padrão: {desvio_padrao:.2f}')
    print(f'Coeficiente de Variação: {coeficiente_variacao:.2f}%')

#   OUTILIERS
    df_estelionato_outliers_inferior = df_ocorrencia[df_ocorrencia['estelionato'] < limite_inferio]
    df_estelionato_outliers_superior = df_ocorrencia[df_ocorrencia['estelionato'] > limite_superior]

#   OUTLIERS INFERIORES
    print(f'\nOutliers Inferiores')
    print(67*'~')
    if len(df_estelionato_outliers_inferior) == 0:
        print('Não há outliers inferiores')
    else:
        print(df_estelionato_outliers_inferior.sort_values(by='estelionato', ascending=True))

#   OUTLIERS SUPERIORES
    print(f'\nOutliers Superiores')
    print(67*'~')
    if len(df_estelionato_outliers_superior) == 0:
        print('Não há outliers superiores')
    else:
        print(df_estelionato_outliers_superior.sort_values(by='estelionato', ascending=False))


except Exception as u:
    print('Erro de informações: {u}')

#   PLOTANDO GRÁFICO COM MATPLOTLIB
try:
    # import matplotlib.pyplot as plt
    # fig, ax = plt.subplots(figsize=(10, 6))
    # ax.boxplot(array_roubo_veiculo, vert=False, showmeans=True)
    plt.subplots(2, 2, figsize=(16, 10))
    plt.suptitle('Análise de Estelionato RJ')

    # POSIÇÃO 01
    # BOXPLOT
    plt.subplot(2, 2, 1)
    plt.boxplot(array_estelionatos, vert=False, showmeans=True)
    plt.title("Boxplot dos Dados")

    # POSIÇÃO 02
    # MEDIDAS
    # Exibição de informações estatísticas
    plt.subplot(2, 2, 2)
    plt.title('Medidas Estatísticas')
    plt.text(0.1, 0.9, f'Limite inferior: {limite_inferio}', fontsize=10)
    plt.text(0.1, 0.8, f'Menor valor: {minimo}', fontsize=10)
    plt.text(0.1, 0.7, f'Q1: {q1}', fontsize=10)
    plt.text(0.1, 0.6, f'Mediana: {mediana_estelionato}', fontsize=10)
    plt.text(0.1, 0.5, f'Q3: {q3}', fontsize=10)
    plt.text(0.1, 0.4, f'Média: {media_estelionato:.3f}', fontsize=10)
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
    if not df_estelionato_outliers_inferior.empty:
        dados_inferiores = df_estelionato_outliers_inferior.sort_values(by='roubo_veiculo', ascending=True)     # crescente
        # Gráfico de Barras
        plt.barh(dados_inferiores['munic'], dados_inferiores['estelionato'], color='red')
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
    if not df_estelionato_outliers_superior.empty:
        dados_superiores = df_estelionato_outliers_superior.sort_values(by='estelionato', ascending=True)

        # Cria o gráfico e guarda as barras
        barras = plt.barh(dados_superiores['munic'], dados_superiores['estelionato'], color='purple')
        # Adiciona rótulos nas barras
        plt.bar_label(barras, fmt='%.0f', label_type='edge', fontsize=8, padding=2)
        
        # Diminui o tamanho da fonte dos eixos
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)

        plt.title('Outliers Superiores')
        # plt.xlabel('Total Estelionatos')
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

print('\nAnálise concluída com sucesso!')
print(67*'=')
print("Analisando os dados pude observar que o estado do Rio de Janeiro possui um grande número de estelionatos (o que me espantou), principalmente na capital,"\
" e que com base no q1 e q3, podemos observar que a maioria dos municípios" \
" apresenta valores abaixo da média, o que indica que a maioria dos municípios possui uma incidência menor de estelionatos, " \
" com tudo uma grande variação entre os municípios, o que indica que alguns locais possuem uma incidência muito maior de estelionatos do que outros. Além disso, a presença de " \
" outliers sugere que existem municípios com casos extremos de estelionatos, o que pode indicar problemas específicos nessas áreas.")


#   explicação dos dados analisados
#   O código analisa dados de ocorrências de estelionatos no estado do Rio de Janeiro, agrupando por município e realizando diversas análises estatísticas.
#   Ele calcula medidas de tendência central (média, mediana), medidas de dispersão (variância, desvio padrão, coeficiente de variação), medidas de posição (quartis) e identifica outliers.
#   Além disso, o código gera gráficos para visualizar as distribuições dos dados e as medidas estatísticas, facilitando a interpretação dos resultados.
#   O objetivo é fornecer uma visão geral dos estelionatos no estado, identificando padrões e anomalias nos dados.