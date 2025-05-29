import pandas as pd
import matplotlib.pyplot as plt

# Cálculo das Médias das Variáveis

df = pd.read_excel('Base de Dados.xlsx')
def calcular_media(df, coluna):
  media = df[coluna].mean()
  return print(f"Média de '{coluna.strip()}': {media}")
calcular_media(df, 'Erros_Reportados\xa0')
calcular_media(df, 'Tempo_Conclusao\xa0')
calcular_media(df, 'Produtividade\xa0')
calcular_media(df, 'Experiencia\xa0')

# Cálculo do Desvio padrão das Variáveis

def calcular_desvio_padrao(coluna):
    desvio = df[coluna].std()
    print(f"Desvio padrão de '{coluna.strip()}': {desvio:.2f}")
calcular_desvio_padrao('Erros_Reportados\xa0')
calcular_desvio_padrao('Tempo_Conclusao\xa0')
calcular_desvio_padrao('Produtividade\xa0')
calcular_desvio_padrao('Experiencia\xa0')

# Base para Verificar Outliers

sequencia = df['Erros_Reportados\xa0']
id = 0
for numero in sequencia:
    id +=1
    if numero > 6:
      print(f"/\ Acima do Padrão {id} = {numero}")
    elif numero < 2:
      print(f"\/ Abaixo do Padrão {id} = {numero}")

df.columns = ['ID', 'Produtividade', 'Experiencia', 'Erros_Reportados', 'Tempo_Conclusao']

df['Tempo_Conclusao'] = df['Tempo_Conclusao'].round(0).astype(int)
df['Produtividade'] = df['Produtividade'].round(0).astype(int)

def box_plot(df, coluna, titulo, xlabel, cor=''):
    contagem = df[coluna].value_counts().sort_index()
    print(f"\n{titulo} (Tabela):")
    print(pd.DataFrame({
        coluna: [f"{i} {xlabel.lower() + ('s' if i != 1 else '')}" for i in contagem.index],
        'Pessoas': contagem.values
    }).to_string(index=False))

    plt.figure(figsize=(10, 4))
    box = plt.boxplot(df[coluna], vert=False, patch_artist=True)

    for pedaco in box['boxes']:
        pedaco.set_facecolor(cor)

    plt.title(f'Box Plot de {titulo}')
    plt.xlabel(xlabel)
    plt.tight_layout()
    plt.show()

def grafico_pessoas_por_categoria(df, coluna, titulo, xlabel, cor):
    contagem = df[coluna].value_counts().sort_index()
    print(f"\n{titulo} (Tabela):")
    print(pd.DataFrame({
        coluna: [f"{i} {xlabel.lower() + ('s' if i != 1 else '')}" for i in contagem.index],
        'Pessoas': contagem.values
    }).to_string(index=False))

    plt.figure(figsize=(10, 4))
    plt.bar(contagem.index, contagem.values, color=cor)
    plt.title(f'Pessoas por {titulo}')
    plt.xlabel(xlabel)
    plt.ylabel('Número de Pessoas')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

# Gráficos de barras para as variáveis
grafico_pessoas_por_categoria(df, 'Erros_Reportados', 'Quantidade de Erros', 'Erro', 'red')
grafico_pessoas_por_categoria(df, 'Tempo_Conclusao', 'Tempo de Conclusão', 'Hora', 'orange')
grafico_pessoas_por_categoria(df, 'Produtividade', 'Produtividade (Linhas/Dia)', 'Linha', 'green')
grafico_pessoas_por_categoria(df, 'Experiencia', 'Experiência', 'Ano de Experiência', 'skyblue')

# Box plots para cada variável
box_plot(df, 'Erros_Reportados', 'Quantidade de Erros', 'Erro', 'red')
box_plot(df, 'Tempo_Conclusao', 'Tempo de Conclusão', 'Hora', 'orange')
box_plot(df, 'Produtividade', 'Produtividade (Linhas/Dia)', 'Linha', 'green')
box_plot(df, 'Experiencia', 'Experiência', 'Ano de Experiência', 'skyblue')