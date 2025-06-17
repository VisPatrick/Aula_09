#   pip install sqlalchemy pymysql pandas matplotlib numpy
import pandas as pd
import numpy as np

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

    print(f'Máximo: {maximo}')
    print(f'Mínimo: {minimo}')
    print(f'Amplitude Total: {amplitude_total}')

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
    print(f'Menor ')

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